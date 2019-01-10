from django.shortcuts import render

# Create your views here.


def products_list(request):
    return render(request, 'products_list.html')


def publish(request):
    if request.method == 'GET':
       return render(request, 'publish.html')
    elif request.method == 'POST':
    	pass
