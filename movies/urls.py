from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^items', views.ItemView.as_view(), name='items'),
    url(r'^attributes', views.AttributeView.as_view(), name='attributes'),
]
