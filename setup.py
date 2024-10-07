from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This Function Will return The List of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements] # Because in the req.txt la next line la packakes name irukku so atha replace pannanum

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
name = 'ML-DEPLOY',
version = '0.0.1',
author = 'Abu',
author_mail = 'mdabucse@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)
