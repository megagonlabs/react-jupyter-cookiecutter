from pathlib import Path
import idom_jupyter

PRODUCTION = True
BUNDLE_JS = "bundle.min.js"
try:
    from .dev.development import get_epoch
    PRODUCTION = False
    BUNDLE_JS = "bundle.js"
except ImportError or ModuleNotFoundError:
    pass
_VERSION_PATH = Path(__file__).parent / 'version'
VERSION = Path(_VERSION_PATH).read_text().strip()
print("{{ cookiecutter.python_package_name }}: " + VERSION)
MODULE_NAME = f"labeler_ui@{VERSION}"
BUNDLE_PATH = Path(__file__).parent / BUNDLE_JS
FALLBACK = "Failed to display {{ cookiecutter.python_package_name }} widget."
from .Widget import Widget