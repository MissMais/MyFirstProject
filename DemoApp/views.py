from django.shortcuts import render, redirect
from DemoApp.models import Users
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def home(request):
    if request.method == 'POST':
        id = request.POST['Id']
        name = request.POST['Name'] 
        age = request.POST['Age']
        salary = request.POST['Salary']
        city = request.POST['City']
        # print(id, name, age, salary, city)
        user = Users(userid=id, username=name, age=age, salary=salary, city=city)
        user.save()
        return redirect ('/')
    else:

        users = Users.objects.all
        return render (request, 'home.html', {'users':users})