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
        :param pyproject_path:
        :param docs_path:
        :param license_path:
        """
        self.repo_path = None
        self.pyproject_path = None
        self.project_data = None
        self.docs_path = None
        self.contributors = None
        self.license_file_copyright = None
        self.copyright = None
        self.authors = None
        self.version = None
        self.release = None
        self.metadata = None
        self.license_path = None

        # Setters
        self.set_pyproject_path(pyproject_path)
        self.set_project_data()
        self.set_metadata()
        self.set_docs_path(docs_path)
        self.set_license_path(license_path)

    def set_git_repo_path(self, repo_path: Path | None = None) -> None:
        """
        Set repo path.
        :param self:
        :param repo_path:
        :return:
        """
        if repo_path is None:
            # Run the Git command
            result = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True)

            # Check that the command was successful
            if result.returncode != 0:
                raise Exception("Could not find Git root directory")

            # Strip trailing newline from output and construct path
            git_root = result.stdout.splitlines()
            repo_path = Path(git_root)

        self.repo_path = repo_path

    def get_git_repo_path(self) -> Path:
        """
        Get repo path.
        :param self:
        :return:
        """
        if self.repo_path is None:
            self.set_git_repo_path()
        return self.repo_path

    def set_pyproject_path(self, pyproject_path: Path | str | None = None) -> None:
        """
        Set pyproject path.
        :param self:
        :param pyproject_path:
        :return:
        """
        if pyproject_path is str:
            pyproject_path = Path(pyproject_path)

        if pyproject_path.exists() is False:
            pyproject_path = None

        if pyproject_path is None or pyproject_path.exists() is False:
            pyproject_path = Path(f'{self.get_git_repo_path()}/pyproject.toml')

        self.pyproject_path = pyproject_path

    def get_pyproject_path(self) -> Path | None:
        """
        Get pyproject path.
        :param self:
        :return:
        """
        if self.pyproject_path is None:
            self.set_pyproject_path()
        return self.pyproject_path

    def set_project_data(self, project_data: dict | None = None) -> None:
        """
        Load project data from pyproject.toml.
        :param self:
        :param project_data:
        """
        if project_data is None:
            project_data = toml.load(self.get_pyproject_path())
        self.project_data = project_data

    def get_project_data(self) -> dict:
        """
        Get project data.
        :param self:
        :return:
        """
        if self.project_data is None:
            self.set_project_data()
        return self.project_data

    def set_metadata(self, data: dict | None = None) -> None:
        """
        Set metadata.
        :param self:
        :param data:
        :return:
        """
        if data is None:
            data = self.get_project_data()
        self.metadata = data["tool"]["poetry"]

    def get_metadata(self) -> dict:
        """
        Get metadata from pyproject.toml.
        :param self:
        :return:
        """
        if self.metadata is None:
            self.set_metadata()
        return self.metadata

    def set_docs_path(self, docs_path: Path | None = None) -> None:
        """
        Set docs path.
        :param self:
        :param docs_path:
        """
        if docs_path is None:
            docs_path = Path(f'{self.get_git_repo_path()}/docs')
        self.docs_path = docs_path

    def get_docs_path(self) -> Path | None:
        """
        Get docs path.
        :param self:
        :return:
        """
        if self.docs_path is None:
            self.set_docs_path()
        return self.docs_path

    def set_contributors(self) -> None:
        """
        Set contributors from git log.
        :param self:
        """
        git_command = ['git', 'log', '--pretty=format:%an', f'-- {self.get_docs_path()}']
        result = subprocess.run(git_command, capture_output=True, text=True)
        self.contributors = set(result.stdout.splitlines())

    def get_contributors(self) -> set:
        """
        Get contributors from git log.
        :param self:
        :return:
        """
        if self.contributors is None:
            self.set_contributors()
        return self.contributors

    def set_license_file_path(self, license_path: Path | None = None) -> None:
        """
        Find license file.
        :param self:
        :param license_path:
        """
        if license_path is None:
            license_path = Path(f'{self.get_git_repo_path()}/LICENSE')
            if not license_path.exists():
                license_path = Path(f'{self.get_git_repo_path()}/LICENSE.txt')
                if not license_path.exists():
                    license_path = None

        self.license_path = license_path

    def get_license_file_path(self) -> Path | None:
        """
        Get license file path.
        :param self:
        :return:
        """
        if self.license_path is None:
            self.set_license_file_path()
        return self.license_path

    def set_license_file_copyright(self) -> None:
        """
        Set copyright from license file.
        :param self:
        """
        license_path = self.get_license_file_path()
        project_copyright = None
        if license_path is not None:
            with open(license_path) as f:
                for line in f:
                    if "Copyright" in line:
                        project_copyright = line.strip()
                        break

        if project_copyright is None:
            project_copyright = ""

        self.license_file_copyright = project_copyright

    def get_license_file_copyright(self) -> str | None:
        """
        Get license file path.
        :param self:
        :return:
        """
        if self.license_file_copyright is None:
            self.set_license_file_copyright()
        return self.license_file_copyright

    def set_copyright(self, project_copyright: str | None = None) -> None:
        """
        Set copy right from license file.
        :param self:
        :param project_copyright:
        """
        if project_copyright is None:
            project_copyright = self.get_license_file_copyright()
        if project_copyright is None or project_copyright == "":
            project_copyright = self.get_metadata()["license"]
        self.copyright = project_copyright

    def get_copyright(self) -> str | None:
        """
        Extract copy right from file.
        :param self:
        :return:
        """
        if self.copyright is None:
            self.set_copyright()
        return self.copyright

    def set_authors(self) -> None:
        """
        Set authors from contributors.
        :param self:
        """
        self.authors = ', '.join(self.get_contributors())

    def get_authors(self) -> str:
        """
        Get author from contributors in a String if it is multiple authors then it adds comma between the names.
        :param self:
        :return:
        """
        if self.authors is None:
            self.set_authors()
        return self.authors

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

    def set_version(self, version: str | None = None) -> None:
        """
        Set version.
        :param self:
        :param version:
        :return:
        """
        if version is None:
            version = self.get_metadata()["version"]

        self.version = version
        parts = version.split('.')
        if len(parts) >= 2:
            self.version = '.'.join(parts[:2])

    def get_version(self) -> str:
        """
        Get short version from long version.
        :param self:
        :return:
        """
        if self.version is None:
            self.set_version()
        return self.version

    def set_release(self, release: str | None = None) -> None:
        """
        Set release.
        :param self:
        :param release:
        :return:
        """
        if release is None:
            release = self.get_metadata()["version"]

        self.release = release

    def get_release(self) -> str:
        """
        Get release.
        :param self:
        :return:
        """
        if self.release is None:
            self.set_release()
        return self.release
