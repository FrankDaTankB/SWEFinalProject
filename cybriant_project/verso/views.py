from django.shortcuts import render

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
# Create your views here.
