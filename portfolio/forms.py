from django import  forms
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'placeholder': 'Телефон'}))
    message =forms.CharField(label='Текст сообщения', widget=forms.Textarea(attrs={"rows": 4,"tabindex":5,'placeholder': 'Сообщение' }))
    captcha = CaptchaField()