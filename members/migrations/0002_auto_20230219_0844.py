# Generated by Django 4.1.7 on 2023-02-19 08:44

from django.db import migrations


def seed_database_options(apps, schema_editor):
    DataBase = apps.get_model('members', 'DataBase')
    dbs = [
        "Scopus",
        "PubMed",
        "Dimensions",
        "Web of Science"
    ]
    for db in dbs:
        db_model = DataBase(label=db)
        db_model.save()


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_database_options),
    ]
