from exceptions.errors import RepositoryError


class Repository:
    def __init__(self):
        self._data = {}

    def add(self,id_entity,entity):
        if id_entity in self._data:
            raise RepositoryError("existing id!")
        self._data[id_entity] = entity

    def search_by_id(self,id_entity):
        if id_entity not in self._data:
            raise RepositoryError("id not found!")
        return self._data[id_entity]

    def update(self,id_entity,entity):
        if id_entity not in self._data:
            raise RepositoryError("id not found!")
        self._data[id_entity] = entity

    def delete(self,id_entity):
        if id_entity not in self._data:
            raise RepositoryError("id not found!")
        self._data[id_entity].delete()

    def get_all(self):
        return list(self._data.values())

    def __len__(self):
        return len(self._data)