from django.conf.urls import url
from.import views

app_name = 'meal_plans.urls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]