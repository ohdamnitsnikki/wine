from django import forms
from django_countries.fields import CountryField


class ContactForm(forms.Form):
    product_name = forms.CharField(label='Product Name')
    country = CountryField().formfield()
    meat_or_fish = forms.ChoiceField(choices=(('meat', 'Red Meat'), ('fish', 'White Fish')), label='Meat or Fish')
    description = forms.CharField(widget=forms.Textarea, label='Description')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ContactForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['username'] = forms.CharField(initial=user.username, disabled=True, label='Username')
            self.fields['email'] = forms.CharField(initial=user.email, disabled=True, label='Email')
