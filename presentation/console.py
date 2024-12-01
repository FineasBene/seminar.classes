from exceptions.errors import ValidationError, RepositoryError


class Console:

    def __init__(self,candidate_service):
        self.__candidate_service = candidate_service
        self.__commands = {
            "add_candidate":self.__ui_add_candidate,
            "show_candidates":self.__ui_show_candidates
        }

    def __ui_show_candidates(self, parameters):
        if len(parameters) != 0:
            print("invalid number of parameters!")
            return
        candidates = self.__candidate_service.get_all_candidates()
        if len(candidates) == 0:
            print("no candidates found!")
        for candidate in candidates:
            print(candidate)

    def __ui_add_candidate(self, parameters):
        if len(parameters) != 2:
            print("invalid number of parameters!")
            return

        id_candidate = int(parameters[0])
        name = parameters[1]
        self.__candidate_service.add_candidate(id_candidate,name)
        print("candidate added successfully!")

    def run(self):
        while True:
            command = input(">>>")
            command = command.strip()
            if command == "":
                continue
            command = command.lower()
            if command == "exit":
                break
            parts = command.split(" ")
            command_name = parts[0]
            parameters = parts[1:]
            if command_name in self.__commands:
                try:
                    self.__commands[command_name](parameters)
                except ValueError:
                    print("invalid numerical parameter!")
                except ValidationError as ve:
                    print(f"validation error:{ve}")
                except RepositoryError as re:
                    print(f"repository error:{re}")
            else:
                print("invalid command!")