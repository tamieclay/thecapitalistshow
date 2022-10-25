from django.shortcuts import render

from home.models import Register ,Pitch

# Create your views here.


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        
        new_user = Register(name=name, email=email,number=number)
        new_user.save()
               
    data = Register.objects.all()
    context = {
        'data' : data
    }
    return render(request,"index.html", context)