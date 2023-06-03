"""
Pyproject to Sphinx.

(C) 2023 SiteNetSoft. All rights reserved.
Released under MIT License

PyProjectParser class.
"""

import unittest
from pathlib import Path
from unittest.mock import patch, mock_open, MagicMock
from pyproject_to_sphinx.pyproject_parser import PyProjectParser  # Replace 'pyproject_parser' with the actual module where PyProjectParser is defined


class TestPyProjectParser(unittest.TestCase):

    def setUp(self):
        self.parser = PyProjectParser()

    @patch('pyproject_parser.Path.resolve')
    @patch('pyproject_parser.Path.exists')
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

    @patch('pyproject_parser.Path.resolve')
    @patch('pyproject_parser.Path.exists')
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

    @patch('pyproject_parser.Path.resolve')
    def test_docs_path(self, mock_resolve):
        # Mock the resolve method
        mock_resolve.return_value = Path('mock_path')

        # Test getter and setter
        self.parser.docs_path = Path("mock_path")
        self.assertEqual(self.parser.docs_path, Path("mock_path"))

    @patch('pyproject_parser.toml.load')
    def test_metadata(self, mock_load):
        mock_metadata = {"version": "1.0.0"}
        mock_load.return_value = {"tool": {"poetry": mock_metadata}}

        # Test getter and setter
        self.parser.metadata = mock_metadata
        self.assertEqual(self.parser.metadata, mock_metadata)

    @patch('subprocess.run')
    def test_contributors(self, mock_run):
        # Mock the subprocess.run to return a successful Git command
        mock_run.return_value = MagicMock(returncode=0, stdout="Contributor 1\nContributor 2")

        # Test getter and setter
        self.parser.contributors = {"Contributor 1", "Contributor 2"}
        self.assertEqual(self.parser.contributors, {"Contributor 1", "Contributor 2"})

    @patch('pyproject_parser.Path.resolve')
    @patch('pyproject_parser.Path.exists')
    def test_license_file_path(self, mock_exists, mock_resolve):
        # Mock the path exists method
        mock_exists.return_value = True
        # Mock the resolve method
        mock_resolve.return_value = Path('mock_path')

        # Test getter and setter
        self.parser.license_file_path = Path("mock_path")
        self.assertEqual(self.parser.license_file_path, Path("mock_path"))

    @patch('builtins.open', new_callable=mock_open, read_data='Copyright (C) 2023 Mock')
    def test_license_file_copyright(self, mock_file):
        # Test getter and setter
        self.parser.license_file_copyright = "Copyright (C) 2023 Mock"
        self.assertEqual(self.parser.license_file_copyright, "Copyright (C) 2023 Mock")

    def test_copyright(self):
        # Test getter and setter
        self.parser.copyright = "Copyright (C) 2023 Mock"
        self.assertEqual(self.parser.copyright, "Copyright (C) 2023 Mock")

    def test_authors(self):
        # Test getter and setter
        self.parser.authors = "Author 1, Author 2"
        self.assertEqual(self.parser.authors, "Author 1, Author 2")

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
