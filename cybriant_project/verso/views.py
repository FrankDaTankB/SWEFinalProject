from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import customerRegistration

from neomodel import db, clear_neo4j_database, StructuredNode, UniqueIdProperty, StringProperty, IntegerProperty, RelationshipTo

# Put classes for neo4j here
class Customer(StructuredNode):
    uid = UniqueIdProperty()
    companyName = StringProperty(unique_index=True)
    subCompany = StringProperty(unique_index=True)
    Point_of_Contact = StringProperty(unique_index=True)
    phoneNumber = IntegerProperty(index=True, default=0)
    email = StringProperty(unique_index=True)
    domain2cust = RelationshipTo('domainName', 'customerDomain')
    ip2cust = RelationshipTo('ipAddress', 'customerIP')
    amazon2cust = RelationshipTo('amazonS3', 'customerAmazonS3')

class domainName(StructuredNode):
    uid = UniqueIdProperty()
    domainName = StringProperty(unique_index=True)

class ipAddress(StructuredNode):
    uid = UniqueIdProperty()
    ipAddress = StringProperty(unique_index=True)

class amazonS3(StructuredNode):
    uid = UniqueIdProperty()
    amazonS3 = StringProperty(unique_index=True)

# Views here
def home(request):
    return render(request, 'verso/login.html')

def index(request):
    return render(request, 'verso/index.html', {'title': 'Welcome'})

def customerReg(request):
    if request.method == 'POST':
        form = customerRegistration(request.POST)
        if form.is_valid():
            newCustomer = Customer(companyName = 'CompanyName', subCompany = 'SubCompany', Point_of_Contact = 'point_of_Contact', phoneNumber = 'PhoneNumber', email = 'Email').save()
            newDomain = domainName(domainName = 'DomainName').save()
            newIP = ipAddress(ipAddress = 'IpAddress').save()
            newAmazonS3 = amazonS3(amazonS3 = 'AmazonS3').save()
            messages.success(request, f'Customer has been added!')
            return redirect('verso-index')
    else:
        form = customerRegistration()
    return render(request, 'verso/customerReg.html', {'form': form})

def searchCustomer(request):
    return render(request, 'verso/searchCustomer.html')
# Create your views here.
