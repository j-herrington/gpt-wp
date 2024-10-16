from setuptools import setup, find_packages

setup(
    name='gpt-wp',
    version='0.1.0',
    packages=find_packages(include=['gpt_wp', 'gpt_wp.*']),
    install_requires=[
        'requests~=2.31.0',
        'selenium~=4.14.0',
        'openai~=0.28.1',
        'python-dotenv~=1.0.1'
    ],
    entry_points={
        'console_scripts': [
            'gpt-wp=gpt_wp.cli:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='Generate blog content and publish to WordPress using OpenAI GPT-3.5-turbo.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jherrin/gpt-wp',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)