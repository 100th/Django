from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Profile

class SignupForm(UserCreationForm):
    phone_number = forms.CharField()
    address = forms.CharField()


    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)


    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        if email:
            if get_user_model().objects.filter(email=email).exists():
                raise forms.ValidationError('duplicated email')
        return email


    def save(self):
        user = super().save()
        profile = Profile.objects.create(
             user=user,
             phone_number=self.cleaned_data['phone_number'],
             address = self.cleaned_data['address'])
        return user


# class LoginForm(AuthenticationForm):
#     answer = forms.IntegerField(label='3+3=?')


    # def clean_answer(self):
    #     if self.cleaned_data.get('answer', None) != 6:
    #         raise forms.ValidationError('오답입니다.')
