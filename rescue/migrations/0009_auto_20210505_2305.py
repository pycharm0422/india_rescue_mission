# Generated by Django 2.2.17 on 2021-05-05 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rescue', '0008_messageboard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageboard',
            name='message',
            field=models.TextField(null=True),
        ),
    ]
