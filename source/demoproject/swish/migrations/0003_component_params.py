# Generated by Django 2.2.2 on 2019-10-24 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swish', '0002_component_componentaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='params',
            field=models.TextField(blank=True),
        ),
    ]
