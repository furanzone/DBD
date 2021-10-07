from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import status, views
from rest_framework.response import Response
from src import DbLoader as dl 

# Create your views here.

# # demo
# class DemoView(TemplateView):
#     template_name = 'demo.html'

class mapping(views.APIView):

    def post(self):
        try:

            x = dl.DbLoader(host='localhost', port='', dbname='djangodb', user='postgres', password='1234')
            x.connectDB()

            output = x.view_connDB()
            return()

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        return 0
