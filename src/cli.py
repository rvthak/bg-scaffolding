import click
from .service import Service

_service = Service()


@click.group()
def cli():
    pass


_DATE_TYPE = click.DateTime(formats=["%d-%m-%Y"])


@cli.command("availability-check")
@click.argument("apartment_id", type=int)
@click.argument("start_date", type=_DATE_TYPE)
@click.argument("end_date", type=_DATE_TYPE)
def availability_check(apartment_id: int, start_date, end_date):
    is_available, apartments = _service.check_apartment_availability(apartment_id, start_date.date(), end_date.date())

    if is_available:
        click.echo("The apartment you asked for is available in the requested period!")
    else:
        click.echo("The apartment you asked for is available in the requested period!")

    if apartments:
        click.echo("Available apartments:")
        for ap in apartments:
            click.echo(f" - {ap.id, ap.address, ap.description}")
    else:
        click.echo("No apartments are available during the requested period")


if __name__ == "__main__":
    cli()
