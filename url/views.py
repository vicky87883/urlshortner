from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
import string
import random

def generate_short_url():
    characters = string.ascii_letters + string.digits
    shortened_url = ''.join(random.choice(characters) for _ in range(6))
    return shortened_url

def home(request):
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        shortened_url = generate_short_url()
        url = URL(original_url=original_url, shortened_url=shortened_url)
        url.save()
        return render(request, 'url/home.html', {'shortened_url': shortened_url})
    return render(request, 'url/home.html')

def redirect_url(request, shortened_url):
    url = get_object_or_404(URL, shortened_url=shortened_url)
    return redirect(url.original_url)
