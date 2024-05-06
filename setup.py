# for installing the local packages in the virtual environemnt
from setuptools import find_packages, setup

setup(
    name='mcq_generator',
    version='0.0.1',
    author='Umang Rathi',
    author_email='umangrathi110@gmail.com',
    install_requires=['openai', 'langchain', 'streamlit', 'python-dotenv','PyPdf2'],
    packages=find_packages()   
    # this find_packages() is responsible for finding the local packages from you local directiory (whenever it found the __init__.py it consider this as a package)
)


# if want to install the package 
# pip install package_name

# command to install the requirements (installing package from requirement)
# pip install -r requirement.txt 

# for installing local package into your current virtual environment 
# python setup.py install 

# another method mention -e . in the requirement.txt automatically it search out the packages in your folder and execute the setup.py in the backend

