from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm, PasswordChangeForm

UNO = 'UNO.png'
DOS = 'DOS.png'
TRES = 'TRES.png'

AVATAR_CHOICES = (
    (UNO, 'UNO'),
    (DOS, 'DOS'),
    (TRES, 'TRES'),
)

AVATAR_CHOICES_ADMIN = (
    ("APU.png", 'APU'),
    ("SANJAY.png", 'SANJAY'),
)

class CustomRadioSelect(forms.RadioSelect):
    option_template_name = 'accounts/radio_option_custom.html'

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    avatar_img = forms.ChoiceField(label='Avatar', widget=CustomRadioSelect(), choices=AVATAR_CHOICES)
    
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2', 'avatar_img')

class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    avatar_img = forms.ChoiceField(required=False, label='Avatar', widget=CustomRadioSelect(), choices = AVATAR_CHOICES)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'avatar_img')

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        
        if self.instance.is_staff:
            self.fields["avatar_img"].choices = AVATAR_CHOICES_ADMIN
        else:
            self.fields["avatar_img"].choices = AVATAR_CHOICES

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
   
    class Meta:
        model = User
        fields = ('username', 'password')

    
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label=("Contraseña Actual"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=("Nueva Contraseña"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label=("Repetir Nueva Contraseña"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')