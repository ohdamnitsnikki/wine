from django.shortcuts import render, redirect
from .forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            # Save the form data in the admin
            form_data = form.cleaned_data
            form.save()
            return redirect('subscribe/subscribe.html')

        messages.success(request, f'You are now a subscriber!')

    else:
        form = SubscriptionForm()
    return render(request, 'subscribe/subscribe.html', {'form': form})
