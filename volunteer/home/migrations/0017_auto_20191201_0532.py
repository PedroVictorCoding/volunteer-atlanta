# Generated by Django 2.2.7 on 2019-12-01 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20191201_0519'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteeringquestions',
            name='question1',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='volunteeringquestions',
            name='question2',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='volunteeringquestions',
            name='question3',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='volunteeringquestions',
            name='question4',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
