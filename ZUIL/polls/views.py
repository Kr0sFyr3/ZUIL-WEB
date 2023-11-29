from django.shortcuts import render

from django.http import HttpResponse

import subprocess

def choiseScreen(request):
    return render(request, 'polls/choiseScreen.html')

'''
def execute_script(request):
    try:
        script_path = '../ZUIL/reken.py'  # Update with the actual path to your script
        result = subprocess.check_output(['python', script_path], universal_newlines=True)
        return HttpResponse(result)
    except subprocess.CalledProcessError as e:
        return HttpResponse(f"Error: {e}")
'''

def home(request):
    return render(request, 'polls/home.html')

def scanScreen(request):
    return render(request, 'polls/scanScreen.html')

def scanItemScreen(request):
    return render(request, 'polls/scanItemScreen.html')

def returnScreen(request):
    return render(request, 'polls/returnScreen.html')

def lendScreen(request):
    return render(request, 'polls/lendScreen.html')

def lendMultipleScreen(request):
    return render(request, 'polls/lendMultipleScreen.html')