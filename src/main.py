# src/main.py
import sys
import logging
from content_generator import generate_blog_content
from image_downloader import download_image_from_unsplash
from wordpress_uploader import upload_image_to_wordpress, create_wordpress_post
from utils import get_environment_variables, load_env_variables

# Initialize logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main(title=None, test_mode=False):
    """Main function to get environment variables, generate content, download an image, upload the image, and create a post."""
    load_env_variables(test_mode)

    try:
        env_vars = get_environment_variables(test_mode)
    except EnvironmentError as e:
        logging.error(f"Error getting environment variables: {e}")
        sys.exit(1)

    if not title:
        title = env_vars.get('TITLE')

    dl_path = env_vars.get('DL_PATH')
    img_search_term = env_vars.get('IMG')

    if not title or not dl_path or not img_search_term:
        logging.error("Missing one or more required environment variables: TITLE, DL_PATH, IMG")
        sys.exit(1)

    content = generate_blog_content(title)
    if not content:
        logging.error("Error generating content.")
        sys.exit(1)

    image_path = download_image_from_unsplash(img_search_term, dl_path)
    if not image_path:
        logging.error("Error downloading image.")
        sys.exit(1)

    upload_id = upload_image_to_wordpress(image_path)
    if not upload_id:
        logging.error("Error uploading image.")
        sys.exit(1)

    post_created = create_wordpress_post(title, content, upload_id)
    if not post_created:
        logging.error("Error creating WordPress post.")
        sys.exit(1)


# Execute the main function if the script is run directly
if __name__ == '__main__':
    main()