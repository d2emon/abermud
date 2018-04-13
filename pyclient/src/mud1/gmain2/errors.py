class LoginError(Exception):
    """
    Login errors
    """
    def __init__(self):
        self.message = "No!"

    def __str__(self):
        return self.message
