from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def send_file(request):
    id_client = 1234
    if request.method == "GET":
        return render(request, 'send_file.html', {'id_client':id_client})
    
    elif request.method == "POST":
        file = request.POST.get('ID')
        print(file)
        return render(request, 'send_file.html', {'id_client':id_client})