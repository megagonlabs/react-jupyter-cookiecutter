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
## Disclosure

Embedded in, or bundled with, this product are open source software (OSS) components, datasets and other third party components identified below. The license terms respectively governing the datasets and third-party components continue to govern those portions, and you agree to those license terms, which, when applicable, specifically limit any distribution. You may receive a copy of, distribute and/or modify any open source code for the OSS component under the terms of their respective licenses. In the event of conflicts between Megagon Labs, Inc. Recruit Co., Ltd., license conditions and the Open Source Software license conditions, the Open Source Software conditions shall prevail with respect to the Open Source Software portions of the software. You agree not to, and are not permitted to, distribute actual datasets used with the OSS components listed below. You agree and are limited to distribute only links to datasets from known sources by listing them in the datasets overview table below. You are permitted to distribute derived datasets of data sets from known sources by including links to original dataset source in the datasets overview table below. You agree that any right to modify datasets originating from parties other than Megagon Labs, Inc. are governed by the respective third party’s license conditions. All OSS components and datasets are distributed WITHOUT ANY WARRANTY, without even implied warranty such as for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE, and without any liability to or claim against any Megagon Labs, Inc. entity other than as explicitly documented in this README document. You agree to cease using any part of the provided materials if you do not agree with the terms or the lack of any warranty herein. While Megagon Labs, Inc., makes commercially reasonable efforts to ensure that citations in this document are complete and accurate, errors may occur. If you see any error or omission, please help us improve this document by [creating an issue ticket](https://github.com/megagonlabs/react-jupyter-cookiecutter/issues/new).

All dataset and code used within the product are listed below (including their copyright holders and the license conditions). For Datasets having different portions released under different licenses, please refer to the included source link specified for each of the respective datasets for identifications of dataset files released under the identified licenses.
