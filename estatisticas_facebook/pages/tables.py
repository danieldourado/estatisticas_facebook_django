import django_tables2 as tables
from .models import *

class PageInsightsTable(tables.Table):
    class Meta:
        model = PageInsights
        template = 'django_tables2/bootstrap.html'