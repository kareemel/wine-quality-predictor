import click
from wqp import __version__
from wqp.workflow import model_training_workflow

@click.version_option(__version__)
@click.group()
def wqp():
    pass

@wqp.group()
def jobs():
    pass

@jobs.command()
@click.option('--data-path')
def train(data_path):
    model_training_workflow(data_path=data_path)
