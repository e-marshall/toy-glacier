import abc
import json

from toy_glacier_project import core

class GlacierRepo(abc.ABC):

	def __init__(self, collection:dict = None):
		if collection is None:
			collection = {}
		self.collection = collection
	
	@abc.abstractmethod
	def add(self, glacier: core.Glacier):
		pass

	@abc.abstractmethod
	def get(self, name: str) -> core.Glacier:
		pass

class memoryGlacierRepo(GlacierRepo):
	
	def add(self, glacier: core.Glacier):
		self.collection[glacier.name] = glacier
		
	def get(self, name: str) -> core.Glacier:
		if name in self.collection:
			return self.collection[name]
		else: 
			raise ValueError(f"Glacier: {name} not found in repository.")
		

class jsonGlacierRepo(GlacierRepo):

	def __init__(self, filepath: str):
		super().__init__()
		self.filepath = filepath
		# Load existing data from the JSON file if it exists
		try:
			with open(self.filepath,  encoding="utf-8", mode = 'r') as f:
				data = json.load(f)
				for name, glacier_data in data.items():
					self.collection[name] = core.Glacier(**glacier_data)
		except FileNotFoundError:
			raise ValueError(f"File: {self.filepath} not found. Cannot instantiate jsonGlacierRepo.")
			

	def add(self, glacier):
		self.collection[glacier.name] = glacier
		self._save_to_file()
	
	def get(self, name: str) -> core.Glacier:
		if name in self.collection:
			return self.collection[name]
		else: 
			raise ValueError(f"Glacier: {name} not found in repository.")
		
	def _save_to_file(self):
		data = {name: glacier.__dict__ for name, glacier in self.collection.items()}
		with open(self.filepath, 'w', encoding="utf-8") as f:
			json.dump(data, f, indent=4)