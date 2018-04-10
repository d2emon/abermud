class ArgsError(Exception):
    """
    Args parsing errors
    """
    def __init__(self, message):
        self.message = message


class LoginError(Exception):
    """
    Login errors
    """
    def __init__(self):
        self.message = "No!"

    def __str__(self):
        return self.message
