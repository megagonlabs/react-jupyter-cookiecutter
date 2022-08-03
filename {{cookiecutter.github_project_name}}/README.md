# {{ cookiecutter.github_project_name }}
## To use in Python Notebook
```python
# To use library modules
from {{ cookiecutter.python_package_name }} import Widget
Widget().show()
```
## For development
- Under **{{ cookiecutter.github_project_name }}** folder
  - Run `pip install -e .`
- Under **{{ cookiecutter.github_project_name }}/js** folder
  - Run `npm install`
  - Run `npm run watch`: this automatically rebundles JS components for you; then restart the notebook to test
- Periodically delete JS files created by {{ cookiecutter.github_project_name }} under `/Users/[username]/Library/Application Support/idom-jupyter/`
  - run `whoami` to get username from the terminal (macOS)
## Disclosures
![last-updated](https://img.shields.io/badge/Last%20Updated-Jul%2011%20,2022-lightgrey)
|Library|License|
|:-|:-|
|[idom](https://pypi.org/project/idom/)|[MIT](https://choosealicense.com/licenses/mit/)|
|[idom-jupyter](https://pypi.org/project/idom-jupyter/)|:warning: Missing|
|[@babel/core](https://www.npmjs.com/package/@babel/core)|[MIT](https://choosealicense.com/licenses/mit/)|
|[@babel/preset-env](https://www.npmjs.com/package/@babel/preset-env)|[MIT](https://choosealicense.com/licenses/mit/)|
|[@babel/preset-react](https://www.npmjs.com/package/@babel/preset-react)|[MIT](https://choosealicense.com/licenses/mit/)|
|[@rollup/plugin-babel](https://www.npmjs.com/package/@rollup/plugin-babel)|[MIT](https://choosealicense.com/licenses/mit/)|
|[@rollup/plugin-commonjs](https://www.npmjs.com/package/@rollup/plugin-commonjs)|[MIT](https://choosealicense.com/licenses/mit/)|
|[@rollup/plugin-json](https://www.npmjs.com/package/@rollup/plugin-json)|[MIT](https://choosealicense.com/licenses/mit/)|
|[@rollup/plugin-node-resolve](https://www.npmjs.com/package/@rollup/plugin-node-resolve)|[MIT](https://choosealicense.com/licenses/mit/)|
|[babel-plugin-transform-css-import-to-string](https://www.npmjs.com/package/babel-plugin-transform-css-import-to-string)|[MIT](https://choosealicense.com/licenses/mit/)|
|[npm-watch](https://www.npmjs.com/package/npm-watch)|[MIT](https://choosealicense.com/licenses/mit/)|
|[rollup](https://www.npmjs.com/package/rollup)|[MIT](https://choosealicense.com/licenses/mit/)|
|[rollup-plugin-inject-process-env](https://www.npmjs.com/package/rollup-plugin-inject-process-env)|[MIT](https://choosealicense.com/licenses/mit/)|
|[rollup-plugin-terser](https://www.npmjs.com/package/rollup-plugin-terser)|[MIT](https://choosealicense.com/licenses/mit/)|
|[normalize.css](https://www.npmjs.com/package/normalize.css)|[MIT](https://choosealicense.com/licenses/mit/)|
|[react](https://www.npmjs.com/package/react)|[MIT](https://choosealicense.com/licenses/mit/)|
|[react-dom](https://www.npmjs.com/package/react-dom)|[MIT](https://choosealicense.com/licenses/mit/)|
