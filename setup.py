from setuptools import find_packages, setup

# Read the long description from the README file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Package metadata
__version__ = "0.0.0"
REPO_NAME = "wine-prediction"
AUTHOR_USER_NAME = "Suhail Ahmed Rajpar"
AUTHOR_EMAIL = "rajpar.suhail.ahmed@gmail.com"

setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for wine quality prediction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    packages=find_packages(),  # Automatically find packages in the current directory
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify the required Python version
)
