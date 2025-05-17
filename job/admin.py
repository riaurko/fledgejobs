from django.contrib.admin import site
from job.models import Job
from job.models import Category


site.register(Job)
site.register(Category)