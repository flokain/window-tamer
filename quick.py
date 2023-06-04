import asyncio
import yaml
import subprocess
import click


class Config:
    def __init__(self, config_file):
        self.load_config(config_file)

    def load_config(self, config_file):
        with open(config_file, 'r') as file:
            config_data = yaml.safe_load(file)
            self.commands = config_data


class ShellExecutor:
    async def execute_command(self, command):
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        return process.returncode, stdout.decode(), stderr.decode()


@click.group()
@click.option('--config-file', help='Path to the configuration file', required=True)
@click.pass_context
def cli(ctx, config_file):
    ctx.obj['config'] = Config(config_file)


@cli.command()
@click.pass_context
def start(ctx):
    print(ctx.obj['config'])    

if __name__ == '__main__':
   cli(obj={})