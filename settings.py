import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

PS_HOST = os.environ.get("PS_HOST")
PS_USER = os.environ.get("PS_USER")
PS_PASSWORD = os.environ.get("PS_PASSWORD")
PS_DATABASE = os.environ.get("PS_DATABASE")
