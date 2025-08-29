from toy_glacier import cli


def test_create_glacier():
    glacier = cli.make_glacier(name="name", glacier_mass=100)
    assert glacier.name == "name"
    assert glacier.mass == 100


def test_accumulation_event():
    glacier = cli.make_glacier(name="name", glacier_mass=100)
    glacier.accumulate(accum_amount=50)
    assert glacier.mass == 150


def test_ablation_event():
    glacier = cli.make_glacier(name="name", glacier_mass=100)
    glacier.ablate(ablate_amount=50)
    assert glacier.mass == 50
