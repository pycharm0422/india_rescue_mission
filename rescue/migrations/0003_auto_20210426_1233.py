# Generated by Django 2.2.17 on 2021-04-26 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rescue', '0002_doctors'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Doctors',
            new_name='Doctor',
        ),
    ]
