import click
from window_tamer.config import Config

@click.group()
@click.option('--config-file', help='Path to the configuration file', required=True)
@click.pass_context
def cli(ctx, config_file):
    if ctx.obj is None:
        ctx.obj={}
    ctx.obj['config'] = Config(config_file)


@cli.command()
@click.pass_context
def start(ctx):
    print(ctx.obj['config'])    

if __name__ == '__main__':
   cli()