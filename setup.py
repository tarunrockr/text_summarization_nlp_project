import setuptools

with open( 'README.md', "r", encoding="utf-8") as file:
    long_description = file.read()

__version__ = "0.0.0"

REPO_NAME = "text_summarization_nlp_project"
AUTHOR_USER_NAME = "abc"
SRC_REPO = "text_summarizer"
AUTHOR_EMAIL = "abc@gamil.com"

setuptools.setup(
    name = SRC_REPO,
    reversion = __version__,
    author    = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description  = "CNN Application",
    long_description = long_description,
    long_description_content = "text/markdown",
    url = "",
    project_urls={
        "Bug Tracker": "",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
