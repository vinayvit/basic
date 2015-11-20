from django.conf.urls import url
from . import views
from catlogs.models import Publisher

urlpatterns = [
  url(r'^$', view.product_list(model=Publishers), name='product_list'),
  ]
