from django.shortcuts import render
from django.http import HttpResponse

# Basic way of sending a response, also takes number as a param
def hello(request, number):
    text = "<h1>Hello, welcome to my page</h1>" + str(number)
    return HttpResponse(text)


# Using the render function
def template(request):
    return render(request, "myapp/template/hello.html", {})