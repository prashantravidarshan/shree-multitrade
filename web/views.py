from django.shortcuts import render
from web import models


def index(request):
    banner = models.Banner.objects.get(pk=1)
    contact = models.Contact.objects.get(pk=1)
    aboutus_card = models.AboutUs.objects.all()
    '''aboutus_card2 = models.AboutUs.objects.get(pk=2)
    aboutus_card3 = models.AboutUs.objects.get(pk=3)'''
    who_we_are = models.WhoWeAre.objects.get(pk=1)

    context = {
        'banner': banner,
        'contact': contact,
        'aboutus_card': aboutus_card,
        'who_we_are': who_we_are,
    }

    return render(request, 'web/index.html', context)


def dashboard(request):
    return render(request, 'web/user_panel.html')