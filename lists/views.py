from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from lists.models import Item


# Create your views here.

@csrf_exempt
def home_page(request):
    
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
    
    #if request.method == 'POST':
    #    return HttpResponse(request.POST['item_text'])
    #return render(request, 'home.html')
    #return HttpResponse('<html><title>To-Do lists</title></html>')
    

#home_page = None