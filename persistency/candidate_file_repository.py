from domain.candidate import Candidate
from persistency.repository import Repository


class CandidateFileRepository(Repository):

    def __init__(self,file_path):
        super().__init__()
        self.__file_path = file_path

    def add(self,id_entity,entity):
        self.__read_all_from_file()
        Repository.add(self,id_entity,entity)
        self.__append_to_file(entity)

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
        with open(self.__file_path, 'r') as f:
            self._data.clear()
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    id_candidate = int(parts[0])
                    name = parts[1]
                    candidate = Candidate(id_candidate, name)
                    self._data[id_candidate] = candidate

    def __write_all_to_file(self):
        with open(self.__file_path, 'w') as f:
            for candidate in self._data.values():
                f.write(f"{candidate.get_id_candidate()},{candidate.get_name()}\n")

    def __append_to_file(self, entity):
        with open(self.__file_path, 'a') as f:
            f.write(f"{entity.get_id_candidate()},{entity.get_name()}\n")

