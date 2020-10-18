from django.core.management.base import BaseCommand
from sightings.models import Squirrels
import csv
import os
import datetime

class Command(BaseCommand):
    help = 'Export the data in CSV format'
    def add_arguments(self,parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        meta = Squirrels._meta
        fields = [i.name for i in meta.fields]

        with open(options['path'],'w') as fp:
            w = csv.writer(fp)
            w.writerow(fields)
            for obj in Squirrels.objects.all():
                row = [getattr(obj, f) for f in fields]
                print(row)
                w.writerow(row)
