from django import forms

from trouvetonchamp.models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom'
            }),
            'summary': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Résumé'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }),
            'banner': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select banner image'
            }),
            'img1': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select image'
            }),
            'img2': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select image'
            }),
            'img3': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select image'
            }),
            'users': forms.Select(attrs={
                'class': 'form-control'
            }),
            'date_pub': forms.DateTimeInput(attrs={
                'class': 'form-control'
            }),

        }
        categories = forms.ModelChoiceField(
            queryset=Category.objects.all()
        )


