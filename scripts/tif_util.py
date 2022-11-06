import os.path
import pwd
import re
from lxml import etree

import requests
import yaml
from git import Repo

from scripts.tif_env import *


def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def git_sync(git_url, repo_dir):
    try:
        Repo.clone_from(git_url, repo_dir)
    except:
        repo = Repo(repo_dir)
        repo.remotes.origin.pull("main")


def yaml_dict(stream):
    return yaml.safe_load(stream)


def open_yaml(yaml_loc):
    with open(yaml_loc, "r") as stream:
        return yaml_dict(stream)


def open_raw(yaml_loc):
    with open(yaml_loc, "r") as stream:
        return stream.read()


def nested_get(dic, keys):
    for key in keys:
        dic = dic[key]
    return dic


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


def yaml_extract(name, path=DATA_PATH):
    return Struct(**open_yaml(os.path.join(path, name)))


def dep_repo(temp_str):
    return f"https://github.com/tea-is-fantastic/{temp_str}"


def yaml_deps(path):
    config = os.path.join(path, 'config.yaml')
    if not os.path.exists(config):
        return
    inp = open_yaml(config)
    for x in inp["dependencies"]:
        pth = os.path.join(get_path(x), x)
        git_sync(dep_repo(x), pth)
        yaml_deps(pth)


def demote():
    pw_record = pwd.getpwnam('a')
    homedir = pw_record.pw_dir
    user_uid = pw_record.pw_uid
    user_gid = pw_record.pw_gid

    def result():
        os.setgid(user_gid)
        os.setuid(user_uid)

    return result


def download(image_url, path):
    img_data = requests.get(image_url).content
    with open(path, 'wb') as handler:
        handler.write(img_data)


def reg_test(path, reg, rep, flags=re.X, already=None, callback=None):
    with open(path, 'r') as f:
        content = f.read()
        if already is not None:
            if bool(re.search(already, content)):
                return
        content_new = re.sub(reg, rep, content, flags=flags)
        if callback is not None:
            content_new = callback(content_new)
        return content_new


def reg_rep(path, reg, rep, flags=re.X, already=None, callback=None):
    content_new = reg_test(path, reg, rep, flags, already, callback)
    if not content_new:
        return
    with open(path, 'w') as g:
        g.write(content_new)
    return content_new


def xmlpretty(s):
    x = etree.fromstring(s)
    return etree.tostring(x, pretty_print=True, encoding="unicode")
