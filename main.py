from dotenv import load_dotenv
from os import environ
import selenium


load_dotenv()
twitter_email = environ.get('TWITTER_EMAIL')
twitter_password = environ.get('TWITTER_PASSWORD')

print(twitter_email)

