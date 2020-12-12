from django.forms import ModelForm
from app_login.models import User,Profile

from django.contrib.auth.forms import UserCreationForm


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','password1','password2',)
