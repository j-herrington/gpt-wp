# User Guide

## Introduction

Welcome to GPT-WP, a project designed to streamline blogging by integrating OpenAI's GPT-3.5 Turbo model with WordPress. This guide provides instructions on how to use the GPT-WP project to generate and publish blog posts on WordPress.

## Generating and Publishing a Blog Post

1. **Ensure all environment variables are set**: Make sure your `.env` file contains all the required environment variables as described in the Configuration Guide.

2. **Run the CLI Script**:
    ```bash
    python cli.py --title "Your Blog Title"
    ```

The script will perform the following steps:
- Generate blog content using the title specified in your command line argument or `.env` file.
- Download a related image from Unsplash using the search term specified in your `.env` file.
- Upload the downloaded image to your WordPress site.
- Create a new WordPress post with the generated content and uploaded image.

## Troubleshooting

### Common Issues

1. **Chromedriver Permission Issues on Mac**:
    - If you face permission issues with Chromedriver on Mac, navigate to System Preferences -> Security & Privacy and allow Chromedriver to run.

2. **Environment Variables Not Set**:
    - Ensure your `.env` file is in the root directory and contains all necessary environment variables.
    - Use `python-dotenv` to load these variables into your Python environment.

3. **API Keys Not Working**:
    - Verify that your OpenAI API key and WordPress JWT token are correct and have the necessary permissions.

### Getting Help

If you encounter any issues not covered here, please open an issue on GitHub or contact the maintainers.


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

