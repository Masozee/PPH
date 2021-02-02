from .models import Kontak, Signup
from django import forms
from .models import Kontak, downloadForm
from django.forms import ModelForm
from captcha.fields import CaptchaField


class ContactForm(ModelForm):

    class Meta:
        model = Kontak
        fields = ['nama_kntk','email_kntk', 'telp_kntk', 'org_kntk', 'pesan_kntk', ]


class DownloadForm(ModelForm):

    class Meta:
        model = downloadForm
        fields = ['nama','email','dokumen','organisasi',]
        widgets = {'dokumen': forms.HiddenInput()}


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



