# Generated by Django 2.2.7 on 2019-12-01 05:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0015_remove_post_category_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteeringLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_name', models.CharField(max_length=250)),
                ('activity', models.CharField(max_length=1000)),
                ('hours', models.CharField(max_length=250)),
                ('date_activity', models.CharField(max_length=250)),
                ('supervisor_contact', models.CharField(max_length=1000)),
                ('signature', models.CharField(max_length=50000)),
                ('user', models.ForeignKey(on_delete='', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VolunteeringQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete='', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]
