"""
    @description: This file contains the urls for the profiles app
"""

from django.urls import path
from . import views


urlpatterns = [
    path("init_product/", views.init_product, name="init_product"),
    path("update_product/", views.update_product, name="update_product"),
]
