from setuptools import find_packages,setup
from typing import List

with open("README.md","r", encoding="utf-8") as file_obj:
    long_description = file_obj.read()

__version__ = "0.0.0"

REPO_NAME = "Chicken_Disease_Classifier"
AUTHOR_USER_NAME = "GauravPahwa2021"
SRC_REPO = "CNN_Classifier"
AUTHOR_EMAIL = "2020uce1603@mnit.ac.in"

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for NLP app",
    long_description = long_description,
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {"Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
    package_dir = {"": "src"},
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)