from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from ekartApp.models import Product
from ekartApp.forms import UserRegistartionForm
# Create your views here.

class HomeView(View):
    def get(self,request):
        products=Product.objects.all()
        return render(request,'index.html',{'products':products})
    
class productView(View):
    def get(self,request,**kwargs):
        product=Product.objects.get(id=kwargs.get("id"))
        return render(request,'product_details.html',{'product':product})
    
class userRegisterView(View):
    def get(self,request):
        form=UserRegistartionForm()
        return render(request,"register.html",{"form":form})
    