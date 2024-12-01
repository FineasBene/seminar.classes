import pickle

from persistency.repository import Repository


class CandidatePickleRepository(Repository):
    def __init__(self,file_path):
        super().__init__()
        self.__file_path = file_path

    def add(self,id_entity,entity):
        self.__read_all_from_file()
        Repository.add(self,id_entity,entity)
        self.__write_all_to_file()

    def update(self,id_entity,entity):
        self.__read_all_from_file()
        Repository.update(self,id_entity,entity)
        self.__write_all_to_file()

    def delete(self,id_entity):
        self.__read_all_from_file()
        Repository.delete(self,id_entity)
        self.__write_all_to_file()

    def search_by_id(self,id_entity):
        self.__read_all_from_file()
        return Repository.search_by_id(self,id_entity)

    def __len__(self):
        self.__read_all_from_file()
        return Repository.__len__(self)

    def get_all(self):
        self.__read_all_from_file()
        return Repository.get_all(self)

    def __read_all_from_file(self):
        with open(self.__file_path, 'rb') as f:
            try:
                self._data = pickle.load(f)
            except EOFError:
                return

    def __write_all_to_file(self):
        with open(self.__file_path, 'wb') as f:
            # noinspection PyTypeChecker
            pickle.dump(self._data, f)
