#   models.py

from django.db import models
from django.http import HttpResponse

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline


"""
    python manage.py makemigrations
    python manage.py migrate
"""

    from news.models import Article, Reporter

    # View all availabe objects
        Reporter.objects.all()
   
    # Creating a new Reporter object
       r = Reporter(full_name="John Smith")
       r.save()
       print(r.id)
       print(r.full_name)

    # Querying info
        Reporter.objects.get(id=1)
        Reporter.objects.get(full_name__startswith="John")
        Reporter.objects.filter(full_name__startswith="John")
        Reporter.objects.get(full_name__contains="mith")
    

    # Creating a new Article object
        from datetime import date

        a = Article(pub_date=date.today(), headline="Django is so cool", content="Post content here...", reporter=r)
        a.save()

    # Access Articles from Reporter object
        r = a.reporter
        print(r.full_name)

    # Access Articles from Reporter object
        r.article_set.all()

        r.delete()



# admin.py

    from django.contrib import admin

    from . import models

    admin.site.register(models.Article)



# urls.py

    from django.url import path
    from . import views

    urlpatterns = [
        path('articles/<int:year>/', views.year_archive),
        path('articles/<int:year>/<int:month>/', views.month_archive),
        path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail)
    ]



# views.py

    from django.shortcuts import render
    from .models import Article

    def year_archive(request, year):
        a_list = Article.objects.filter(pub_date__year=year)
        context = {'year': year, 'article_list': a_list}
        return render(request, 'news/year_archive.html', context)
 


#   news/template/news/year_archive.html

    {% extends "base.html" %}
    {% block title %}Articles for {{ year }}{% endblock title %}

    {% block content %}
    <h1>Articles for {{ year }}</h1>

    {% for article in a_list %}
        <p>{{ article.headline }}</p>
        <p>{{ article.reporter.full_name }}</p>
        <p>{{ article.pub_date|date:"F j, Y" }}</p>
    {% endfor %}
    {% endblock content %}


form django.db import models

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

python manage.py makemigrations
python manage.py MsiDigitalCertificate

path('', include('myapp.urls'))

from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.index, name="index")

]
{% url 'polls:index' %}

def index(request):
    return HttpResponse("Hello world")

def detail(request, id):
    details = Reports.objects.get(id=id)
    return render(request, 'polls/detail.html', {'details':details})

{% extends './base.html' %}
{% block content %}

{% endblock content %}

from django.db import models

class Article(models.Model):
    
    title = models.CharField(max_length=70)
    description = models.TextField()