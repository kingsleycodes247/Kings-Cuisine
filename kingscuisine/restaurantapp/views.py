from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from .forms import BookingForm, ContactForm

def home(request):
    return render(request, 'index.html')

def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            people = form.cleaned_data['people']
            message = form.cleaned_data['message'] or 'No special requests'

            full_message = (
                f"Reservation Request\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Phone: {phone}\n"
                f"Date: {date}\n"
                f"Time: {time}\n"
                f"Party Size: {people}\n"
                f"Message: {message}"
            )
            send_mail(
                f'Reservation from {name}',
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ['kingsleycodes247@gmail.com'], 
                fail_silently=False,
            )
           
            return redirect(reverse('home') + '#book-a-table?sent=1')
    return redirect(reverse('home') + '#book-a-table')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"From: {name} ({email})\n\n{message}"
            send_mail(
                f'{subject} from {name}',
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ['kingsleycodes247@gmail.com'], 
                fail_silently=False,
            )
            # Correct redirect with fragment and query
            return redirect(reverse('home') + '#contact?sent=1')
    return redirect(reverse('home') + '#contact')
