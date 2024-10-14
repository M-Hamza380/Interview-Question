from setuptools import setup, find_packages
from typing import List

Hypen_E_Dot = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    Args:
        file_path (str): Receive the requirements libraries

    Returns:
        List[str]: This function will return the list of requirements
    """
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if Hypen_E_Dot in requirements:
            requirements.remove(Hypen_E_Dot)
    
    return requirements

setup(
    name = "interview-question-creator",
    version = "0.0.1",
    author = "Muhammad Hamza Anjum",
    author_email = "hamza.anjum380@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt"),
)
