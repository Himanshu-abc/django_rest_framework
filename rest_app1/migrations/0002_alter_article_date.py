# Generated by Django 3.2.6 on 2021-09-02 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
