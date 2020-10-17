from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
from sightings.models import Squirrels
import csv
import os

class Command(BaseCommand):
    help = 'Import Squirrel data from the csv file'
    
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
        
        def conver_boo(str):
            if str.lower() == 'true':
                return True
            elif str.lower()=='false':
                return False
            else:
                return None

        for item in data:
            result = Squirrels(
                    Latitude = item['Y'],
                    Longitude = item['X'],
                    Unique_Squirrel_Id = item['Unique Squirrel ID'],
                    Shift = item['Shift'],
                    Date = datetime.strptime(item['Date'],'%m%d%Y'),
                    Age = item['Age'],
                    Primary_Fur_Color = item['Primary Fur Color'],
                    Location = item['Location'],
                    Specific_Location = item['Specific Location'],
                    Running = conver_boo(item['Running']),
                    Chasing = conver_boo(item['Chasing']),
                    Climbing = conver_boo(item['Climbing']),
                    Eating = conver_boo(item['Eating']),
                    Foraging = conver_boo(item['Foraging']),
                    Other_Activities = item['Other Activities'],
                    Kuks = conver_boo(item['Kuks']),
                    Quaas = conver_boo(item['Quaas']),
                    Moans = conver_boo(item['Moans']),
                    Tail_Flags = conver_boo(item['Tail flags']),
                    Tail_Twitches = conver_boo(item['Tail twitches']),
                    Approaches = conver_boo(item['Approaches']),
                    Indifferent = conver_boo(item['Indifferent']),
                    Runs_From = conver_boo(item['Runs from']),
                    )
            result.save()
