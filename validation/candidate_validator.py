from exceptions.errors import ValidationError


class CandidateValidator:

    def validate(self, candidate):
        errors = ""
        if candidate.get_id_candidate()<0:
            errors += "invalid id!\n"
        if candidate.get_name() == "":
            errors += "invalid name!\n"
        if len(errors)>0:
            raise ValidationError(errors)