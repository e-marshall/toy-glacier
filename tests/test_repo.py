from toy_glacier_project.core import repo, glacier
from toy_glacier_project.infrastructure import repo_implementations as repo_impl
import pytest
import json
from pathlib import Path

from toy_glacier_project.core import glacier


#Create objs we'll use in testing w/ fixtures
@pytest.fixture
def glacier_obj():
    """Fixture for a test glacier."""
    return glacier.make_glacier("test glacier", 1000)

@pytest.fixture
def memory_repo_obj(glacier_obj):
    """Fixture for a test glacier repository with one glacier."""
    repo_instance = repo_impl.memoryGlacierRepo()
    repo_instance.add(glacier_obj)
    return repo_instance

@pytest.fixture
def json_repo(tmp_path = './data'):
    """Fixture for a test glacier repository with one glacier."""
    filepath = Path(tmp_path, "sample_glacier_db.json")
    repo_instance = repo_impl.jsonGlacierRepo(str(filepath))
    return repo_instance

def test_glacier_obj_type(glacier_obj):
    assert isinstance(glacier_obj, glacier.Glacier)
    
def test_can_get_glacier_by_id(memory_repo_obj, glacier_obj):
    retrieved_glacier = memory_repo_obj.get_by_id(str(glacier_obj.id))
    assert retrieved_glacier.name == glacier_obj.name
    assert retrieved_glacier.mass == glacier_obj.mass
    assert retrieved_glacier.id == glacier_obj.id

def test_get_by_id_raises_error_for_nonexistent_id(memory_repo_obj):
    non_existent_id = "123e4567-e89b-12d3-a456-426614174000"
    with pytest.raises(ValueError, 
                       match = f"Glacier with ID: {non_existent_id} not found in repository."):
        memory_repo_obj.get_by_id(non_existent_id)  

def test_can_get_glacier_by_name(memory_repo_obj, glacier_obj):
    retrieved_glacier = memory_repo_obj.get_by_name(glacier_obj.name)
    assert retrieved_glacier.name == glacier_obj.name
    assert retrieved_glacier.mass == glacier_obj.mass
    assert retrieved_glacier.id == glacier_obj.id

def test_get_by_name_raises_error_for_nonexistent_name(memory_repo_obj):
    name = "nonexistant glacier"
    with pytest.raises(ValueError, 
                       match = f"Glacier: {name} not found in repository."):
        memory_repo_obj.get_by_name(name)

# Memory repo tests
def test_can_instantiate_memory_repo():

    repo_instance = repo_impl.memoryGlacierRepo()
    assert isinstance(repo_instance, repo_impl.memoryGlacierRepo)

def test_repository_can_save_a_glacier(glacier_obj):
    
    #Make a repo
    glac_repo = repo_impl.memoryGlacierRepo()
    # Add glacier to the repo
    glac_repo.add(glacier_obj)
    assert isinstance(glacier_obj, glacier.Glacier)
    # Retrieve glacier from the repo
    returned_glacier = glac_repo.get_by_name(glacier_obj.name)
    # Check that the returned glacier is the same as the one we added
    assert returned_glacier.id == glacier_obj.id
    assert returned_glacier.name == glacier_obj.name
    assert returned_glacier.mass == glacier_obj.mass

def test_repository_retrieves_glacier(memory_repo_obj):
    # Retrieve glacier from the repo
    returned_glacier = memory_repo_obj.get_by_name('test glacier')
    # Check that the returned glacier is the same as the one we added
    assert returned_glacier.name == 'test glacier'
    assert returned_glacier.mass == 1000

def test_repository_cant_retrieve_nonexistent_glacier(memory_repo_obj):
    name = "nonexistant glacier"
    with pytest.raises(ValueError, 
                       match = f"Glacier: {name} not found in repository."):
        memory_repo_obj.get_by_name(name)

#Json repo tests
def test_can_instantiate_json_repo():

    here = Path(__file__).parent
    filepath = Path(here, 'data','sample_glacier_db.json')
    repo_instance = repo_impl.jsonGlacierRepo(str(filepath))
    assert isinstance(repo_instance, repo_impl.jsonGlacierRepo)
    assert repo_instance.filepath == str(filepath)

def test_cant_instantiate_nonexistent_json_repo():
    cwd = Path.cwd()
    print('cwd:', cwd)
    here = Path('.')
    print('here:', here)
    here2 = Path(__file__).parent

    filepath = Path(here2, 'data','nonexistent_glacier_db.json')
    
    with pytest.raises(ValueError,
                       match = f"File: {str(filepath)} not found. Cannot instantiate jsonGlacierRepo."):
        repo_impl.jsonGlacierRepo(str(filepath))

