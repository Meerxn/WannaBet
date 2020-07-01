# Generated by Django 3.0.7 on 2020-07-01 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WannaBet', '0005_auto_20200701_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sides',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side', models.CharField(choices=[('W', 'Win'), ('L', 'Loss'), ('D', 'Draw')], max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='bet',
            name='descrition',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bet',
            name='type',
            field=models.CharField(choices=[('M', 'Money'), ('A', 'Activity'), ('G', 'Gift')], default='None', max_length=1),
        ),
        migrations.DeleteModel(
            name='Challange',
        ),
        migrations.AddField(
            model_name='sides',
            name='bet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='side_choices', to='WannaBet.Bet'),
        ),
        migrations.AddField(
            model_name='sides',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WannaBet.Profile'),
        ),
        migrations.AddField(
            model_name='bet',
            name='members',
            field=models.ManyToManyField(through='WannaBet.Sides', to='WannaBet.Profile'),
        ),
    ]