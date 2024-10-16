# cli.py
import argparse
from gpt_wp.main import main

def run():
    parser = argparse.ArgumentParser(description='GPT-WP: Generate and post blogs to WordPress using OpenAI GPT-3.5.')
    parser.add_argument('--title', type=str, help='The title of the blog post')
    parser.add_argument('--test-mode', action='store_true', help='Run in test mode with mock environment variables')
    args = parser.parse_args()

    # Pass the arguments to the main function
    main(title=args.title, test_mode=args.test_mode)

if __name__ == '__main__':
    run()