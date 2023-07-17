from django.shortcuts import render, redirect
from .forms import SubscriptionForm
from .models import Subscriber
from django.contrib import messages


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            # Save the form data in the admin
            form_data = form.cleaned_data
            subscriber = Subscriber.objects.create(
                username=form_data["username"], email=form_data["email"])
            subscriber.save()

        messages.success(request, 'You are now a subscriber!')

    else:
        form = SubscriptionForm()
    return render(request, 'subscribe/subscribe.html', {'form': form})
