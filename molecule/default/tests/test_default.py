import datetime as dt

"""Role testing files using testinfra."""

def test_updated(host):
    """Validate files updated"""

    files_names = [
        "/etc/ssl/certs/ca-certificates.crt",
    ]

    for file_name in files_names:
        file = host.file(file_name)

        now = dt.datetime.today()

        assert file.exists
        assert (now - file.mtime).total_seconds() < 60


def test_directories(host):
    """Validate service directories exists."""
    directories = [
        "/etc/ssl/local/",
    ]

    for directory in directories:
        d = host.file(directory)

        assert d.exists
        assert d.is_directory

def test_files(host):
    """Validate files existing"""

    files_names = [
        "/etc/ssl/local/certificate.pem",
        "/etc/ssl/local/private_key.pem",
        "/etc/ssl/local/chain.pem",
        "/etc/ssl/local/fullchain.pem",
    ]

    for file_name in files_names:
        file = host.file(file_name)

        assert file.exists
        assert file.is_file

def test_bad_concatenation(host):
    """Validate files are not concatenated badly"""

    # This would happen if there is no new line in the SSL files

    files_names = [
        "/etc/ssl/local/fullchain.pem",
    ]

    for file_name in files_names:
        file = host.file(file_name)

        # print(file.content_string)

        assert not file.contains("----------")
        assert not file.contains("---------- ----------")

# TODO: Does not seem to work on molecule.
# def test_service(host):
#     """Validate service is valid."""
#     service = host.service("template")
#
#     assert service.is_valid

def test_commands(host):
    """Validate commands exists."""
    commands = [
    ]

    for command in commands:
        c = host.find_command(command)

# def test_executables(host):
#     """Validate service executables exists."""
#     executables = [
#     ]
#
#     for executable in executables:
#         e = host.file(executable)
#
#         assert e.exists
#         assert e.is_file
#         assert e.is_executable
