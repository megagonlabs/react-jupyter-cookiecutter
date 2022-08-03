# react-jupyter-cookiecutter

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for creating a custom Jupyter widget project using [idom-jupyter](https://github.com/idom-team/idom-jupyter). This template is adapted from [widget-cookiecutter](https://github.com/jupyter-widgets/widget-cookiecutter).

## Usage

Install [cookiecutter](https://github.com/cookiecutter/cookiecutter):

    $ pip install cookiecutter

After installing cookiecutter, use the react-jupyter-cookiecutter to:

    # Create project from the git repo template
    $ cookiecutter https://github.com/rit-git/react-jupyter-cookiecutter.git

    # OR create project from a local template
    $ cookiecutter react-jupyter-cookiecutter/

As react-jupyter-cookiecutter runs, you will be asked for basic information about your custom Jupyter widget project. You will be prompted for the following information:

- `author_name`: your name or the name of your organization,
- `author_email`: your project's contact email,
- `github_project_name`: name of your custom Jupyter widget's GitHub repository,
- `github_organization_name`: name of your custom Jupyter widget's GitHub user or organization,
- `python_package_name`: name of the Python "backend" package used in your custom widget.
- `npm_package_name`: name for the npm "frontend" package holding the JavaScript implementation used in your custom widget.
- `project_short_description` : a short description for your project that will be used for both the "backend" and "frontend" packages.

After this, you will have a directory containing files used for creating a custom Jupyter widget. You will now be able to easily package and distribute your custom Jupyter widget.

## Local Dev Installation

- Under **{{ cookiecutter.github_project_name }}** folder
  - Run `pip install -e .`
- Under **{{ cookiecutter.github_project_name }}/js** folder
  - Run `npm install`
  - Run `npm run watch`: this automatically rebundles JS components for you; then restart the notebook to test
- Periodically delete JS files created by {{ cookiecutter.github_project_name }} under `/Users/[username]/Library/Application Support/idom-jupyter/`
  - run `whoami` to get username from the terminal (macOS)
