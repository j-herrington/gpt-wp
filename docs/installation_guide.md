# Installation Guide

Follow these steps to set up the GPT-WP project:

## Prerequisites

Before installing GPT-WP, ensure you have the following prerequisites installed and set up:

- Python 3.x
- WordPress installation with the REST API enabled
- Chrome browser
- Chromedriver compatible with your Chrome version
- OpenAI API key

## Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/jh3rr/gpt-wp.git
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd gpt-wp
    ```

3. **Install the Required Python Packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:
    Create a `.env` file in the root directory of the project with the following content:
    ```env
    # OpenAI API key
    OPENAI_API_KEY="your_openai_api_key_here"

    # WordPress configuration
    WP_HOST="your_wordpress_host_here"
    JWT_TOKEN="your_jwt_token_here"

    # Selenium Chrome Driver Path
    CD_PATH="/path/to/your/chromedriver"

    # Image download path
    DL_PATH="/path/to/image/download/directory"

    # Blog post title and image search term
    TITLE="Your Default Blog Post Title"
    IMG="Your Image Search Term"
    ```

## Notes

- **Chromedriver Permission Issues on Mac**: If you face permission issues with Chromedriver on Mac, navigate to System Preferences -> Security & Privacy and allow Chromedriver to run.
- Ensure all environment variables are correctly set in the `.env` file.
- Use `python-dotenv` to load environment variables into your Python environment.

If you encounter any issues during installation, refer to the [Troubleshooting](troubleshooting.md) section or open an issue on GitHub.