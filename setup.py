from setuptools import find_packages,setup
from typing import List


def get_requirements()->List[str]:
    """
    this function return the lists of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            ## read lines 
            lines=file.readlines()
            ## for process in each line
            for line in lines:
                requirement =line.strip()
                ## ignore the empty lines and -e.
                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt is not found")

    return requirement_lst


print(get_requirements())


setup(
    name="NetworkSecurity",
    author = "professor Nitish Kumar",
    version="0.0.1",
    email="professorernitish@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements()
)