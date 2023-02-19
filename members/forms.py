from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    DB_CHOICES = (("Scopus", "Scopus"), ("PubMed", "PubMed"),
                  ("Dimensions", "Dimensions"), ("Web of Science", "Web of Science")
                  )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-input--full"}))
    first_name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={"class": "form-input--full"}))
    last_name = forms.CharField(
        max_length=80, widget=forms.TextInput(attrs={"class": "form-input--full"}))
    database_revue = forms.ChoiceField(
        choices=DB_CHOICES, label="Base de Revues", initial="", required=True, widget=forms.Select(attrs={"class": "form-input--full"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', 'database_revue')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs['class'] = "form-input--full"
        self.fields["password1"].widget.attrs['class'] = "form-input--full"
        self.fields["password2"].widget.attrs['class'] = "form-input--full"
