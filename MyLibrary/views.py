from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def LibraryHome_view(request):
  
  return render(request,'LibraryHome.html')