import os
import shutil
import sys
import urllib.request
import zipfile

DOWNLOAD_URL = "https://github.com/shotgunsoftware/python-api/archive/refs/tags/{filename}"

FILE_NAME = "v{MAJOR}.{MINOR}.{PATCH}.zip"
FOLDER_NAME = "python-api-{MAJOR}.{MINOR}.{PATCH}"

def build(source_path, build_path, install_path, targets):
    """Build/Install function.

    Args:
        source_path (str): Path to the rez package root.
        build_path (str): Path to the rez build directory.
        install_path (str): Path to the rez install directory.
        targets (str): Target run by the command, i.e. `build`, `install`...
    """
    package_major, package_minor, package_patch = os.environ.get(
        "REZ_BUILD_PROJECT_VERSION", "0.0.0"
    ).split(".")


    source_archive = FILE_NAME.format(
        MAJOR=package_major,
        MINOR=package_minor,
        PATCH=package_patch,
    )
    extracted_folder_name = FOLDER_NAME.format(
        MAJOR=package_major,
        MINOR=package_minor,
        PATCH=package_patch,
    )
    download_url = DOWNLOAD_URL.format(filename=source_archive)

    def _build():
        """Build the package locally."""
        archive_path = os.path.join(build_path, source_archive)

        if not os.path.isfile(archive_path):
            print(f"Downloading shotgun_api3 archive from: {download_url}")
            
            download_request = urllib.request.Request(
                url=download_url,
                headers={'User-Agent': 'Mozilla/5.0'},
            )

            with open(archive_path, "wb") as file:
                with urllib.request.urlopen(download_request) as request:
                    file.write(request.read())

        print("Extracting the archive.")
        with zipfile.ZipFile(archive_path) as archive_file:
            archive_file.extractall(build_path)

    def _install():
        """Install the package."""
        print("Installing the package.")
        extracted_archive_path = os.path.join(
            build_path, extracted_folder_name, "shotgun_api3"
        )
        install_directory = os.path.join(install_path, "python", "shotgun_api3")

        if os.path.isdir(install_directory):
            shutil.rmtree(install_directory)
        os.makedirs(install_directory)

        for element in os.listdir(extracted_archive_path):
            element_path = os.path.join(extracted_archive_path, element)
            shutil.move(element_path, install_directory)

    _build()

    if "install" in (targets or []):
        _install()


if __name__ == "__main__":
    build(
        source_path=os.environ["REZ_BUILD_SOURCE_PATH"],
        build_path=os.environ["REZ_BUILD_PATH"],
        install_path=os.environ["REZ_BUILD_INSTALL_PATH"],
        targets=sys.argv[1:],
    )
