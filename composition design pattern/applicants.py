"""
contains classes for Visa application process.
"""
from abc import (ABCMeta,
                 abstractmethod)


class Applicant(metaclass=ABCMeta):
    """
    Interface for applicants.
    """
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.background_check = None

    def get_fullname(self) -> str:
        """
        returns applicant's full name (first name and last name).
        """
        fullname = f"{self.firstname} {self.lastname}"
        return fullname

    @property
    @abstractmethod
    def score(self) -> None:
        """
        applicant's overall score, raises NotImplementedError if
        not overwritten.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def status(self) -> None:
        """
        applicant's visa status, raises NotImplementedError if not overwritten.
        """
        raise NotImplementedError


class NormalApplicant(Applicant):
    """
    a normal applicant with no modifier or special treatment.
    """
    _pass_score = 2

    def __init__(self, firstname: str, lastname: str,
                 language_score: int, desired_skill: bool) -> None:
        super().__init__(firstname, lastname)
        self.language_score = language_score
        self.desired_skill = desired_skill

    @property
    def score(self) -> int:
        """
        calculates applicant score based on job desirability
        and language skill.
        """
        score = 0
        if self.desired_skill:
            score += 1
        if self.language_score > 4:
            score += (abs(self.language_score - 4))
        return score

    @property
    def status(self) -> str:
        """
        grants or denies visa depending on score
        compared to required pass score.
        """
        status = 'DENIED'
        if self.score >= self._pass_score:
            status = 'GRANTED'
        return status


class ThirdWorldApplicant(NormalApplicant):
    """
    applicants with a negative modifier to their visa score
    from third-world countries.
    """
    _pass_score = 3

    def __init__(self, firstname: str, lastname: str,
                 language_score: int, desired_skill: bool,
                 origin_country_mod: int) -> None:
        super().__init__(firstname, lastname, language_score, desired_skill)
        self.class_modifier = origin_country_mod

    @property
    def class_modifier(self) -> int:
        """
        sets class modifier to country of origin's modifier (non-positive).
        """
        return self._class_modifier

    @class_modifier.setter
    def class_modifier(self, origin_country_mod: int) -> None:
        """
        sets class modifier to the non-positive value of origin country's.
        Parameters
        ----------
        origin_country_mod:
            a non-positive value based on applicant's origin country.
        """
        if origin_country_mod > 0:
            raise ValueError('third-world applicants '
                             'cannot have positive modifier')
        self._class_modifier = origin_country_mod

    @property
    def score(self) -> int:
        """
        calculates applicant score based on job desirability and
        language skill.
        """
        score = self.class_modifier
        if self.desired_skill:
            score += 1
        if self.language_score > 4:
            score += (abs(self.language_score - 4))
        return score

    @property
    def status(self) -> str:
        """
        grants or denies visa depending on score compared to
        required pass score.
        """
        status = 'DENIED'
        if self.score >= self._pass_score:
            status = 'GRANTED'
        return status


class VIPApplicant(Applicant):
    """
    VIP applicants with special treatment.
    """
    def __init__(self, firstname: str, lastname: str) -> None:
        super().__init__(firstname, lastname)

    @property
    def score(self) -> str:
        """
        returns VIP instead of a number, auto-pass.
        """
        score = "VIP"
        return score

    @property
    def status(self) -> str:
        """
        automatically passed status check, visa granted.
        """
        status = 'GRANTED'
        return status
