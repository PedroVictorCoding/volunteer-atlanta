# Generated by Django 2.2.7 on 2019-11-15 01:44

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_userprofile_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='student_id',
            field=models.IntegerField(default=0, verbose_name=django.contrib.auth.models.User),
        ),
    ]