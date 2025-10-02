from click.testing import CliRunner
import rich_click as click
from toy_glacier_project.infrastructure.cli import accumulation_event, make_glacier, ablation_event


def test_accumulation_event():
    runner = CliRunner()
    result = runner.invoke(accumulation_event, ["100"])
    # Check that it runs successfully
    expected_exit_code = 0
    assert result.exit_code == expected_exit_code, (
        f"Expected: {expected_exit_code}, received: {result.exit_code}"
    )

    # Check that it outputs expected type (str)
    expected_type = str
    assert isinstance(result.output, expected_type), (
        f"Expected: {expected_type}, received {type(result.output)}"
    )
    click.echo(type(result))


def test_accumulation_event_amt():
    glacier = make_glacier(name="name", mass=100)
    glacier.accumulate(accum_amount=50)
    assert glacier.mass == 150


def test_ablation_event():
    runner = CliRunner()
    result = runner.invoke(ablation_event, ["10"])
    # Check that it runs successfully
    expected_exit_code = 0
    assert result.exit_code == expected_exit_code, (
        f"Expected: {expected_exit_code}, received: {result.exit_code}"
    )

    # Check that it outputs expected type (str)
    expected_type = str
    assert isinstance(result.output, expected_type), (
        f"Expected: {expected_type}, received {type(result.output)}"
    )
    click.echo(type(result))


def test_ablation_event_amt():
    glacier = make_glacier(name="name", mass=100)
    glacier.ablate(ablate_amount=50)
    assert glacier.mass == 50
