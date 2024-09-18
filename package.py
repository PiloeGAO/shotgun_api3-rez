name = "shotgun_api3"

version = "3.6.2"

authors = ["Autodesk", "Leo Depoix (@piloegao)"]

description = """
    A shotgun_api3 rez package using the pre-build version.
    """

requires = ["python"]

uuid = "org.autodesk.shotgun_api3"

build_command = "python {root}/build.py {install}"


def commands():
    env.PYTHONPATH.append("{root}/python")
