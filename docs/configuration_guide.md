# Configuration Guide

This guide provides instructions on how to configure the GPT-WP project.

## Environment Variables

The following environment variables need to be set for the project to function correctly. These can be set in a `.env` file in the root directory.

- `OPENAI_API_KEY`: Your OpenAI API key.
- `WP_HOST`: The host URL of your WordPress site.
- `JWT_TOKEN`: The JWT token for authentication with your WordPress site.
- `CD_PATH`: The path to your ChromeDriver executable.
- `DL_PATH`: The directory path where images will be downloaded.
- `TITLE`: The default title for the blog post.
- `IMG`: The default image search term.

## Example `.env` File

```plaintext
OPENAI_API_KEY=your_openai_api_key
WP_HOST=your_wordpress_host
JWT_TOKEN=your_jwt_token
CD_PATH=path_to_your_chromedriver
DL_PATH=path_to_download_directory
TITLE=default_title
IMG=default_image_search_term
```

## Notes

- Ensure all required environment variables are set before running the application.
- The `.env` file should not be committed to version control as it contains sensitive information. Ensure it is added to your `.gitignore` file.

For installation instructions, please refer to the [installation guide](installation_guide.md).