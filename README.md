# DaWei's Portfolio Website

This is my personal portfolio website built with Hugo and the Blowfish theme.

## 🚀 Features

- **Modern Design**: Clean and professional layout using the Blowfish theme
- **Responsive**: Mobile-friendly design that works on all devices
- **Fast Loading**: Optimized for performance with Hugo's static site generation
- **SEO Optimized**: Built-in SEO features and structured data
- **Dark/Light Mode**: Automatic theme switching based on user preference

## 🛠️ Technology Stack

- **Hugo**: Static site generator
- **Blowfish Theme**: Modern, lightweight Hugo theme
- **Markdown**: Content written in Markdown
- **GitHub Pages**: Hosted on GitHub Pages

## 📁 Project Structure

```
├── config/           # Hugo configuration files
├── content/          # Markdown content files
├── static/           # Static assets (images, CSS, etc.)
├── themes/           # Hugo themes (Blowfish)
└── public/           # Generated static site (not in git)
```

## 🚀 Getting Started

### Prerequisites

- Hugo (v0.141.0 or later)
- Git

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/dwhao84/dwhao84.github.io.git
   cd dwhao84.github.io
   ```

2. Install Hugo theme dependencies:
   ```bash
   git submodule update --init --recursive
   ```

3. Start the development server:
   ```bash
   hugo server --buildDrafts
   ```

4. Open your browser and visit `http://localhost:1313`

### Building for Production

```bash
hugo --buildDrafts
```

The generated site will be in the `public/` directory.

## 📝 Content Management

### Adding New Pages

1. Create a new Markdown file in the `content/` directory
2. Add front matter with appropriate metadata
3. Write your content in Markdown

### Updating Existing Content

- Edit the Markdown files in the `content/` directory
- Images should be placed in the `static/assets/` directory
- Reference images using relative paths: `assets/image.png`

## 🎨 Customization

### Theme Configuration

The theme is configured in `config/_default/params.toml`. Key settings include:

- Color scheme and appearance
- Navigation menu
- Social links
- Homepage layout

### Styling

- Custom CSS can be added to `static/assets/extra.css`
- Theme variables can be overridden in the configuration files

## 📱 Content Sections

- **首頁 (Home)**: Main landing page with introduction
- **關於我 (About)**: Personal information and skills
- **專案 (Projects)**: Portfolio of iOS development projects
- **技術 (Tech)**: Technical skills and expertise
- **工作經驗 (Experience)**: Work history and achievements
- **聯絡方式 (Contact)**: Contact information and social links

## 🚀 Deployment

This site is automatically deployed to GitHub Pages when changes are pushed to the main branch.

### Manual Deployment

1. Build the site:
   ```bash
   hugo --buildDrafts
   ```

2. Deploy the `public/` directory to your hosting provider

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📞 Contact

- **Email**: dwsamurai84@gmail.com
- **GitHub**: [@dwhao84](https://github.com/dwhao84)
- **Medium**: [@dwsamurai84_dev](https://medium.com/@dwsamurai84_dev)
