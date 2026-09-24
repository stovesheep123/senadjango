from django.contrib.auth.forms import (
    AdminPasswordChangeForm,
    UserChangeForm,
    UserCreationForm,
)

from .models import CustomUser
#down this line is incorrect #
from django.contrib.auth.forms import UserCreationForm as AdminUserCreationForm  # or check the correct source name

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "nickname")

class CustomAdminUserCreationForm(AdminUserCreationForm):

    class Meta(AdminUserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "nickname")

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields =  ("username", "email", "nickname")