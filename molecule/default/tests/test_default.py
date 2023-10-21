"""Role testing files using testinfra."""

def test_directories(host):
    """Validate service directories exists."""
    directories = [
    ]

    for directory in directories:
        d = host.file(directory)

        assert d.exists
        assert d.is_directory

def test_files(host):
    """Validate files existing"""

    files_names = [
    ]

    for file_name in files_names:
        file = host.file(file_name)

        assert file.exists
        assert file.is_file

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
