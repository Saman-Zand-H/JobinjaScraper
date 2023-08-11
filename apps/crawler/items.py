import scrapy
from scrapy_djangoitem import DjangoItem

from demand.models import DemandTechnology


class Technology(DjangoItem):
    django_model = DemandTechnology
    