from abc import ABC, abstractmethod
from models import *

class Repository(ABC):

    @abstractmethod
    def get_by_id(self, id: str):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def add(self, object):
        pass
    
    @abstractmethod
    def update(self, object):
        pass

    @abstractmethod
    def delete(self, id: str):
        pass

    @abstractmethod
    def dump_repository(self):
        pass

class PostgresRepo(Repository):

    def get_by_id(self, id):
        return super().get_by_id(id)

    def get_all(self):
        return super().get_all()
    
    def add(self, object: User):
        return super().add(object)

    def update(self, object):
        return super().update(object)
    
    def delete(self, id):
        return super().delete(id)

    def dump_repository(self):
        pass

class MongoRepo(Repository):
    def get_by_id(self, id):
        return super().get_by_id(id)

    def get_all(self):
        return super().get_all()
    
    def add(self, object: User):
        return super().add(object)

    def update(self, object):
        return super().update(object)
    
    def delete(self, id):
        return super().delete(id)

    def dump_repository(self):
        pass

class Neo4jRepo(Repository):
    def get_by_id(self, id):
        return super().get_by_id(id)

    def get_all(self):
        return super().get_all()
    
    def add(self, object: User):
        return super().add(object)

    def update(self, object):
        return super().update(object)
    
    def delete(self, id):
        return super().delete(id)
    
    def dump_repository(self):
        pass
    