from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import customerRegistration

from neomodel import config, db, clear_neo4j_database, StructuredNode, UniqueIdProperty, StringProperty, IntegerProperty, RelationshipTo, Relationship, RelationshipFrom

# Put classes for neo4j here
class Customer(StructuredNode):
    uid = UniqueIdProperty()
    companyName = StringProperty(unique_index=True)
    subCompany = StringProperty(unique_index=True)
    Point_of_Contact = StringProperty(unique_index=True)
    phoneNumber = StringProperty(index=True, default=0)
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
            cust_data = request.POST.dict()
            newCustomer = Customer(companyName = cust_data.get("CompanyName"),
            subCompany = cust_data.get("SubCompany"),
            Point_of_Contact = cust_data.get("point_of_Contact"),
            phoneNumber = cust_data.get("PhoneNumber"),
            email = cust_data.get("Email")).save()
            newDomain = domainName(domainName = cust_data.get("DomainName")).save()
            newIP = ipAddress(ipAddress = cust_data.get("IpAddress")).save()
            newAmazonS3 = amazonS3(amazonS3 = cust_data.get("AmazonS3")).save()
            d2crel = newCustomer.domain2cust.connect(newDomain)
            ip2custrel = newCustomer.ip2cust.connect(newIP)
            ama2custrel = newCustomer.amazon2cust.connect(newAmazonS3)
            messages.success(request, 'Customer has been added!')
            return redirect('verso-index')
    else:
        form = customerRegistration()
    return render(request, 'verso/customerReg.html', {'form': form})

def viewCustomer(request):
    return render(request, 'verso/viewCustomer.html')
# Create your views here.
