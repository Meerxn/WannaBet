# Generated by Django 3.0.7 on 2020-07-02 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WannaBet', '0013_auto_20200702_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='members',
            field=models.ManyToManyField(related_name='bet_member', to='WannaBet.Profile'),
        ),
    ]
