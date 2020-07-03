# Generated by Django 3.0.7 on 2020-07-03 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WannaBet', '0019_auto_20200703_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bet',
            name='identifier',
        ),
        migrations.RemoveField(
            model_name='bet',
            name='event',
        ),
        migrations.AddField(
            model_name='bet',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='for_event', to='WannaBet.Event'),
        ),
    ]
