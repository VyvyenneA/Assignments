from django.conf.urls import urls
form . import views

urlpatterns = [
    path(r'^$', views.index, name='index'),
]