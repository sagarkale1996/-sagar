from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    print("i amm view")
    return HttpResponse("This is view ")
