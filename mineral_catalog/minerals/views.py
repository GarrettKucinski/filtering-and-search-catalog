from django.shortcuts import render

from .models import Mineral
from collections import OrderedDict

# Create your views here.


def mineral_detail(request, pk):
    mineral = Mineral.objects.values().get(pk=pk)
    mineral.pop('id', None)

    mineral = OrderedDict(
        sorted(mineral.items(), key=lambda x: x[1], reverse=True))

    return render(request, 'mineral_detail.html',
                  {'mineral': mineral, 'detail': True})
