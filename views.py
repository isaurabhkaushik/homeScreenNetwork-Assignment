from django.shortcuts import render
from rest_framework.exceptions import Throttled
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.throttling import AnonRateThrottle

import datetime

# Create your views here.
from django.http import HttpResponse


class ThrottlerViewset( APIView):
    # API accepting request to return current datetime
    def get(self, request):
        current_datetime = datetime.datetime.now()
        return HttpResponse("Current datetime is {}".format(current_datetime), status=status.HTTP_200_OK)
