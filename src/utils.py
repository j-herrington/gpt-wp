import os
from dotenv import load_dotenv, find_dotenv

def load_env_variables(test_mode=False):
    if test_mode:
        os.environ['OPENAI_API_KEY'] = 'test_openai_api_key'
        os.environ['WP_HOST'] = 'test_wp_host'
        os.environ['JWT_TOKEN'] = 'test_jwt_token'
        os.environ['CD_PATH'] = '/test/chromedriver'
        os.environ['DL_PATH'] = '/test/download/path'
        os.environ['TITLE'] = 'Test Title'
        os.environ['IMG'] = 'test_image'
    else:
        # Load environment variables from .env file if it exists
        dotenv_path = find_dotenv()
        if dotenv_path:
            load_dotenv(dotenv_path)

def get_environment_variables(test_mode=False) -> dict:
    """Fetch environment variables and return them in a dictionary."""
    env_vars = {
        'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY'),
        'WP_HOST': os.getenv('WP_HOST'),
        'JWT_TOKEN': os.getenv('JWT_TOKEN'),
        'CD_PATH': os.getenv('CD_PATH'),
        'DL_PATH': os.getenv('DL_PATH'),
        'TITLE': os.getenv('TITLE'),
        'IMG': os.getenv('IMG'),
    }

    # Check for missing values in real run
    if not all(env_vars.values()) and not test_mode:
        missing_vars = [key for key, value in env_vars.items() if value is None]
        raise EnvironmentError(f"Missing environment variables: {', '.join(missing_vars)}")

    return env_vars