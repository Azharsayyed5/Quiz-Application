# Generated by Django 2.1.5 on 2019-08-31 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Questions',
            new_name='QuestionMaster',
        ),
        migrations.AlterModelTable(
            name='questionmaster',
            table='QuestionMaster',
        ),
    ]
