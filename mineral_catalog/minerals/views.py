from django.shortcuts import render, get_object_or_404

from .models import Mineral
from collections import OrderedDict

# Create your views here.


def mineral_detail(request, pk):
    minerals = Mineral.objects.values().all()
    field_count = {}

    for mineral in minerals:
        for key, value in mineral.items():
            if value != '' and key != 'id':
                try:
                    field_count[key] = field_count[key] + 1
                except KeyError:
                    field_count[key] = 1

    # mineral = Mineral.objects.values().get(pk=pk)
    mineral = get_object_or_404(Mineral, pk=pk)
    mineral = mineral.__dict__
    field_count = OrderedDict(
        sorted(field_count.items(), key=lambda x: x[1], reverse=True))

    return render(request, 'mineral_detail.html',
                  {'mineral': mineral,
                   'detail': True,
                   'field_count': field_count})
