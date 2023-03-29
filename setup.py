from setuptools import setup, find_packages
from pathlib import Path

with open(Path(__file__).absolute().parents[0] / "cmdgpt" / "VERSION") as _f:
    __version__ = _f.read().strip()
    
with open("README-en.md", "r", encoding="utf-8") as f:
    long_description = f.read()

install_requires = ["requests", "colorama"]

setup(
    name="cmdgpt",
    version=__version__,
    packages=find_packages(),
    description="Interact with the command line using natural language | 用自然语言操控命令行",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    license="MIT",
    url="https://github.com/MZhao-ouo/CMDGPT",
    author="MZhao",
    author_email="mzhao.ouo@gmail.com",
    entry_points={
        "console_scripts": [
            "cmdgpt=cmdgpt.main:main"
        ],
    },
    include_package_data=True,
)
