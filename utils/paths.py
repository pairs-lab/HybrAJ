"""Repository paths, resolved from this file so scripts work from any working directory."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, 'assets')


def asset(*parts):
    """Absolute path of a file under assets/, e.g. asset('ur5e', 'ur5e.urdf')."""
    return os.path.join(ASSETS, *parts)
