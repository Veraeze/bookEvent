# Generated by Django 5.0.4 on 2024-04-17 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_category_alter_event_attendees_alter_event_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='category',
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ManyToManyField(to='features.category'),
        ),
    ]
