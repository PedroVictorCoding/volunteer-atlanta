# Generated by Django 2.2.5 on 2019-10-20 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='content',
            new_name='message',
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
