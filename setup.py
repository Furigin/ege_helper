from setuptools import setup, find_packages

setup(
    name="ege-help",
    version="1.1",
    packages=find_packages(),
    python_requires=">=3.8",
    entry_points={"console_scripts": ["ege-help=ege_help.__main__:main"]},
)
