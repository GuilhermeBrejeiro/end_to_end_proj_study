from setuptools import find_packages, setup
from typing import List


dot_e_to_remove = "-e ."
def get_requirements(path:str)->List[str]:
    """
    This functions with return a list of requirements
    """
    requirements=[]
    with open(path) as file_requirements:
        requirements = file_requirements.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if dot_e_to_remove in requirements:
            requirements.remove(dot_e_to_remove)
    
    return requirements

setup(
    name="machinelearningproject",
    version="0.0.1",
    author="Guilherme Brejeiro",
    author_email="juanbre@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)