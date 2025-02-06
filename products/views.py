from django.shortcuts import render, HttpResponse


# Create your views here.
def products(request):
    return render(request, "products.html")
