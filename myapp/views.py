from django.shortcuts import render
from django.http import HttpResponse

from myapp.models import Dreamreal
# Basic way of sending a response, also takes number as a param
# def hello(request, number):
#     text = "<h1>Hello, welcome to my page</h1>" + str(number)
#     return HttpResponse(text)


# Using the render function
def index(request):
    weekDays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return render(request, "hello.html", {"today": 1, "weekDays": weekDays, "n": 1, "title": "My Page"})

def about(request):
    return HttpResponse("<h1>About Page</h1>")

# CRUD Operations
def crudops(request):
    # dreamreal = Dreamreal(website = "test.com", mail = "test@test.com", name = "Test123 Tester", phonenumber = 145677)

    # dreamreal.save()
    objects = Dreamreal.objects.all()

    for elem in objects:
        print(elem.name)
    print("\n")

    singledata = Dreamreal.objects.filter(name="Test123")
    print(singledata)
    return HttpResponse("<h1>Loading...</h1>")