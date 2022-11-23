# Generated by Django 3.2.16 on 2022-11-19 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Reader',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='Description',
            field=models.TextField(),
        ),
    ]
