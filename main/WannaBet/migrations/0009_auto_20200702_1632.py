# Generated by Django 3.0.7 on 2020-07-02 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WannaBet', '0008_auto_20200701_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='identity',
            field=models.TextField(blank=True, max_length=8),
        ),
    ]
