from ekartApp.models import Kart


def cart_count(request):# function executes own its own as registered in settings.templates
    if request.user.is_authenticated:
        count=Kart.objects.filter(user=request.user,status="inkart").count
        return {'count':count }
    else:
        return {'count':0}