import click
from .service import Service
from .errors import NotFoundError

_service = Service()


@click.group()
def cli():
    pass


@cli.command("list")
def list_items():
    items = _service.get_all()
    if not items:
        click.echo("No items found.")
    else:
        for item in items:
            click.echo(f"{item.id}: {item.name}")


@cli.command("get")
@click.argument("item_id", type=int)
def get_item(item_id: int):
    try:
        item = _service.get_by_id(item_id)
        click.echo(f"{item.id}: {item.name}")
    except NotFoundError as e:
        click.echo(str(e))


@cli.command()
def reset():
    _service.reset()
    click.echo("Database reset to empty state.")


if __name__ == "__main__":
    cli()
