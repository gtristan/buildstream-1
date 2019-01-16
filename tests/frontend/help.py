import pytest
from buildstream.plugintestutils.runcli import cli


def assert_help(cli_output):
    expected_start = "Usage: "
    if not cli_output.startswith(expected_start):
        raise AssertionError("Help output expected to begin with '{}',"
                             .format(expected_start) +
                             " output was: {}"
                             .format(cli_output))


def test_help_main(cli):
    result = cli.run(args=['--help'])
    result.assert_success()
    assert_help(result.output)


@pytest.mark.parametrize("command", [
    ('artifact'),
    ('build'),
    ('checkout'),
    ('shell'),
    ('show'),
    ('source'),
    ('workspace')
])
def test_help(cli, command):
    result = cli.run(args=[command, '--help'])
    result.assert_success()
    assert_help(result.output)
