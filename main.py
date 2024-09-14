import os

from bot import client
from dotenv import load_dotenv

load_dotenv()
client.run(os.getenv('TOKEN'))