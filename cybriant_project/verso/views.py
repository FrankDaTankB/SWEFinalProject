from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import customerRegistration

from neomodel import db, clear_neo4j_database, StructuredNode, UniqueIdProperty, StringProperty, IntegerProperty, RelationshipTo

class Person(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)
    # traverse outgoing IS_FROM relations, inflate to Country objects

def home(request):
    # this will create a new jim everytime you login
    jim = Person(name='Jim', age=3).save()
    jim.save() # validation happens here
    return render(request, 'verso/login.html')


def index(request):
    return render(request, 'verso/index.html', {'title': 'Welcome'})

def customerReg(request):
    if request.method == 'POST':
        form = customerRegistration(request.POST)
        if form.is_valid():
            messages.success(request, f'Customer has been added!')
            return redirect('home')
    else:
        form = customerRegistration()
    return render(request, 'verso/customerReg.html', {'form': form})

def searchCustomer(request):
    return render(request, 'verso/searchCustomer.html')
# Create your views here.
