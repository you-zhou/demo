from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)


User = get_user_model()


class LoginForm(forms.Form):
    """Login form for user authentication."""
    username = forms.CharField(
        label='Username',
        max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': "Username",
                   'autofocus': ""}))
    password = forms.CharField(
        label='Password',
        max_length=50,
        widget=forms.PasswordInput(
            attrs={'placeholder': "Password"}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password.")
            if not user:
                raise forms.ValidationError("This user does not exist.")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active.")
        return super(LoginForm, self).clean(*args, **kwargs)


class RegisterForm(forms.ModelForm):
    """User registration."""
    username = forms.CharField(
        label='Username',
        max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': "Username",
                   'autofocus': ""}))
    first_name = forms.CharField(
        required = False,
        label='First Name',
        max_length=30,
        widget=forms.TextInput(
            attrs={'placeholder': 'First Name (Optional)'})
    )
    last_name = forms.CharField(
        required = False,
        label='Last Name',
        max_length=30,
        widget=forms.TextInput(
            attrs={'placeholder': 'Last Name (Optional)'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(
            attrs={'placeholder': "Email"}))
    password = forms.CharField(
        label='Password',
        max_length=50,
        widget=forms.PasswordInput(
            attrs={'placeholder': "Password"}))
    password2 = forms.CharField(
        label='Confirm Password',
        max_length=50,
        widget=forms.PasswordInput(
            attrs={'placeholder': "Confirm Password"}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
        ]

    def clean_email2(self):
        """
        This needs to follow the order of the fields in Meta data.
        This error message will be on the field. 
        As oppose overwriting clean() will only put the error on top.
        """
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email has already been registered.")
        return email

    def clean_password2(self):
        """
        This needs to follow the order of the fields in Meta data.
        This error message will be on the field. 
        As oppose overwriting clean() will only put the error on top.
        """
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Password must match")
        return password


class CrispyForm(forms.Form):
    """Test django-crispy-forms"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
