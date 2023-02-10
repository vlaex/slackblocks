from setuptools import find_packages, setup


with open("README.md", "r") as file_:
    long_description = file_.read()

production_requirements = []

setup(
    name="slackblocks",
    version="1.0.3",
    author="vlaex & Nicholas Lambourne (original author)",
    author_email="nick@ndl.im",
    description="Python wrapper for the Slack Blocks API",
    install_requires=production_requirements,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vlaex/slackblocks",
    packages=find_packages(".", exclude=["test"]),
    include_package_data=True,
    setup_requires=["pytest", "twine", "wheel"],
    classifiers=[
        "Programming Language :: Python :: 3.10",
    ]
)
