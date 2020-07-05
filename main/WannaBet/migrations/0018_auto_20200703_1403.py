# Generated by Django 3.0.7 on 2020-07-03 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WannaBet', '0017_remove_bet_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bet',
            name='event',
        ),
        migrations.AddField(
            model_name='bet',
            name='event',
            field=models.ManyToManyField(null=True, related_name='for_event', to='WannaBet.Event'),
        ),
    ]