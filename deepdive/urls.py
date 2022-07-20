from django.urls import path, re_path, register_converter
from . import views, converters

urlpatterns = [
    path('', views.index, name='index'),
]

# Registering Custom Path Converters
register_converter(converters.FourDigitYearConverter, 'yyyy')

# Regex path => /(?P<name>pattern)

# urlpatterns = [
#     path('articles/2003/', views.special_case_2003),
#     re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
#     path('articles/<int:year>/', views.year_archive),
#     path('articles/<int:year>/<int:month>', views.month_archive),
#     path('articles/<int:year>/<int:month>/<slug:slug>', views.article_detail),
# ]

# Path Converters
# str, int, slug, uuid, path


