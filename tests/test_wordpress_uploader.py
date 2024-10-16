import sys
import os
import unittest
from unittest.mock import patch, MagicMock
from dotenv import load_dotenv, find_dotenv

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from wordpress_uploader import upload_image_to_wordpress, create_wordpress_post
from utils import load_env_variables

# Load .env file if it exists
dotenv_path = find_dotenv()
load_dotenv(dotenv_path) if dotenv_path else None

class TestWordpressUploader(unittest.TestCase):

    @patch('wordpress_uploader.requests.post')
    def test_upload_image_to_wordpress(self, mock_post):
        # Check if TEST_MODE environment variable is set
        test_mode = os.getenv('TEST_MODE', 'false').lower() == 'true'
        load_env_variables(test_mode=test_mode)

        # Mock the requests.post response
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {'id': 12345}
        mock_post.return_value = mock_response

        image_path = '/path/to/test_image.jpg'
        with patch('builtins.open', unittest.mock.mock_open(read_data=b'test_image_data')):
            upload_id = upload_image_to_wordpress(image_path)

        self.assertEqual(upload_id, 12345)
        mock_post.assert_called_once()
        args, kwargs = mock_post.call_args
        self.assertIn('Bearer test_jwt_token', kwargs['headers']['Authorization'])
        self.assertIn('test_wp_host', args[0])  # Check the first argument for the URL

    @patch('wordpress_uploader.requests.post')
    def test_create_wordpress_post(self, mock_post):
        # Check if TEST_MODE environment variable is set
        test_mode = os.getenv('TEST_MODE', 'false').lower() == 'true'
        load_env_variables(test_mode=test_mode)

        # Mock the requests.post response
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {'id': 67890}
        mock_post.return_value = mock_response

        title = 'Test Title'
        content = 'This is a test content'
        image_id = 12345
        create_wordpress_post(title, content, image_id)

        mock_post.assert_called_once()
        args, kwargs = mock_post.call_args
        self.assertIn('Bearer test_jwt_token', kwargs['headers']['Authorization'])
        self.assertIn('test_wp_host', args[0])  # Check the first argument for the URL
        self.assertEqual(kwargs['json']['title'], title)
        self.assertEqual(kwargs['json']['content'], content)
        self.assertEqual(kwargs['json']['featured_media'], image_id)

if __name__ == '__main__':
    unittest.main()