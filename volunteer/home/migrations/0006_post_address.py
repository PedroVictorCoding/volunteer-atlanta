# Generated by Django 2.2.5 on 2019-09-28 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20190927_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='address',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
