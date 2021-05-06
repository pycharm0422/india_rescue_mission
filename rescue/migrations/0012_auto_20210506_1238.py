# Generated by Django 2.2.17 on 2021-05-06 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rescue', '0011_volunteer'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='contact',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('others', 'others')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='profile',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='state',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='telemedicine',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='telemedicine',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='telemedicine',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='telemedicine',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='telemedicine',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('others', 'others')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='telemedicine',
            name='profile',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='telemedicine',
            name='state',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='telemedicine',
            name='testimonial',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('others', 'others')], max_length=200, null=True)),
                ('blood_group', models.CharField(max_length=20, null=True)),
                ('address', models.TextField(null=True)),
                ('contact', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('profile', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(max_length=200, null=True)),
                ('country', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Counsellor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('others', 'others')], max_length=200, null=True)),
                ('address', models.TextField(null=True)),
                ('contact', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('profile', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(max_length=200, null=True)),
                ('country', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
