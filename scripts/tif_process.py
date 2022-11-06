import subprocess, os

from scripts.tif_env import TEMPLATE_PATH
from scripts.tif_util import git_sync, dep_repo, yaml_deps
from scripts.tif_yaml import app_yaml


def process():
    template_str = f"template_{app_yaml.template}"
    template_folder = os.path.join(TEMPLATE_PATH, template_str)
    git_sync(dep_repo(template_str), template_folder)

    yaml_deps(template_folder)
    subprocess.call(["python", template_folder])
