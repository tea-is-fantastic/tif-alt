import os

from dotenv import load_dotenv

load_dotenv()

APP_PATH = os.environ.get("ROOT_PATH")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

DATA_PATH = os.path.join(APP_PATH, 'data')
TEMPLATE_PATH = os.path.join(APP_PATH, 'templates')
ACTION_PATH = os.path.join(APP_PATH, 'actions')
SCRIPT_PATH = os.path.join(APP_PATH, 'scripts')
SNIPPET_PATH = os.path.join(APP_PATH, 'snippets')
TEMP_PATH = os.path.join(APP_PATH, 'temp')
OUTPUT_PATH = os.path.join(APP_PATH, 'output')


def get_path(n):
    name = n.split("_")[0]
    if name == "action":
        return ACTION_PATH
    elif name == "template":
        return TEMPLATE_PATH
