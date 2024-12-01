from business.candidate_service import CandidateService
from persistency.candidate_file_repository import CandidateFileRepository
from persistency.candidate_pickle_repository import CandidatePickleRepository
from persistency.repository import Repository
from presentation.console import Console
from validation.candidate_validator import CandidateValidator


class App:

    def start_app(self):
        with open("properties.settings","r") as f:
            line = f.readline()

            parts = line.split("=")
            repo_type = parts[1]
            line = f.readline()
            parts = line.split("=")
            repo_path = parts[1]
            if repo_type == "binary":
                repo = CandidatePickleRepository(repo_path)
            elif repo_type == "text":
                repo = CandidateFileRepository(repo_path)
            else:
                repo = Repository()
            validator_candidate = CandidateValidator()
            candidates_service = CandidateService(repo, validator_candidate)
            ui = Console(candidates_service)
            ui.run()