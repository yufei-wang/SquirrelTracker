# Generated by Django 3.1.2 on 2020-10-17 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrels',
            fields=[
                ('Longitude', models.FloatField(help_text='Longitude')),
                ('Latitude', models.FloatField(help_text='Latitude')),
                ('Unique_Squirrel_Id', models.CharField(help_text='Unique ID of the squirrell', max_length=50, primary_key=True, serialize=False, unique=True)),
                ('Shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], help_text='Shift', max_length=16)),
                ('Date', models.DateField(blank=True, help_text='Date', null=True)),
                ('Age', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], help_text='Age', max_length=50, null=True)),
                ('Primary_Fur_Color', models.CharField(blank=True, choices=[('Black', 'Black'), ('Gray', 'Gray'), ('Cinnamon', 'Cinnamon')], help_text='Primary Fur color', max_length=16, null=True)),
                ('Location', models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], help_text='Location', max_length=250, null=True)),
                ('Specific_Location', models.CharField(blank=True, help_text='Specific location', max_length=250, null=True)),
                ('Running', models.NullBooleanField(help_text='Running')),
                ('Chasing', models.NullBooleanField(help_text='Chasing')),
                ('Climbing', models.NullBooleanField(help_text='Climbing')),
                ('Eating', models.NullBooleanField(help_text='Eating')),
                ('Foraging', models.NullBooleanField(help_text='Foraging')),
                ('Other_Activities', models.CharField(blank=True, help_text='Other Activities', max_length=128, null=True)),
                ('Kuks', models.NullBooleanField(help_text='Kuks')),
                ('Quaas', models.NullBooleanField(help_text='Quaas')),
                ('Moans', models.NullBooleanField(help_text='Moans')),
                ('Tail_Flags', models.NullBooleanField(help_text='Tail_Flags')),
                ('Tail_Twitches', models.NullBooleanField(help_text='Tail_Twitches')),
                ('Approaches', models.NullBooleanField(help_text='Approaches')),
                ('Indifferent', models.NullBooleanField(help_text='Indifferent')),
                ('Runs_From', models.NullBooleanField(help_text='Runs_From')),
            ],
        ),
    ]