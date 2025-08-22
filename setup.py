from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="StudyBuddy",
    version="0.1",
    author="Ajith",
    packages=find_packages(),
    install_requires = requirements,
)