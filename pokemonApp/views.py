from django.shortcuts import render
from .models import Pokemon
#from django.db.models import Q


def index(request):
    results = Pokemon.objects.all()
    order_by = request.GET.get('order_by', None)
    if order_by:
        results = results.order_by(order_by)

    type1_contains = request.GET.get('type1_contains')
    print(type1_contains)
    if type1_contains != '' and type1_contains is not None:
        results = results.filter(type1__icontains=type1_contains)

    return render(request, 'home.html', {"data": results})
