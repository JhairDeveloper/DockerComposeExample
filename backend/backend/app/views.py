from django.http import JsonResponse
from .models import Item

def item_list(request):
    items = Item.objects.all().values()
    return JsonResponse(list(items), safe=False)
