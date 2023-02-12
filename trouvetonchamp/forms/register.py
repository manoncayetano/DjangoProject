from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=100)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Mot de passe", min_length=5, max_length=100, widget=forms.PasswordInput())

    def clean(self):
        pass

    def clean_username(self):
        if self.cleaned_data['username'] == '':
            self.add_error('username', 'Le prénom ne peut pas être vide')
        return self.cleaned_data['username']



