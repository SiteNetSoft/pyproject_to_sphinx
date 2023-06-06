"""
Pyproject to Sphinx.

(C) 2023 SiteNetSoft. All rights reserved.
Released under MIT License

PyProjectParser class.
"""

import toml
import subprocess
from pathlib import Path


class PyProjectParser:
    """
    PyProjectParser class.
    """

    def __init__(self,
                 pyproject_path: Path | None = None,
                 docs_path: Path | None = None,
                 license_path: Path | None = None):
        """
        PyProjectParser constructor.
        :param self:
        :param pyproject_path: Path to pyproject.toml file
        :param docs_path: Path to docs directory
        :param license_path: Path to license file
        """
        self._repo_path = None
        self._pyproject_path = None
        self._project_data = None
        self._docs_path = None
        self._metadata = None
        self._contributors = None
        self._license_file_path = None
        self._license_file_copyright = None
        self._copyright = None
        self._authors = None
        self._version = None
        self._release = None

        # Setters
        self._pyproject_path = pyproject_path
        self._docs_path = docs_path
        self._license_path = license_path
        self.authors = None

    @property
    def repo_path(self) -> Path:
        """
        Get repo path.
        :param self:
        :return:
        """
        return self._repo_path

    @repo_path.setter
    def repo_path(self, repo_path: Path | None = None) -> None:
        """
        Set repo path.
        :param self:
        :param repo_path: Path to Git repo
        :return:
        """
        if repo_path is None:
            # Run the Git command
            result = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True)

            # Check that the command was successful
            if result.returncode != 0:
                raise Exception("Could not find Git root directory")

            # Strip trailing newline from output and construct path
            git_root = result.stdout.splitlines()[0].strip()
            repo_path = Path(git_root).resolve()

        self._repo_path = repo_path

    @property
    def pyproject_path(self) -> Path | None:
        """
        Get pyproject path.
        :param self:
        :return:
        """
        return self._pyproject_path

    @pyproject_path.setter
    def pyproject_path(self, pyproject_path: Path | str | None = None) -> None:
        """
        Set pyproject path.
        :param self:
        :param pyproject_path: Path to pyproject.toml file
        :return:
        """
        if isinstance(pyproject_path, str):
            pyproject_path = Path(pyproject_path).resolve()

        if pyproject_path is None or pyproject_path.exists() is False:
            pyproject_path = Path(f'{self.repo_path}/pyproject.toml').resolve()
            if not pyproject_path.is_file():
                raise FileNotFoundError(f"Pyproject file not found at path: {pyproject_path}")

        self._pyproject_path = pyproject_path

    @property
    def project_data(self) -> dict:
        """
        Get project data.
        :param self:
        :return:
        """
        return self._project_data

    @project_data.setter
    def project_data(self, project_data: dict | None = None) -> None:
        """
        Load project data from pyproject.toml.
        :param self:
        :param project_data: Project data (by default it gets it from the file pyproject.toml)
        """
        if project_data is None:
            try:
                project_data = toml.load(self.pyproject_path)
            except Exception as e:
                raise Exception(f"Error reading pyproject.toml file: {str(e)}")

        self._project_data = project_data

    @property
    def docs_path(self) -> Path | None:
        """
        Get docs path.
        :param self:
        :return:
        """
        return self._docs_path

    @docs_path.setter
    def docs_path(self, docs_path: Path | None = None) -> None:
        """
        Set docs path.
        :param self:
        :param docs_path: Path to docs directory
        """
        if docs_path is None:
            docs_path = Path(f'{self.repo_path}/docs').resolve()
        self._docs_path = docs_path

    @property
    def metadata(self) -> dict:
        """
        Get metadata from pyproject.toml.
        :param self:
        :return:
        """
        return self._metadata

    @metadata.setter
    def metadata(self, data: dict | None = None) -> None:
        """
        Set metadata.
        :param self:
        :param data: Project data (by default it gets it from the file pyproject.toml)
        :return:
        """
        if data is None:
            data = self.project_data
        self._metadata = data["tool"]["poetry"]

    @property
    def contributors(self) -> list:
        """
        Get contributors from git log.
        :param self:
        :return:
        """
        return self._contributors

    @contributors.setter
    def contributors(self, contributors: list | None = None) -> None:
        """
        Set contributors from git log.
        :param self:
        :param contributors: Contributors (by default it gets it from the git log)
        """
        if contributors is None or len(contributors) == 0:
            git_command = ['git', 'log', '--pretty=format:%an', f'-- {self.docs_path}']
            result = subprocess.run(git_command, capture_output=True, text=True)
            contributors = list(result.stdout.splitlines())

        self._contributors = contributors

    @property
    def license_file_path(self) -> Path | None:
        """
        Get license file path.
        :param self:
        :return:
        """
        return self._license_file_path

    @license_file_path.setter
    def license_file_path(self, license_path: Path | None = None) -> None:
        """
        Find license file.
        :param self:
        :param license_path: Path to license file
        """
        if license_path is None:
            license_path = Path(f'{self.repo_path}/LICENSE').resolve()
            if not license_path.exists():
                license_path = Path(f'{self.repo_path}/LICENSE.txt').resolve()
                if not license_path.exists():
                    license_path = None

        self._license_file_path = license_path

    @property
    def license_file_copyright(self) -> str | None:
        """
        Get license file path.
        :param self:
        :return:
        """
        return self._license_file_copyright

    @license_file_copyright.setter
    def license_file_copyright(self, value: str | None) -> None:
        """
        Set copyright from license file.
        :param self:
        """
        license_path = self.license_file_path
        project_copyright = None
        if license_path is not None:
            project_copyright = None
            fallback_copyright = None
            with open(license_path) as f:
                for line in f:
                    if line.lstrip().startswith("Copyright"):
                        if "Free Software Foundation" not in line:
                            project_copyright = line.strip()
                            break
                        elif fallback_copyright is None:
                            fallback_copyright = line.strip()
                    elif line.lstrip().startswith("Mozilla Public License"):
                        project_copyright = line.strip()
                    elif line.lstrip().startswith("This is free and unencumbered software"):
                        project_copyright = line.strip()
                    elif line.lstrip().startswith("Creative Commons Attribution"):
                        project_copyright = line.strip()

            if project_copyright is None and fallback_copyright is not None:
                project_copyright = fallback_copyright

        if project_copyright is None:
            project_copyright = ""

        self._license_file_copyright = project_copyright

    @property
    def copyright(self) -> str | None:
        """
        Extract copy right from file.
        :param self:
        :return:
        """
        return self._copyright

    @copyright.setter
    def copyright(self, project_copyright: str | None = None) -> None:
        """
        Set copy right from license file.
        :param self:
        :param project_copyright: The project copyright information
        """
        if project_copyright is None:
            project_copyright = self.license_file_copyright
        if not project_copyright:
            project_copyright = self.metadata["license"]
        self._copyright = project_copyright

    @property
    def authors(self) -> str:
        """
        Get author from contributors in a String if it is multiple authors then it adds comma between the names.
        :param self:
        :return:
        """
        return self._authors

    @authors.setter
    def authors(self, contributors: set | list | None = None) -> None:
        """
        Set authors from contributors.
        :param contributors: Contributors
        :param self:
        """
        if contributors is None:
            self.contributors = None
            contributors = self.contributors

        authors = None
        if isinstance(contributors, set) or isinstance(contributors, list):
            authors = ', '.join(contributors)

        if authors is None:
            authors = ""

        self._authors = authors

    # - version: This is a shorter, "quick reference" version of your project,
    #   which usually omits smaller point-level details. For example, if your project's full version is '1.3.4',
    #   the version might just be '1.3'.
    # - release: This is the full version string of your project, including alpha/beta/rc tags.
    #   Continuing the previous example, the release would be '1.3.4'.
    #
    # In the pyproject.toml file, the [tool.poetry] section only has a version field,
    # which corresponds to the full version of your project, similar to the release field in Sphinx's conf.py.
    # The version in pyproject.toml typically follows the format of MAJOR.MINOR.PATCH, for example '1.3.4',
    # and can also include identifiers for pre-release and build metadata.
    #
    # For more information about Sphinx versioning see:
    # https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-version

    @property
    def version(self) -> str:
        """
        Get short version from long version.
        :param self:
        :return:
        """
        return self._version

    @version.setter
    def version(self, version: str | None = None) -> None:
        """
        Set version.
        :param self:
        :param version: The version of the project
        :return:
        """
        if version is None:
            version = self.metadata["version"]

        self._version = version
        parts = version.split('.')
        if len(parts) >= 2:
            self._version = '.'.join(parts[:2])

    @property
    def release(self) -> str:
        """
        Get release.
        :param self:
        :return:
        """
        return self._release

    @release.setter
    def release(self, release: str | None = None) -> None:
        """
        Set release.
        :param self:
        :param release: The release of the project
        :return:
        """
        if release is None:
            release = self.metadata["version"]

        self._release = release
