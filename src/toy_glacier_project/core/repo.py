import abc
import json

from toy_glacier_project.core import glacier

class GlacierRepo(abc.ABC):

	def __init__(self, collection:dict = None):
		if collection is None:
			collection = {}
		self.collection = collection
	
	@abc.abstractmethod
	def add(self, glacier_obj: glacier.Glacier):
		pass

	@abc.abstractmethod
	def get_by_name(self, name: str) -> glacier.Glacier:
		pass 

	@abc.abstractmethod
	def get_by_id(self, id: str) -> glacier.Glacier:
		pass

	@abc.abstractmethod
	def list_all(self) -> list[glacier.Glacier]:
		pass
