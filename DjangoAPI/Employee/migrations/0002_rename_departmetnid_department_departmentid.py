# Generated by Django 3.2 on 2023-02-15 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='DepartmetnId',
            new_name='DepartmentId',
        ),
    ]
