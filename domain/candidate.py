from domain.Deletable import Deletable


class Candidate(Deletable):
    def __init__(self, id_candidate, name):
        super().__init__()
        self.__id_candidate = id_candidate
        self.__name = name

    def get_id_candidate(self):
        return self.__id_candidate

    def get_name(self):
        return self.__name

    def __str__(self):
        return F"Candidate: {self.__id_candidate}, {self.__name}"