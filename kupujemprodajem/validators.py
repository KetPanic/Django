from django.core.exceptions import ValidationError

class CustomPasswordValidator():

    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        if not any(char.isdigit() for char in password):
            raise ValidationError('Password must contain at least one digit.')
        if not any(char.isalpha() for char in password):
            raise ValidationError('Password must contain at least one letter.')
        if not any(char in special_characters for char in password):
            raise ValidationError('Password must contain at least one special character.')

    def get_help_text(self):
        return ""