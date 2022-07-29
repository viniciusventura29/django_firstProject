from contextlib import redirect_stderr
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.validators import validate_email


from home.models import Users


def home_index(request):
    infoData_sql = Users.objects.all()
    context = {
        'users': infoData_sql
    }

    return render(request, 'home/index.html', context)


def home_details(request, id):
    userData = Users.objects.get(id=id)

    return render(request, 'home/details.html', {'userData': userData})

def save_user(request):
    if str(request.method)!='POST':
        return render(request,'home/form_cadastro.html')
    else:

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        active = request.POST.get('active')
        price = request.POST.get('price')
        photo = request.FILES.get('photo')

        if (
            not name or not phone 
            or not email or not active
            or not price
        ):
            return render(request, 'home/forma_cadastro.html')

        try:
            validate_email(email)

        except:
            if Users.objects.filter(name=name).exists():
                return render(request, 'home/forma_cadastro.html')


        data_to_save = Users.objects.create(
            name = name,
            phone = phone,
            email = email,
            active = active,
            price = price,
            photo = photo,
        )

        data_to_save.save()

        return redirect('homeindex')
