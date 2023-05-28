from django.urls import path
from . import views
urlpatterns = [
    path('htmltest',views.htmltest,name="htmltest"),
    path('uploadfile',views.uploadfile,name='uploadfile'),
    path('database',views.database,name='database')
]