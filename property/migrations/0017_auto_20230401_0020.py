# Generated by Django 2.2.24 on 2023-03-31 21:20

from django.db import migrations


def add_flats(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    Owner = apps.get_model("property", "Owner")
    for owner in Owner.objects.all():
        apartments = Flat.objects.filter(owner=owner.owner)
        owner.flats.set(apartments)
        owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20230401_0019'),
    ]

    operations = [
        migrations.RunPython(add_flats),
    ]