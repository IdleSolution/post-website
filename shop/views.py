from django.shortcuts import render
from .models import Item

def index(request):
    items = Item.objects.all()
    return render(request, 'shop/index.html', {'items': items})

def item(request, pk):
    item = Item.objects.get(pk=pk)
    item.views += 1
    item.save()
    return render(request, 'shop/item.html', {'item': item})
