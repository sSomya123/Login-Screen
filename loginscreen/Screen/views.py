from django.shortcuts import render

def index(request):
    return render(request, 'Screen/index.html')  # Renders the index.html template
