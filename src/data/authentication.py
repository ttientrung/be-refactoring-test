from django.contrib.auth.models import User

class UserIdAuthBackend:
    """
    Custom authentication backend.

    Allows users to log in using their user_id address.
    """

    def authenticate(self, request, username=None, password=None):
        """
        Overrides the authenticate method to allow users to log in using their user_id address.
        """
        try:
            user = User.objects.get(pk=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        Overrides the get_user method to allow users to log in using their user_id address.
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None