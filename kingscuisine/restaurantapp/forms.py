from django import forms

class BookingForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    date = forms.DateField()
    time = forms.TimeField()
    people = forms.IntegerField(min_value=1)
    message = forms.CharField(required=False, widget=forms.Textarea)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    