import json
from toy_glacier_project.core import repo, glacier

class memoryGlacierRepo(repo.GlacierRepo):
	
	def add(self, glacier_obj: glacier.Glacier):
		self.collection[glacier_obj.name] = glacier_obj
		
	def get_by_name(self, name: str) -> glacier.Glacier:
		if name in self.collection:
			return self.collection[name]
		else: 
			raise ValueError(f"Glacier: {name} not found in repository.")
		
	def get_by_id(self, id: str) -> glacier.Glacier:
		for glacier_obj in self.collection.values():
			if str(glacier_obj.id) == id:
				return glacier_obj
		raise ValueError(f"Glacier with ID: {id} not found in repository.")
	def list_all(self) -> list[glacier.Glacier]:
		return list(self.collection.values())

class jsonGlacierRepo(repo.GlacierRepo):

	def __init__(self, filepath: str):
		super().__init__()
		self.filepath = filepath
		# Load existing data from the JSON file if it exists
		try:
			with open(self.filepath,  encoding="utf-8", mode = 'r') as f:
				data = json.load(f)
				for name, glacier_data in data.items():
					self.collection[name] = glacier.Glacier(**glacier_data)
		except FileNotFoundError as e:
			raise ValueError(f"File: {self.filepath} not found. Cannot instantiate jsonGlacierRepo.") from e
			
	def add(self, glacier_obj: glacier.Glacier):
		self.collection[glacier_obj.name] = glacier_obj
		self._persist()
	
	def get_by_name(self, name: str) -> glacier.Glacier:
		if name in self.collection:
			return self.collection[name]
		else: 
			raise ValueError(f"Glacier: {name} not found in repository.")
		
	def get_by_id(self, id: str) -> glacier.Glacier:
		for glacier_obj in self.collection.values():
			if str(glacier_obj.id) == id:
				return glacier_obj
		raise ValueError(f"Glacier with ID: {id} not found in repository.")
	
	def list_all(self) -> list[glacier.Glacier]:
		return list(self.collection.values())
	
	def _persist(self):
		data = {g.name: {"name": g.name,
				   		 "mass": g.mass} for g in self.collection.values()
						 }
		with open(self.filepath, 'w', encoding="utf-8") as f:
			json.dump(data, f, indent=4)
		