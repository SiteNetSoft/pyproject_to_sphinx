"""
Pyproject to Sphinx.

(C) 2023 SiteNetSoft. All rights reserved.
Released under MIT License

PyProjectParser class.
"""

import pytest
from pyproject_to_sphinx.pyproject_parser import PyProjectParser


def test_get_short_version():
    parser = PyProjectParser()

    assert parser.get_short_version("1.2.3") == "1.2"
    assert parser.get_short_version("0.1") == "0.1"
    assert parser.get_short_version("3") == "3"


@pytest.mark.skip(reason="Need to mock file and git operations")
def test_get_contributors():
    pass


@pytest.mark.skip(reason="Need to mock file operations")
def test_extract_copyright():
    pass


@pytest.mark.skip(reason="Need to mock toml operations")
def test_get_metadata():
    pass
