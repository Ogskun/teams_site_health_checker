import os
from dotenv import load_dotenv

load_dotenv()

# Channel name which is connected to your app
TEAMS_WEBHOOK_URL = os.environ.get('TEAMS_WEBHOOK_URL')

# List of site urls
APPS = [
    # {'url': '', 'name': ''},  # Format
]

try:
    from localsettings import *
except:
    pass