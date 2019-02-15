from django.db import models

# Create your models here.
from django.db.models import signals
from neomodel import StructuredNode, StringProperty, DateProperty, clear_neo4j_database, db
from django_neomodel import DjangoNode
