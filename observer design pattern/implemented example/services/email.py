"""
emulates sending email, only for example's demonstration.
"""


class EMail:
    """
    stand-in for the real Email API.
    """
    @staticmethod
    def send_email(email: str, message: str) -> None:
        """
        sends an email to the given email with given message.
        Parameters
        ----------
        email: str:
            email of the recipient.
        message:
            body of the email.
        """
        print(f"to: {email}\n{message}")
