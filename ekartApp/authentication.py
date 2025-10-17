from django.shortcuts import redirect
from django.contrib import messages

def login_recquired(fn):   #decoratpr function
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            # messages.warning(request,"LOGIN FAILED")
            return redirect("login")
        else:
            return fn(request,*args,**kwargs)
        
    return wrapper
