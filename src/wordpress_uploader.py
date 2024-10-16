import os
import base64
import requests
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Determine if running in test mode
TEST_MODE = os.getenv('TEST_MODE', 'false').lower() == 'true'

# Fetch environment variables
jwt_token = 'test_jwt_token' if TEST_MODE else os.getenv('JWT_TOKEN')
wp_host = 'test_wp_host' if TEST_MODE else os.getenv('WP_HOST')

if not jwt_token or not wp_host:
    raise EnvironmentError("Missing required environment variables: JWT_TOKEN, WP_HOST")

def upload_image_to_wordpress(image_path: str) -> int:
    """Upload an image to WordPress and return its ID."""
    try:
        with open(image_path, 'rb') as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')

        headers = {
            "Authorization": f"Bearer {jwt_token}",
            'Content-Type': 'image/jpeg',
            'Content-Disposition': f'attachment; filename="{os.path.basename(image_path)}"'
        }

        response = requests.post(f"http://{wp_host}/wp-json/wp/v2/media", headers=headers, data=image_data)
        response.raise_for_status()
        image_id = response.json()['id']
        logging.info(f"Image uploaded successfully to WordPress. ID: {image_id}")
        return image_id
    except Exception as e:
        logging.error(f"Error uploading image to WordPress: {e}")
        return None

def create_wordpress_post(title: str, content: str, image_id: int) -> bool:
    """Create a WordPress post with the given title, content, and image ID."""
    try:
        headers = {
            "Authorization": f"Bearer {jwt_token}",
            'Content-Type': 'application/json'
        }

        post_data = {
            'title': title,
            'content': content,
            'status': 'publish',
            'featured_media': image_id
        }

        response = requests.post(f"http://{wp_host}/wp-json/wp/v2/posts", headers=headers, json=post_data)
        response.raise_for_status()
        post_id = response.json()['id']
        logging.info(f"Post created successfully on WordPress. ID: {post_id}")
        return True
    except Exception as e:
        logging.error(f"Error creating post on WordPress: {e}")
        return False