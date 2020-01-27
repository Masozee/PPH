from .models import Kontak, Signup
from django import forms
from .models import Kontak, downloadForm
from django.forms import ModelForm
from .multiforms import MultiFormsView
from captcha.fields import ReCaptchaField

class ReCAPTCHAForm(forms.Form):
    captcha = ReCaptchaField()


class MultipleForm(forms.Form):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())

class ContactForm(ModelForm):
    
    class Meta:
        model = Kontak
        fields = ['nama_kntk','email_kntk', 'telp_kntk', 'org_kntk', 'pesan_kntk']


class DownloadForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = downloadForm
        fields = ['nama','email','organisasi','dokumen']


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


#class VisitorForm(forms.ModelForm):


