from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class SignupForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    address = forms.CharField(widget=forms.Textarea, required=False)
    phone = forms.CharField(max_length=15, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                address=self.cleaned_data['address'],
                phone=self.cleaned_data['phone']
            )
        return user
