from django.shortcuts import render

from .models import Mineral

# Create your views here.


def mineral_detail(request, pk):
    mineral = Mineral.objects.get(pk=pk)
    return render(request, 'mineral_detail.html',
                  {'mineral': mineral, 'detail': True})
