import sys
import os
import unittest
from unittest.mock import patch, MagicMock
from dotenv import load_dotenv, find_dotenv

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from content_generator import generate_blog_content
from utils import load_env_variables

# Load .env file if it exists
dotenv_path = find_dotenv()
load_dotenv(dotenv_path) if dotenv_path else None

class TestContentGenerator(unittest.TestCase):

    @patch('content_generator.openai.ChatCompletion.create')
    def test_generate_blog_content(self, mock_create):
        # Check if TEST_MODE environment variable is set
        test_mode = os.getenv('TEST_MODE', 'false').lower() == 'true'
        load_env_variables(test_mode=test_mode)

        # Mock the OpenAI API response
        mock_response = MagicMock()
        mock_response.choices[0].message['content'].strip.return_value = "This is a test blog content for Test Title"
        mock_create.return_value = mock_response

        title = "Test Title"
        content = generate_blog_content(title)
        self.assertIsNotNone(content)
        self.assertIn("Test Title", content)

if __name__ == '__main__':
    unittest.main()