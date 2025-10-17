from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import TemplateView
from ekartApp.models import Product,Kart
from ekartApp.forms import UserRegistartionForm,LoginForm,kartform
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from ekartApp.authentication import login_recquired
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
    def post(self,request):
        form=UserRegistartionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
class LoginView(View):
    def get(self,request):
        form=LoginForm()
        return render (request,"login.html",{"form":form})
    def post(self,request):
        u_name=request.POST.get("username")
        pswd=request.POST.get("password")
        res=authenticate(request,username=u_name,password=pswd)
        if res:
            login(request,res)
            return redirect("home_view")
        
@method_decorator(login_recquired,name="dispatch")
class AddCartView(View):
    def get(self,request,*args,**kwargs):
        form=kartform()
        return render(request,'add_to_cart.html',{'form':form,})
    def post(self,request,*args,**kwargs):
        print(kwargs)
        product=Product.objects.get(id=kwargs.get("id"))
        quantity=request.POST.get("quantity")
        user=request.user
        
        cart_items= Kart.objects.filter(user=user,Product=product,status="inkart")
        if cart_items:
            cart_items[0].quantity+=int(quantity)
            cart_items[0].save()
            return redirect("home_view")
        else:
            Kart.objects.create(user=user,Product=product,quantity=quantity)
            return redirect("home_view")




    
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('login')
    
class CartListView(View):
    def get(self,request):# function executes own its own as registered in settings.templates
        cart=Kart.objects.filter(user=request.user,status="inkart")
        return render(request,"cart_view.html",{"carts":cart})
        


