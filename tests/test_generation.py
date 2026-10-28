import http.client
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import urllib.error

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import app_data
import generate_index
import generate_projects

APP = {'trackName': 'Example', 'trackViewUrl': 'https://apps.apple.com/app/id123',
       'artworkUrl512': 'https://example.com/icon.png', 'description': 'App', 'price': 0}


class GenerationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.cache_patch = patch.object(app_data, 'CACHE_PATH', self.root / '.cache/apps.json')
        self.cache_patch.start()

    def tearDown(self):
        self.cache_patch.stop()
        self.temp.cleanup()

    def test_primary_success_saves_cache(self):
        with patch.object(app_data, 'fetch_app_data', return_value={'data': [APP]}) as fetch:
            self.assertEqual(app_data.load_apps(), [APP])
            self.assertEqual(fetch.call_count, 1)
        self.assertEqual(json.loads(app_data.CACHE_PATH.read_text()), {'data': [APP]})

    def test_all_failures_try_backup(self):
        errors = [urllib.error.HTTPError('url', code, 'error', {}, None) for code in (403, 404, 429, 500)]
        errors += [urllib.error.URLError('offline'), TimeoutError(),
                   json.JSONDecodeError('bad', '', 0), UnicodeDecodeError('utf8', b'x', 0, 1, 'bad'),
                   ValueError('schema'), http.client.IncompleteRead(b'')]
        for error in errors:
            with self.subTest(error=type(error).__name__), patch.object(app_data, 'fetch_app_data', side_effect=[error, {'data': [APP]}]) as fetch:
                self.assertEqual(app_data.load_apps(), [APP])
                self.assertEqual(fetch.call_args_list[1].args[0], app_data.API_URLS[1])
            if isinstance(error, urllib.error.HTTPError):
                error.close()

    def test_cache_survives_outage(self):
        app_data.atomic_write(app_data.CACHE_PATH, json.dumps({'data': [APP]}))
        before = app_data.CACHE_PATH.read_bytes()
        with patch.object(app_data, 'fetch_app_data', side_effect=TimeoutError):
            self.assertEqual(app_data.load_apps(), [APP])
        self.assertEqual(app_data.CACHE_PATH.read_bytes(), before)

    def test_invalid_payloads(self):
        invalid = [None, [], {}, {'data': []}, {'data': {}}, {'data': [None]}]
        for key, value in [('trackName', None), ('trackViewUrl', 42), ('artworkUrl512', ''), ('description', None), ('price', 'free'), ('price', float('nan')), ('price', -1)]:
            invalid.append({'data': [dict(APP, **{key: value})]})
        for payload in invalid:
            with self.subTest(payload=payload), self.assertRaises(ValueError):
                app_data.validate_apps(payload)

    def test_timeout_and_validation_in_real_fetch(self):
        with patch.object(app_data.urllib.request, 'urlopen') as request:
            request.return_value.__enter__.return_value.read.return_value = b'{"data": []}'
            with self.assertRaises(ValueError):
                app_data.fetch_app_data('https://example.com')
            self.assertEqual(request.call_args.kwargs['timeout'], 15)

    def test_no_cache_preserves_both_pages(self):
        for module, filename, card in [(generate_index, 'index.md', 'app-card'), (generate_projects, 'projects.md', 'project-card')]:
            page = self.root / 'docs' / filename
            app_data.atomic_write(page, f'<a class="{card}">Existing</a>')
            before = page.read_bytes()
            with patch.object(module, 'ROOT', self.root), patch.object(app_data, 'fetch_app_data', side_effect=TimeoutError):
                module.main()
            self.assertEqual(page.read_bytes(), before)

    def test_missing_page_fails_closed(self):
        with self.assertRaises(RuntimeError):
            app_data.preserve_existing(self.root / 'missing.md', 'app-card')

    def test_corrupt_cache_does_not_generate(self):
        app_data.atomic_write(app_data.CACHE_PATH, '{broken')
        with patch.object(app_data, 'fetch_app_data', side_effect=TimeoutError):
            self.assertIsNone(app_data.load_apps())

    def test_medium_outage_preserves_homepage(self):
        page = self.root / 'docs/index.md'
        app_data.atomic_write(page, '<a class="article-card">Existing</a>')
        with patch.object(generate_index, 'ROOT', self.root), patch.object(generate_index, 'fetch_top_apps', return_value=[APP]), patch.object(generate_index, 'fetch_medium_articles', side_effect=TimeoutError):
            generate_index.main()
        self.assertEqual(page.read_text(), '<a class="article-card">Existing</a>')

    def test_failed_atomic_write_preserves_previous_content(self):
        page = self.root / 'existing.md'
        page.write_text('Existing')
        with patch.object(app_data.os, 'replace', side_effect=OSError('disk error')):
            with self.assertRaises(OSError):
                app_data.atomic_write(page, 'New')
        self.assertEqual(page.read_text(), 'Existing')
        self.assertEqual(list(self.root.iterdir()), [page])

    def test_valid_data_renders_both_pages(self):
        self.assertIn('Example', generate_index.generate_markdown([], [APP]))
        self.assertIn('免費', generate_projects.generate_markdown([APP]))


if __name__ == '__main__':
    unittest.main()
