import openai
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Determine if running in test mode
TEST_MODE = os.getenv('TEST_MODE', 'false').lower() == 'true'

# Set the OpenAI API key from environment variables
openai.api_key = 'test_openai_api_key' if TEST_MODE else os.getenv('OPENAI_API_KEY')
if not openai.api_key:
    raise EnvironmentError("Missing OpenAI API key in environment variables.")

def generate_response(prompt: str) -> str:
    """Generate a response from OpenAI based on the given prompt."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are an AI that generates content."},
                      {"role": "user", "content": prompt}],
            max_tokens=500,
            n=1,
            temperature=0.8,
        )
        message = response.choices[0].message['content'].strip()
        logging.info(f"Generated response for prompt '{prompt}' successfully.")
        return message
    except Exception as e:
        logging.error(f"Error generating response: {e}")
        return None

def generate_blog_content(title: str) -> str:
    """Generate blog content based on a given title."""
    return generate_response(f"Write a blog post about {title}.")