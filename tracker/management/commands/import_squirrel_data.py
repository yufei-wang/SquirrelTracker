from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
from tracker.models import Squirrels
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
                    Date = datetime.datetime.strptime(item['Date'],'%m%d%Y'),
                    Age = item['Age'],
                    Primary_Fur_Color = item['Primary Fur Color'],
                    Location = item['Location'],
                    Specific_Location = item['Specific Location'],
                    Running = convertBool(item['Running']),
                    Chasing = convertBool(item['Chasing']),
                    Climbing = convertBool(item['Climbing']),
                    Eating = convertBool(item['Eating']),
                    Foraging = convertBool(item['Foraging']),
                    Other_Activities = item['Other Activities'],
                    Kuks = convertBool(item['Kuks']),
                    Quaas = convertBool(item['Quaas']),
                    Moans = convertBool(item['Moans']),
                    Tail_Flags = convertBool(item['Tail flags']),
                    Tail_Twitches = convertBool(item['Tail twitches']),
                    Approaches = convertBool(item['Approaches']),
                    Indifferent = convertBool(item['Indifferent']),
                    Runs_From = convertBool(item['Runs from']),
                    )
            result.save()
