from toy_glacier import domain


def test_accumulate():
    glacier = domain.Glacier(name="test1", mass=100)
    glacier.accumulate(20)

    assert glacier.mass == 120


def test_ablate():
    glacier = domain.Glacier(name="test", mass=100)
    glacier.ablate(50)

    assert glacier.mass == 50
