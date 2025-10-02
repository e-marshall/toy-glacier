from toy_glacier_project.core import glacier
import pytest

#Create objs we'll use in testing w/ fixtures
@pytest.fixture
def glacier_obj():
    """Fixture for a test glacier."""
    return glacier.make_glacier("test glacier", 1000)

def test_make_glacier():
    glacier_obj = glacier.make_glacier(name="testName", mass=500)
    assert glacier_obj.name == "testName"
    assert glacier_obj.mass == 500

def test_glacier_has_name_mass_id_version(glacier_obj):
    assert glacier_obj.name == "test glacier"
    assert glacier_obj.mass == 1000
    assert hasattr(glacier_obj, 'id')
    assert hasattr(glacier_obj, 'version')
    assert glacier_obj.version == 0
    assert isinstance(glacier_obj.id, type(glacier.uuid4()))

def test_accumulate():
    glacier_obj = glacier.Glacier(name="test1", mass=100)
    glacier_obj.accumulate(20)

    assert glacier_obj.mass == 120

def test_ablate():
    glacier_obj = glacier.Glacier(name="test", mass=100)
    glacier_obj.ablate(50)

    assert glacier_obj.mass == 50


def test_ablate_not_possible():
    with pytest.raises(ValueError):
        glacier_obj = glacier.Glacier(name="test", mass=50)
        glacier_obj.ablate(75)


def test_can_ablate():
    glacier_obj = glacier.Glacier(name="..", mass=10)
    assert not glacier_obj.can_ablate(20)
    assert glacier_obj.can_ablate(5)

def test_glacier_version_updates_on_accumulation(glacier_obj):
    initial_version = glacier_obj.version
    glacier_obj.accumulate(500)
    assert glacier_obj.mass == 1500
    assert glacier_obj.version == initial_version + 1

def test_glacier_version_updates_on_ablation(glacier_obj):
    initial_version = glacier_obj.version
    glacier_obj.ablate(300)
    assert glacier_obj.mass == 700
    assert glacier_obj.version == initial_version + 1
