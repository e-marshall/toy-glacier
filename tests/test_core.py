from toy_glacier import core
import pytest


def test_make_glacier():
    glacier = core.make_glacier(name="testName", volume=500)
    assert glacier.name == "testName"
    assert glacier.volume == 500


def test_accumulate():
    glacier = core.Glacier(name="test1", volume=100)
    glacier.accumulate(20)

    assert glacier.volume == 120


def test_ablate():
    glacier = core.Glacier(name="test", volume=100)
    glacier.ablate(50)

    assert glacier.volume == 50


def test_ablate_not_possible():
    with pytest.raises(ValueError):
        glacier = core.Glacier(name="test", volume=50)
        glacier.ablate(75)


def test_can_ablate():
    glacier = core.Glacier(name="..", volume=10)
    assert not glacier.can_ablate(20)
    assert glacier.can_ablate(5)
