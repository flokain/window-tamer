import pytest
from click.testing import CliRunner
from window_tamer.cli import cli


@pytest.fixture
def runner():
    return CliRunner()

@pytest.fixture
def example_config_file(tmpdir):

    config_data = """
    - name: function1
    - name: function2
    """
    config_file = tmpdir.join('example_config.yaml')
    config_file.write(config_data)
    return str(config_file)


def test_function1(runner, example_config_file):
    result = runner.invoke(cli, ['--config-file', example_config_file,"start"])
    assert result.exit_code == 0
    assert 'Executing function1' in result.output


if __name__ == '__main__':
    pytest.main(['-v','--show-capture=stderr'])