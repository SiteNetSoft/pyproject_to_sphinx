"""
Pyproject to Sphinx.

(C) 2023 SiteNetSoft. All rights reserved.
Released under MIT License

PyProjectParser class.
"""

import unittest
from pathlib import Path
from unittest.mock import patch, mock_open, MagicMock
from pyproject_to_sphinx.pyproject_parser import PyProjectParser


class TestPyProjectParser(unittest.TestCase):

    def setUp(self):
        self.parser = PyProjectParser()

    @patch('pyproject_to_sphinx.pyproject_parser.Path.resolve')
    @patch('pyproject_to_sphinx.pyproject_parser.Path.exists')
    @patch('subprocess.run')
    def test_repo_path(self, mock_run, mock_exists, mock_resolve):
        # Mock the subprocess.run to return a successful Git command
        mock_run.return_value = MagicMock(returncode=0, stdout="mock_path")
        # Mock the path exists method
        mock_exists.return_value = True
        # Mock the resolve method
        mock_resolve.return_value = Path('mock_path')

        # Test getter and setter
        self.parser.repo_path = Path("mock_path")
        self.assertEqual(self.parser.repo_path, Path("mock_path"))

    @patch('pyproject_to_sphinx.pyproject_parser.Path.resolve')
    @patch('pyproject_to_sphinx.pyproject_parser.Path.exists')
    def test_pyproject_path(self, mock_exists, mock_resolve):
        # Mock the path exists method
        mock_exists.return_value = True
        # Mock the resolve method
        mock_resolve.return_value = Path('mock_path')

        # Test getter and setter
        self.parser.pyproject_path = Path("mock_path")
        self.assertEqual(self.parser.pyproject_path, Path("mock_path"))

    def test_project_data(self):
        mock_project_data = {"tool": {"poetry": {"version": "1.0.0"}}}

        # Test getter and setter
        self.parser.project_data = mock_project_data
        self.assertEqual(self.parser.project_data, mock_project_data)

    @patch('pyproject_to_sphinx.pyproject_parser.Path.resolve')
    def test_docs_path(self, mock_resolve):
        # Mock the resolve method
        mock_resolve.return_value = Path('mock_path')

        # Test getter and setter
        self.parser.docs_path = Path("mock_path")
        self.assertEqual(self.parser.docs_path, Path("mock_path"))

    @patch('pyproject_to_sphinx.pyproject_parser.toml.load')
    def test_metadata(self, mock_load):
        mock_metadata = {
            "tool": {
                "poetry": {
                    "version": "1.0.0"
                }
            }
        }
        mock_load.return_value = mock_metadata

        # Test getter and setter
        self.parser.metadata = mock_metadata
        self.assertEqual(self.parser.metadata, {"version": "1.0.0"})

    @patch('subprocess.run')
    def test_contributors(self, mock_run):
        # Mock the subprocess.run to return a successful Git command
        mock_run.return_value = MagicMock(returncode=0, stdout="Contributor 1\nContributor 2")

        # Test getter and setter
        self.parser.contributors = {"Contributor 1", "Contributor 2"}
        self.assertEqual(self.parser.contributors, {"Contributor 1", "Contributor 2"})

    @patch('pyproject_to_sphinx.pyproject_parser.Path.resolve')
    @patch('pyproject_to_sphinx.pyproject_parser.Path.exists')
    def test_license_file_path(self, mock_exists, mock_resolve):
        # Mock the path exists method
        mock_exists.return_value = True
        # Mock the resolve method
        mock_resolve.return_value = Path('mock_path')

        # Test getter and setter
        self.parser.license_file_path = Path("mock_path")
        self.assertEqual(self.parser.license_file_path, Path("mock_path"))

    def test_license_ApacheLicense2_file_copyright(self):
        # Test getter and setter
        self.parser.license_file_path = Path("./tests/fixtures/ApacheLicense2.0/LICENSE").resolve()
        self.parser.license_file_copyright = None
        self.assertEqual(self.parser.license_file_copyright, "Copyright 2023 SiteNetSoft")

    def test_license_BoostSoftwareLicense1_file_copyright(self):
        # Test getter and setter
        self.parser.license_file_path = Path("./tests/fixtures/BoostSoftwareLicense1.0/LICENSE").resolve()
        self.parser.license_file_copyright = None
        self.assertEqual(self.parser.license_file_copyright, "")

    def test_license_BSD2ClauseSimplifiedLicense_file_copyright(self):
        # Test getter and setter
        self.parser.license_file_path = Path("./tests/fixtures/BSD2ClauseSimplifiedLicense/LICENSE").resolve()
        self.parser.license_file_copyright = None
        self.assertEqual(self.parser.license_file_copyright, "Copyright (c) 2023, SiteNetSoft")

    def test_license_BSD3ClauseClearLicense_file_copyright(self):
        # Test getter and setter
        self.parser.license_file_path = Path("./tests/fixtures/BSD3ClauseClearLicense/LICENSE").resolve()
        self.parser.license_file_copyright = None
        self.assertEqual(self.parser.license_file_copyright, "Copyright (c) 2023, SiteNetSoft")

    def test_license_BSD3ClauseNeworRevisedLicense_file_copyright(self):
        # Test getter and setter
        self.parser.license_file_path = Path("./tests/fixtures/BSD3ClauseNeworRevisedLicense/LICENSE").resolve()
        self.parser.license_file_copyright = None
        self.assertEqual(self.parser.license_file_copyright, "Copyright (c) 2023, SiteNetSoft")

    def test_license_BSD4ClauseOriginalorOldLicense_file_copyright(self):
        # Test getter and setter
        self.parser.license_file_path = Path("./tests/fixtures/BSD4ClauseOriginalorOldLicense/LICENSE").resolve()
        self.parser.license_file_copyright = None
        self.assertEqual(self.parser.license_file_copyright, "Copyright (c) 2023, SiteNetSoft")

    def test_license_BSDZeroClauseLicense_file_copyright(self):
        # Test getter and setter
        self.parser.license_file_path = Path("./tests/fixtures/BSDZeroClauseLicense/LICENSE").resolve()
        self.parser.license_file_copyright = None
        self.assertEqual(self.parser.license_file_copyright, "Copyright (c) 2023, SiteNetSoft")

    def test_license_CreativeCommonsAttribution4_0International_file_copyright(self):
        # Test getter and setter
        self.parser.license_file_path = Path("./tests/fixtures/CreativeCommonsAttribution4.0International/LICENSE")\
            .resolve()
        self.parser.license_file_copyright = None
        self.assertEqual(self.parser.license_file_copyright,
                         "Creative Commons Attribution 4.0 International Public License")

    def test_license_FallBackToTxt_file_copyright(self):
        # Test getter and setter
        self.parser.license_file_path = Path("./tests/fixtures/FallBackToTxt/LICENSE") \
            .resolve()
        self.parser.license_file_copyright = None
        self.assertEqual(self.parser.license_file_copyright, "Copyright (c) 2023 SiteNetSoft (txt)")

    def test_license_GNUAfferoGeneralPublicLicensev3_0_file_copyright(self):
        # Test getter and setter
        self.parser.license_file_path = Path("./tests/fixtures/GNUAfferoGeneralPublicLicensev3.0/LICENSE").resolve()
        self.parser.license_file_copyright = None
        self.assertEqual(self.parser.license_file_copyright, "Copyright (C) 2023 SiteNetSoft")

    def test_license_GNUGeneralPublicLicensev3_0_file_copyright(self):
        # Test getter and setter
        self.parser.license_file_path = Path("./tests/fixtures/GNUGeneralPublicLicensev3.0/LICENSE").resolve()
        self.parser.license_file_copyright = None
        self.assertEqual(self.parser.license_file_copyright, "Copyright (C) 2023  SiteNetSoft")

    def test_license_GNULesserGeneralPublicLicensev3_0_file_copyright(self):
        # Test getter and setter
        self.parser.license_file_path = Path("./tests/fixtures/GNULesserGeneralPublicLicensev3.0/LICENSE").resolve()
        self.parser.license_file_copyright = None
        self.assertEqual(self.parser.license_file_copyright,
                         "Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>")

    def test_license_MIT_file_copyright(self):
        # Test getter and setter
        self.parser.license_file_path = Path("./tests/fixtures/MIT/LICENSE").resolve()
        self.parser.license_file_copyright = None
        self.assertEqual(self.parser.license_file_copyright, "Copyright (c) 2023 SiteNetSoft (not txt)")

    def test_license_MozillaPublicLicense2_0_file_copyright(self):
        # Test getter and setter
        self.parser.license_file_path = Path("./tests/fixtures/MozillaPublicLicense2.0/LICENSE").resolve()
        self.parser.license_file_copyright = None
        self.assertEqual(self.parser.license_file_copyright, "Mozilla Public License Version 2.0")

    def test_license_TheUnlicense_file_copyright(self):
        # Test getter and setter
        self.parser.license_file_path = Path("./tests/fixtures/TheUnlicense/LICENSE").resolve()
        self.parser.license_file_copyright = None
        self.assertEqual(self.parser.license_file_copyright,
                         "This is free and unencumbered software released into the public domain.")

    def test_copyright(self):
        # Test getter and setter
        self.parser.copyright = "Copyright (C) 2023 Mock"
        self.assertEqual(self.parser.copyright, "Copyright (C) 2023 Mock")

    def test_authors_list_setter(self):
        # Test getter and setter
        self.parser.authors = ["Author 1", "Author 2"]
        self.assertEqual(self.parser.authors, "Author 1, Author 2")

    @patch('subprocess.run')
    def test_authors_None_setter(self, mock_run):
        # Mock the subprocess.run to return a successful Git command
        mock_run.return_value = MagicMock(returncode=0, stdout="Contributor 1\nContributor 2")

        # Test getter and setter
        self.parser.contributors = ["Contributor 1", "Contributor 2"]
        # Retest authors setter so that it uses the contributors property
        self.parser.authors = None

        self.assertEqual(self.parser.authors, "Contributor 1, Contributor 2")

    @patch('subprocess.run')
    def test_authors_subprocess_failure(self, mock_run):
        mock_run.return_value = MagicMock(returncode=1)  # Simulate a subprocess failure
        self.assertEqual(self.parser.authors, "")

    def test_version(self):
        # Test getter and setter
        self.parser.version = "1.0.0"
        self.assertEqual(self.parser.version, "1.0")

    def test_release(self):
        # Test getter and setter
        self.parser.release = "1.0.0"
        self.assertEqual(self.parser.release, "1.0.0")


if __name__ == '__main__':
    unittest.main()
