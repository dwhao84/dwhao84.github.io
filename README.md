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
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        .project-card:hover {
            transform: translateY(-5px);
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
        }
        .project-links a {
            display: inline-flex;
            align-items: center;
            padding: 8px 12px;
            background: #0071e3;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-size: 0.9em;
            transition: background 0.3s ease;
        }
        .project-links a:hover {
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
    </header>

    <div class="github-stats">
        <img src="https://github-readme-stats.vercel.app/api?username=dwhao84&show_icons=true&theme=radical" alt="GitHub stats">
        <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=dwhao84&layout=donut" alt="Top Languages">
    </div>

    <div class="projects">
        <div class="project-card">
            <h3>Drink Order App</h3>
            <p>A custom drink ordering application showcasing UI design and order management.</p>
            <div class="project-links">
                <a href="https://github.com/dwhao84/DrinkOrderApp"><i class="fab fa-github"></i> GitHub</a>
                <a href="https://medium.com/彼得潘的-swift-ios-app-開發教室/hw-50-drink-order-app-1-get-6d4f7566c6f5"><i class="fab fa-medium"></i> Medium</a>
            </div>
        </div>

        <div class="project-card">
            <h3>App Store Clone</h3>
            <p>Recreation of the App Store interface demonstrating UIKit proficiency.</p>
            <div class="project-links">
                <a href="https://github.com/dwhao84/HW48-App-store"><i class="fab fa-github"></i> GitHub</a>
                <a href="https://medium.com/彼得潘的-swift-ios-app-開發教室/hw-48-app-store-425538e1f98b"><i class="fab fa-medium"></i> Medium</a>
                <a href="https://apple.co/3SGTvDt"><i class="fab fa-app-store-ios"></i> App Store</a>
            </div>
        </div>

        <div class="project-card">
            <h3>YouBike API Integration</h3>
            <p>Implementation of JSON decoding and Core Data with the YouBike API.</p>
            <div class="project-links">
                <a href="https://github.com/dwhao84/HW-44-JSON-Decoder"><i class="fab fa-github"></i> GitHub</a>
                <a href="https://medium.com/彼得潘的-swift-ios-app-開發教室/hw-47-串接you-bike-api-資料存到core-data-70fa9782e915"><i class="fab fa-medium"></i> Medium</a>
            </div>
        </div>

        <div class="project-card">
            <h3>Psychological Quiz App</h3>
            <p>Interactive quiz application built with UIKit and Storyboard.</p>
            <div class="project-links">
                <a href="https://github.com/dwhao84/HW37_PsychologicalTest"><i class="fab fa-github"></i> GitHub</a>
                <a href="https://medium.com/彼得潘的-swift-ios-app-開發教室/hw-37-psychologicaltest-心理測驗-with-storyboard-747b1de293f7"><i class="fab fa-medium"></i> Medium</a>
            </div>
        </div>

        <div class="project-card">
            <h3>Multiple Choice Challenge</h3>
            <p>Educational app featuring multiple choice questions and scoring.</p>
            <div class="project-links">
                <a href="https://github.com/dwhao84/HW36_MultipleChoiceChallenge"><i class="fab fa-github"></i> GitHub</a>
                <a href="https://medium.com/彼得潘的-swift-ios-app-開發教室/hw36-multiple-choice-選擇題-d55c2e9e6089"><i class="fab fa-medium"></i> Medium</a>
            </div>
        </div>
    </div>
</body>
</html>