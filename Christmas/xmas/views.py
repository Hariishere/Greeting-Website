from django.shortcuts import render
from . import Randmsg
# Create your views here.

def index(request):
    return render(request,'button.html')
def message(request):
    msg=Randmsg.get_random_message()
    return render(request,'Message.html',{'msg':msg})