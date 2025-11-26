from setuptools import find_packages, setup 
from typing import List
def get_requirements():
    """
    Reads requirements.txt and returns a clean list of requirement strings.
    Skips empty lines and editable install directives like '-e .'.
    """
    requirements = []
    try:
        with open("requirements.txt", "r") as file:
            for line in file:
                req = line.strip()
                if req and req != "-e .":
                    requirements.append(req)

    except FileNotFoundError:
        print("requirements.txt file does not exist")

    return requirements
setup(
    name="NetworkSecurity",
    version= "0.0.1",
    packages=find_packages(),
    install_requires = get_requirements()
)