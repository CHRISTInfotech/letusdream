from django.contrib import messages
from django.shortcuts import redirect
from .models import SubscribeNewsletter, LUDPrograms

def email_subscription(request):
    email = request.POST['emailfornews']
    program = request.POST['program']
    if LUDPrograms.objects.filter(title=program).exists():
        program_db = LUDPrograms.objects.get(title=program)
    else:
        program_db = LUDPrograms.objects.create(title=program)
    
    if SubscribeNewsletter.objects.filter(email=email,program=program_db).exists():
        user = SubscribeNewsletter.objects.get(email=email,program=program_db)
        messages.success(request,'Subscription Information is with us since ' + user.subscribed_on.__str__() + ' !')
    else:
        SubscribeNewsletter.objects.create(email=email,program=program_db)
        messages.success(request,'Subscription Information Added !')
    
    return redirect('dreams','program')