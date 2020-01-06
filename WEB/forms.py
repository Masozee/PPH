from .models import Kontak, Signup
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Kontak, downloadForm
from django.forms import ModelForm


class ContactForm(ModelForm):
    
    class Meta:
        model = Kontak
        fields = ['nama_kntk','email_kntk', 'telp_kntk', 'org_kntk', 'pesan_kntk']


class DownloadForm(ModelForm):
    
    class Meta:
        model = downloadForm
        fields = ['nama','email','dokumen']


class EmailSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type": "email",
        "name": "email",
        "id": "email",
        "placeholder": "Type your email address",
    }), label="")

    class Meta:
        model = Signup
        fields = ('email', )