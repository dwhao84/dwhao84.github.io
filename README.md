<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Da-Wei Hao - iOS Developer</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/js/all.min.js"></script>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f7;
        }
        header {
            text-align: center;
            margin-bottom: 40px;
        }
        h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            color: #1d1d1f;
        }
        h2 {
            font-size: 2em;
            margin: 40px 0 20px;
            color: #1d1d1f;
            text-align: center;
        }

        /* Download button styles */
        .download-section {
            text-align: center;
            margin: 20px 0;
        }
        .download-button {
            display: inline-flex;
            align-items: center;
            padding: 12px 24px;
            background-color: #34C759;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-size: 1.1em;
            font-weight: 500;
            transition: all 0.3s ease;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .download-button:hover {
            background-color: #30B352;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        .download-button i {
            margin-right: 8px;
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        .download-button {
            animation: pulse 2s infinite;
        }

        .github-stats {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 40px;
            flex-wrap: wrap;
        }
        .github-stats img {
            max-width: 100%;
            height: auto;
        }
        .projects {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 30px;
        }
        .project-card {
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        .project-card:hover {
            transform: translateY(-5px);
        }
        .project-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        .project-content {
            padding: 20px;
        }
        .project-card h3 {
            color: #1d1d1f;
            margin-bottom: 15px;
            font-size: 1.5em;
        }
        .project-links {
            display: flex;
            gap: 10px;
            margin-top: 15px;
            flex-wrap: wrap;
        }
        .project-links a {
            display: inline-flex;
            align-items: center;
            padding: 8px 12px;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-size: 0.9em;
            transition: background 0.3s ease;
        }
        .project-links a.github {
            background: #6e5494;
        }
        .project-links a.github:hover {
            background: #8a6bba;
        }
        .project-links a.medium {
            background: #000000;
        }
        .project-links a.medium:hover {
            background: #292929;
        }
        .project-links a.app-store {
            background: #0071e3;
        }
        .project-links a.app-store:hover {
            background: #0077ed;
        }
        .project-links i {
            margin-right: 5px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Da-Wei Hao</h1>
        <p>iOS Developer</p>
        <div class="download-section">
            <a href="path/to/your/resume.pdf" class="download-button" download>
                <i class="fas fa-file-download"></i>
                Download Resume
            </a>
        </div>
    </header>

    <div class="github-stats">
        <img src="https://github-readme-stats.vercel.app/api?username=dwhao84&show_icons=true&theme=radical" alt="GitHub stats">
        <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=dwhao84&layout=donut" alt="Top Languages">
    </div>

    <h2>iOS Projects</h2>

    <div class="projects">
        <!-- Projects go here, ensure images have valid paths -->
    </div>

</body>
</html>
