from toy_glacier_project import repo, core
import pytest
import json
from pathlib import Path


#Create objs we'll use in testing w/ fixtures
@pytest.fixture
def glacier():
    """Fixture for a test glacier."""
    return core.make_glacier("test glacier", 1000)

@pytest.fixture
def memory_repo(glacier):
    """Fixture for a test glacier repository with one glacier."""
    repo_instance = repo.memoryGlacierRepo()
    repo_instance.add(glacier)
    return repo_instance

@pytest.fixture
def json_repo(tmp_path = './data'):
    """Fixture for a test glacier repository with one glacier."""
    filepath = Path(tmp_path, "sample_glacier_db.json")
    repo_instance = repo.jsonGlacierRepo(str(filepath))
    return repo_instance

def test_can_instantiate_memory_repo():

    repo_instance = repo.memoryGlacierRepo()
    assert isinstance(repo_instance, repo.memoryGlacierRepo)

def test_can_instantiate_json_repo():

    here = Path(__file__).parent
    filepath = Path(here, 'data','sample_glacier_db.json')
    repo_instance = repo.jsonGlacierRepo(str(filepath))
    assert isinstance(repo_instance, repo.jsonGlacierRepo)
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
        repo.jsonGlacierRepo(str(filepath))

def test_repository_can_save_a_glacier(glacier):
    
    #Make a repo
    glac_repo = repo.memoryGlacierRepo()
    # Add glacier to the repo
    glac_repo.add(glacier)
    # Retrieve glacier from the repo
    returned_glacier = glac_repo.get(glacier.name)
    # Check that the returned glacier is the same as the one we added
    assert returned_glacier.name == glacier.name
    assert returned_glacier.mass == glacier.mass

def test_repository_retrieves_glacier(memory_repo):
    # Retrieve glacier from the repo
    returned_glacier = memory_repo.get('test glacier')
    # Check that the returned glacier is the same as the one we added
    assert returned_glacier.name == 'test glacier'
    assert returned_glacier.mass == 1000

def test_repository_cant_retrieve_nonexistent_glacier(memory_repo):
    name = "nonexistant glacier"
    with pytest.raises(ValueError, 
                       match = f"Glacier: {name} not found in repository."):
        memory_repo.get(name)

