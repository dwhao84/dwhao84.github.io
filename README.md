
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
            text-align: left;
        }

        h2 {
            font-size: 2em;
            margin: 40px 0 20px;
            color: #1d1d1f;
            text-align: center;
        }

        /* GitHub Stats Section */
        .github-stats {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 40px;
            flex-wrap: wrap;
        }

        .github-stats img {
            height: 200px;
            width: auto;
            max-width: 100%;
        }

        /* Projects Section */
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
            object-position: top;
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
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-size: 0.9em;
            transition: all 0.3s ease;
            padding: 8px 12px;
        }

        .project-links a i {
            margin-right: 8px;
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

        /* Download Button Section */
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
            animation: pulse 2s infinite;
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

        footer {
            text-align: center;
            padding: 20px 0;
            margin-top: 40px;
            border-top: 1px solid #ddd;
        }

        .social-icons {
            display: flex;
            justify-content: center;
            gap: 20px;
        }

        .social-icons a {
            color: #333;
            font-size: 24px;
            transition: color 0.3s ease;
        }

        .social-icons a:hover {
            color: #0077b5;
        }

    </style>
</head>
<body>
    <header>
        <h1>Da-Wei Hao Portfolio</h1>
    </header>

    <div class="github-stats">
        <img src="https://github-readme-stats.vercel.app/api?username=dwhao84&show_icons=true&theme=radical" alt="GitHub stats">
        <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=dwhao84&layout=compact&theme=radical" alt="Top Languages">
    </div>

    <h2>iOS Projects</h2>

    <div class="projects">
        <!-- Drink Order App -->
        <div class="project-card">
            <img src="Kebuke_banner.png" alt="Drink Order App Screenshot" class="project-image">
            <div class="project-content">
                <h3>Drink Order App</h3>
                <p>A custom drink ordering application showcasing UI design and order management.</p>
                <div class="project-links">
                    <a href="https://github.com/dwhao84/DrinkOrderApp" class="github"><i class="fab fa-github"></i>GitHub</a>
                    <a href="https://medium.com/彼得潘的-swift-ios-app-開發教室/hw-50-drink-order-app-1-get-6d4f7566c6f5" class="medium"><i class="fab fa-medium"></i>Medium</a>
                </div>
            </div>
        </div>

        <!-- App Store App -->
        <div class="project-card">
            <img src="App_store.jpg" alt="App Store Clone Screenshot" class="project-image">
            <div class="project-content">
                <h3>App Store App</h3>
                <p>Recreation of the App Store interface demonstrating UIKit proficiency.</p>
                <div class="project-links">
                    <a href="https://github.com/dwhao84/HW48-App-store" class="github"><i class="fab fa-github"></i>GitHub</a>
                    <a href="https://medium.com/彼得潘的-swift-ios-app-開發教室/hw-48-app-store-425538e1f98b" class="medium"><i class="fab fa-medium"></i>Medium</a>
                </div>
            </div>
        </div>

        <!-- YouBike App -->
        <div class="project-card">
            <img src="Youbike_banner.jpg" alt="YouBike API Integration Screenshot" class="project-image">
            <div class="project-content">
                <h3>YouBike App</h3>
                <p>Implementation of JSON decoding and Core Data with the YouBike API.</p>
                <div class="project-links">
                    <a href="https://github.com/dwhao84/HW-44-JSON-Decoder" class="github"><i class="fab fa-github"></i>GitHub</a>
                    <a href="https://medium.com/彼得潘的-swift-ios-app-開發教室/hw-47-串接you-bike-api-資料存到core-data-70fa9782e915" class="medium"><i class="fab fa-medium"></i>Medium</a>
                </div>
            </div>
        </div>

        <!-- Psychological Quiz App -->
        <div class="project-card">
            <img src="https://via.placeholder.com/400x200" alt="Psychological Quiz App Screenshot" class="project-image">
            <div class="project-content">
                <h3>Psychological Quiz App</h3>
                <p>Interactive quiz application built with UIKit and Storyboard.</p>
                <div class="project-links">
                    <a href="https://github.com/dwhao84/HW37_PsychologicalTest" class="github"><i class="fab fa-github"></i>GitHub</a>
                    <a href="https://medium.com/彼得潘的-swift-ios-app-開發教室/hw-37-psychologicaltest-心理測驗-with-storyboard-747b1de293f7" class="medium"><i class="fab fa-medium"></i>Medium</a>
                </div>
            </div>
        </div>

        <!-- Multiple Choice App -->
        <div class="project-card">
            <img src="CleanShot 2024-10-09 at 21.54.07@2x.png" alt="Multiple Choice Challenge Screenshot" class="project-image">
            <div class="project-content">
                <h3>Multiple Choice App</h3>
                <p>Educational app featuring multiple choice questions and scoring.</p>
                <div class="project-links">
                    <a href="https://github.com/dwhao84/HW36_MultipleChoiceChallenge" class="github"><i class="fab fa-github"></i>GitHub</a>
                    <a href="https://medium.com/彼得潘的-swift-ios-app-開發教室/hw36-multiple-choice-選擇題-d55c2e9e6089" class="medium"><i class="fab fa-medium"></i>Medium</a>
                </div>
            </div>
        </div>
    </div>

    <div class="download-section">
        <a href="path/to/your/resume.pdf" class="download-button" download>
            <i class="fas fa-file-download"></i>Download Resume
        </a>
    </div>
       <footer>
        <div class="social-icons">
            <a href="https://github.com/dwhao84" target="_blank" rel="noopener noreferrer">
                <i class="fab fa-github"></i>
            </a>
            <a href="https://twitter.com/YourTwitterHandle" target="_blank" rel="noopener noreferrer">
                <i class="fab fa-twitter"></i>
            </a>
        </div>
    </footer>
</body>
</html>