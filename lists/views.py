from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def home_page(request):
    return render(request, 'home.html', {'new_item_text': request.POST.get('item_text','')})
    
    #if request.method == 'POST':
    #    return HttpResponse(request.POST['item_text'])
    #return render(request, 'home.html')
    #return HttpResponse('<html><title>To-Do lists</title></html>')
    

#home_page = None