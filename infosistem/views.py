from django.shortcuts import render
from .models import Detal, Copybook, Aonn, Alist


def newcopybook(request):

    return render(request, 'infosistem/newcopybook.html')

