from dotenv import load_dotenv
from bot import Bot
from os import environ

load_dotenv()

advertised_down = environ.get('ADVERTISE_DOWN')
advertised_up = environ.get('ADVERTISE_UP')
twitter_email = environ.get('TWITTER_EMAIL')
twitter_password = environ.get('TWITTER_PASSWORD')

bot = Bot(
    advertised_down,
    advertised_up,
    twitter_email,
    twitter_password
    )

bot.get_internet_speed()


