from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name="PyGaza",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    scripts=["pylogin.py"],

    install_requires=required,

    package_data={
        #SIf any package contains *.txt or *.rst files, include them:
        "": ["*.txt", "*.rst"],
        # And include any *.msg files found in the "hello" package, too:
        "hello": ["*.msg"],
    },

    # metadata to display on PyPI
    author="Aboud",
    author_email="aboud@gmail.com",
    description="This is an Login Package",
    keywords="Test platform login",
    url="http://example.com/HelloWorld/",   # project home page, if any
    project_urls={
        "Bug Tracker": "https://bugs.example.com/PyGaza/",
        "Documentation": "https://docs.example.com/PyGaza/",
        "Source Code": "https://code.example.com/PyGaza/",
    },
    classifiers=[
        "License :: MIT :: Python Software License"


    entry_points="""
        [console_scripts]
        test_me=PyGaza.scripts.test:test_me
        # yourscript=yourpackage.scripts.yourscript:cli
    """,

    ]


    # could also include long_description, download_url, etc.
)
