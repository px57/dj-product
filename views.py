from django.shortcuts import render
from gpm.http import Response

def __empty__(request):
    res = Response()
    return res.success()
