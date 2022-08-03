from setuptools import setup, find_packages
from pathlib import Path

version = Path("./{{ cookiecutter.python_package_name }}/version").read_text().strip()
package = {
    "name": "{{ cookiecutter.python_package_name }}",
    "version": version,
    "description": "{{ cookiecutter.project_short_description }}",
    "url": "https://github.com/{{ cookiecutter.github_organization_name }}/{{ cookiecutter.github_project_name }}",
    "author": "{{ cookiecutter.author_name }}",
    "author_email": "{{ cookiecutter.author_email }}",
    "license": "unlicense",
    "packages": find_packages(exclude=["dev"]),
    "install_requires": [
        "idom==0.38.1", 
        "idom-jupyter==0.7.6"
    ],
    "include_package_data": True,
    "zip_safe": False
}
setup(**package)