# Website generators

Run `python scripts/generate_index.py` and `python scripts/generate_projects.py`
from the repository checkout. Run offline regression tests with
`python -m unittest discover -s tests -v`.

Both generators use `app_data.py`: each App endpoint has a 15-second socket
timeout. HTTP, connection, truncated response, JSON, encoding and schema errors
trigger the backup endpoint. Empty or partially invalid catalogs are rejected
as a whole. Only validated, non-empty responses atomically replace
`.cache/apps.json`; failures never overwrite that snapshot.

The deployment workflow restores the most recent snapshot with actions/cache
and saves it under a new run-specific key after a successful job. Cache entries
may be evicted by GitHub. If both APIs and the cache are unavailable, generators
leave the existing checked-in pages untouched. A missing page or one without
App cards stops deployment instead of publishing empty content. Medium errors
or empty feeds similarly preserve the homepage. Generated pages are written
atomically, and the deployment builds the site before publishing.
