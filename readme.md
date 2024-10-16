# GPT-WP

Generate blog content and publish to WordPress using OpenAI GPT-3.5-turbo. Includes image integration and automated testing.

## Features:
- **Automated Content Generation**: Create engaging blog posts using OpenAI GPT-3.5-turbo.
- **Image Integration**: Automatically download images from Unsplash to enhance blog content.
- **WordPress Publishing**: Effortlessly upload and publish posts on WordPress.
- **Automated Testing**: Generate and run tests to validate the content generation process.

## Project Structure

```plaintext
gpt-wp/
├── docs/
│   ├── user_guide.md
│   ├── api_documentation.md
│   ├── installation_guide.md
│   ├── configuration_guide.md
│   ├── contributing_guide.md
│   ├── release_notes.md
│   └── faq.md
├── gpt_wp/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── content_generator.py
│   ├── image_downloader.py
│   ├── main.py
│   ├── utils.py
│   └── wordpress_uploader.py
├── tests/
│   ├── __init__.py
│   ├── test_content_generator.py
│   ├── test_image_downloader.py
│   ├── test_utils.py
│   └── test_wordpress_uploader.py
├── venv/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```
## Installation

Please refer to the [installation guide](docs/installation_guide.md) for detailed instructions.

## Configuration

Please refer to the [configuration guide](docs/configuration_guide.md) for detailed instructions.

## Usage

1. **Generate blog content and post to WordPress:**

    ```bash
    gpt-wp --title "Your Blog Title"
    ```

2. **Run in test mode:**

    ```bash
    gpt-wp --title "Your Blog Title" --test-mode
    ```
   
## Running Tests

To run the tests:

1. **Set the `TEST_MODE` environment variable:**

    ```bash
    export TEST_MODE=true
    ```

2. **Run the tests using `pytest`:**

    ```bash
    PYTHONPATH=gpt_wp pytest tests/
    ```

3. **Run the tests using `unittest`:**

    ```bash
    PYTHONPATH=gpt_wp python -m unittest discover -s tests
    ```
   
## Contributing

Please refer to the [contributing guide](docs/contributing_guide.md) for detailed instructions on how to contribute to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.