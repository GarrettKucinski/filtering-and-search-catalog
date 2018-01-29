from django.shortcuts import render

from minerals.models import Mineral


def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(request, 'mineral_list.html', {'minerals': minerals})
