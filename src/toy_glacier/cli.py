import click

from toy_glacier.core import make_glacier


@click.group()
def main():
    """
    Entry point for the toy_glacier CLI application.

    This function serves as the main Click group for all glacier-related commands.
    """    
    pass

@main.command("accumulation-event")
@click.argument(
    "amount",
    type=int,
)
@click.option(
    "--name", default="defaultName", help="Name of the glacier created in this call."
)
@click.option(
    "--glacier-volume", default=100, help="Initial volume of glacier created in this call."
)
def accumulation_event(
    amount: int,
    name: str,
    glacier_volume: int,
):
    """
    Create a glacier and apply an accumulation event.

    This command creates a glacier with the specified name and initial volume,
    then increases its volume by the specified accumulation amount.

    Parameters
    ----------
    amount : int
        The volume to add to the glacier (m3).
    name : str
        The name assigned to the glacier.
    glacier_volume : int
        The initial volume of the glacier (m3).
    """    
    glacier = make_glacier(name=name, glacier_volume=glacier_volume)
    create_text = click.wrap_text(
        f"Glacier created with name: {name}, initial volume: {glacier_volume} (m3)."
    )
    click.echo(create_text)

    glacier.accumulate(accum_amount=amount)
    accum_text = click.wrap_text(
        f"Accumulation event: Volume is now {glacier.volume} (m3)."
    )
    click.echo(accum_text)


@main.command("ablation-event")
@click.argument("amount", type=int)
@click.option(
    "--name", default="defaultName", help="Name of glacier created in this call."
)
@click.option(
    "--glacier-volume",
    default=100,
    help="Initial volume of a glacier created in this call.",
)
def ablation_event(amount: int, name: str, glacier_volume: int):
    """
    Create a glacier and apply an ablation event.

    This command creates a glacier with the specified name and initial volume,
    then decreases its volume by the specified ablation amount.

    Parameters
    ----------
    amount : int
        The volume to remove from the glacier (m3).
    name : str
        The name assigned to the glacier.
    glacier_volume : int
        The initial volume of the glacier (m3).
    """    
    glacier = make_glacier(name=name, volume=glacier_volume)
    create_text = click.wrap_text(
        f"Glacier created with name: {name}, initial volume: {glacier_volume} (m3)."
    )
    click.echo(create_text)

    glacier.ablate(ablate_amount=amount)
    ablate_text = click.wrap_text(f"Ablation event: Volume is now {glacier.volume} (m3)")
    click.echo(ablate_text)
