import os
import sys
import datetime
from django.shortcuts import render
from django.http import HttpResponse

der = os.getcwd()

sys.path.append(der + "\polls\ssd_keras")

from main import main

#num = main()

def index(request):
    num = main()
    dt_now = datetime.datetime.now()
    now = str(dt_now.year) + "-" + str(dt_now.month) + "-" + str(dt_now.day) + "-" + str(dt_now.hour) + ":" + str(dt_now.minute)
    return HttpResponse("人数は" + str(num) + "人です " + str(now))