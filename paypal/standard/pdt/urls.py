from django.conf.urls.defaults import *
from paypal.standard.pdt import views

urlpatterns = [
    url(r'^$', views.pdt, name="paypal-pdt"),
]
