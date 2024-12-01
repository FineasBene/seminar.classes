class Deletable:
    def __init__(self):
        self.__deleted = False

    def delete(self):
        self.__deleted = True

    def is_deleted(self):
        return self.__deleted