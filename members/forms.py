from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    DB_CHOICES = (("Scopus", "Scopus"), ("PubMed", "PubMed"),
                  ("Dimensions", "Dimensions"), ("Web of Science", "Web of Science")
                  )
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=80)
    database_revue = forms.ChoiceField(
        choices=DB_CHOICES, label="Base de Revues", initial="", required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', 'database_revue')
