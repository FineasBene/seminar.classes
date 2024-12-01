from domain.candidate import Candidate
from persistency.candidate_file_repository import CandidateFileRepository
from persistency.candidate_pickle_repository import CandidatePickleRepository
from persistency.repository import Repository


class Tests:
    def run_all_tests(self):
        self.__run_all_tests_for_candidate_repository()


    def __run_all_tests_for_candidate_repository(self):
        repository = Repository()
        id_candidate = 1
        name = "Georgel"
        candidate = Candidate(id_candidate, name)
        repository.add(id_candidate, candidate)
        assert len(repository)==1
        filepath = "tests/candidates_test.bin"
        file_repository = CandidatePickleRepository(filepath)
        file_repository.add(id_candidate, candidate)
        #assert len(file_repository)==1