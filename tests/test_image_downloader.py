import sys
import os
import unittest
from unittest.mock import patch, MagicMock
from selenium.webdriver.common.keys import Keys  # Import Keys
from dotenv import load_dotenv, find_dotenv

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from image_downloader import download_image_from_unsplash
from utils import load_env_variables

# Load .env file if it exists
dotenv_path = find_dotenv()
load_dotenv(dotenv_path) if dotenv_path else None

class TestImageDownloader(unittest.TestCase):

    @patch('image_downloader.webdriver.Chrome')
    @patch('image_downloader.WebDriverWait')
    @patch('image_downloader.glob.glob')
    @patch('image_downloader.os.path.getctime')
    def test_download_image_from_unsplash(self, mock_getctime, mock_glob, mock_WebDriverWait, mock_Chrome):
        # Check if TEST_MODE environment variable is set
        test_mode = os.getenv('TEST_MODE', 'false').lower() == 'true'
        load_env_variables(test_mode=test_mode)

        # Setup mocks
        mock_driver = MagicMock()
        mock_Chrome.return_value = mock_driver

        # Mock search box and download button elements
        mock_search_box = MagicMock()
        mock_download_button = MagicMock()

        # Configure WebDriverWait to return these elements
        mock_WebDriverWait.return_value.until.side_effect = [mock_search_box, mock_download_button, lambda d: True]

        # Mock image download path and file globbing
        mock_glob.return_value = ['/path/to/downloaded_image.jpg']
        mock_getctime.return_value = 1234567890

        # Execute function
        search_term = "nature"
        download_path = "/path/to/download/"
        image_path = download_image_from_unsplash(search_term, download_path)

        # Assertions
        mock_Chrome.assert_called_once()
        mock_search_box.send_keys.assert_called_with(search_term + Keys.ENTER)
        mock_download_button.click.assert_called_once()
        mock_glob.assert_called_with(f"{download_path}*")
        mock_getctime.assert_called_once_with('/path/to/downloaded_image.jpg')
        self.assertEqual(image_path, '/path/to/downloaded_image.jpg')

if __name__ == '__main__':
    unittest.main()