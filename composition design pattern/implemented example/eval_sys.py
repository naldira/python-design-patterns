"""
application evaluation module to determine
whether an applicant will be granted visa.
"""
from typing import List
from applicants import (VIPApplicant,
                        ThirdWorldApplicant,
                        NormalApplicant,
                        Applicant)
from intelligence import BackgroundCheck


class ApplicantEvalSystem:
    """
    announces whther applicant's visa request is granted or denied.
    """
    @staticmethod
    def eval_applicant(applicants: List[Applicant]) -> None:
        """
        given a list of applicants, announces their results one by one.
        Parameters
        ----------
        applicants: List[Applicants]:
            a list of applicants who are to be processed.
        """
        for applicant in applicants:
            print(f"results for {applicant.get_fullname()}:")
            if applicant.background_check() is None:
                print('background check was not done \n')
            elif applicant.background_check():
                print(f"applicant score: {applicant.score}, status: "
                      f"{applicant.status}\n")
            else:
                print(applicant.background_check, 'status: DENIED\n')


if __name__ == '__main__':
    mr_important = VIPApplicant('mr', 'important')
    mr_important.background_check = BackgroundCheck(0, False)
    muhammed = ThirdWorldApplicant('Muhammed', 'Ali', 5, True, -3)
    muhammed.background_check = BackgroundCheck(5, False)
    john_doe = NormalApplicant('John', 'Doe', 5, True)
    john_doe.background_check = BackgroundCheck(1, False)
    ApplicantEvalSystem.eval_applicant([john_doe, muhammed, mr_important])
