from django.shortcuts import render
from .models import Link
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
# Create your views here.


def crawler(request):

    if request.method == 'POST':
        site = request.POST.get('site')
        page = requests.get(site)
        text = page.text
        soup = BeautifulSoup(text, 'html.parser')
        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_name = link.string
            link = Link.objects.create(address=link_address, name=link_name)
            link.save()
        return HttpResponseRedirect('/')
    else:
        links = Link.objects.all()
        return render(request, 'scrape/link.html', {'links': links})


def clear(request):
    Link.objects.all().delete()
    return render(request, 'scrape/link.html')

