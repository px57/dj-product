"""
    @description: This file contains the urls for the profiles app
"""

from django.urls import include
from django.urls import path

from . import views

urlpatterns = [
    # path(
    #     'signin/', 
    #     views.signin, 
    #     name='profiles__signin'
    # ),
    path("admin/", include("product.__views__.admin.urls")),
]