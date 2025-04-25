from django.shortcuts import render

# Create your views here.
def show_name(request):
    return render(request, 'backend/show_name.html', {'name': 'Johnbkk'})