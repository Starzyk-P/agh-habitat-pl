"""
Earth Engine authentication module.
"""

import os

# Google Cloud project registered for Earth Engine. Override with the
# EE_PROJECT environment variable or the `project` argument.
DEFAULT_PROJECT = "agh-ml-2025"


def authenticate():
    """
    Authenticate with Google Earth Engine.
    """
    try:
        import ee
    except ImportError:
        raise ImportError("earthengine-api is required for authentication")
    ee.Authenticate()


def initialize(project=None):
    """
    Initialize Earth Engine API.

    Args:
        project (str, optional): Google Cloud project ID registered for
            Earth Engine. Defaults to the EE_PROJECT environment variable,
            then to DEFAULT_PROJECT.
    """
    try:
        import ee
    except ImportError:
        raise ImportError("earthengine-api is required for initialization")
    project = project or os.environ.get("EE_PROJECT") or DEFAULT_PROJECT
    ee.Initialize(project=project)
