# Generated by Django 2.2.24 on 2022-11-09 15:26

from django.db import migrations
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException


def format_phonenumber(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.filter(owner_pure_phone=None):
        try:
            parsed_phonenumber = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        except NumberParseException:
            safe_wrong_number = '+70000000000'
            parsed_phonenumber = phonenumbers.parse(safe_wrong_number, 'RU')
        if phonenumbers.is_valid_number(parsed_phonenumber):
            flat.owner_pure_phone = parsed_phonenumber
            flat.save()


def remove_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    flats.update(owner_pure_phone=None)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20221109_1249'),
    ]

    operations = [
        migrations.RunPython(format_phonenumber, remove_pure_phone)
    ]
