import sys
import os
import unittest

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from utils import get_environment_variables, load_env_variables

class TestUtils(unittest.TestCase):

    def test_get_environment_variables(self):
        # Check if TEST_MODE environment variable is set
        test_mode = os.getenv('TEST_MODE', 'false').lower() == 'true'
        load_env_variables(test_mode=test_mode)

        expected_env_vars = {
            'JWT_TOKEN': 'test_jwt_token',
            'WP_HOST': 'test_wp_host',
            'CD_PATH': '/test/chromedriver',
            'TITLE': 'Test Title',
            'DL_PATH': '/test/download/path',
            'IMG': 'test_image',
            'OPENAI_API_KEY': 'test_openai_api_key'
        }
        env_vars = get_environment_variables(test_mode=test_mode)
        self.assertEqual(env_vars, expected_env_vars)

if __name__ == '__main__':
    unittest.main()