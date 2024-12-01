from domain.candidate import Candidate


class CandidateService:

    def __init__(self,candidate_repository,candidate_validator):
        self.__candidate_repository = candidate_repository
        self.__candidate_validator = candidate_validator

    def add_candidate(self,id_candidate,name):
        candidate = Candidate(id_candidate,name)
        self.__candidate_validator.validate(candidate)
        self.__candidate_repository.add(id_candidate,candidate)

    def get_all_candidates(self):
        return self.__candidate_repository.get_all()