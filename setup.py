import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "wine-prediction"
AUTHOR_USER_NAME = "Suhail Ahmed Rajpar"
SRC_REPO = "src"
AUTHOR_EMAIL = "rajpar.suhail.ahmed@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for wine quality prediction",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Corrected key
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # Uncommented
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",  # Uncommented
    },
    package_dir={"": SRC_REPO},
    packages=setuptools.find_packages(where=SRC_REPO)
)
