# Generated by Django 2.2.24 on 2023-03-21 10:55

from django.db import migrations


def set_newbuilding_marker(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.filter(construction_year__gte=2015):
        flat.new_building = True
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_auto_20230321_1255'),
    ]

    operations = [
        migrations.RunPython(set_newbuilding_marker),
    ]
