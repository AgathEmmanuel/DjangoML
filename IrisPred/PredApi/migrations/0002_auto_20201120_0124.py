# Generated by Django 3.1.3 on 2020-11-19 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PredApi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='specs',
            name='classification',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='specs',
            name='petal_length',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='specs',
            name='petal_width',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='specs',
            name='sepal_length',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='specs',
            name='sepal_width',
            field=models.FloatField(default=0),
        ),
    ]
