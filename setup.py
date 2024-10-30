import setuptools

with open("README.md",'r',encoding='utf-8')as f:
    lond_description = f.read()

AUTHOR_USER_NAME = "amal-creator"
REPO_NAME = "climatingchangemodelling"
AUTHOR_EMAIL = "amalragpop@gmail.com"
SRC_REPO = "climatingchangemodelling"
__version__ = "0.0.0"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A  interface for climate change modelling",
    long_description=lond_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)