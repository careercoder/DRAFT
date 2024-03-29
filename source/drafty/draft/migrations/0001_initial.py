# Generated by Django 2.2.6 on 2019-10-27 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Friendly name of extension.', max_length=100)),
                ('type', models.CharField(help_text='Extension Type', max_length=20)),
                ('element', models.CharField(help_text='Unique name of the element.', max_length=100)),
                ('path', models.CharField(help_text='Module Installed Path', max_length=150)),
                ('params', models.TextField(blank=True)),
                ('data', models.TextField(blank=True)),
                ('enabled', models.BooleanField(default=False)),
                ('state', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('slug', models.SlugField(max_length=75)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('anchor', models.CharField(max_length=75)),
                ('slug', models.SlugField(max_length=75)),
                ('link', models.CharField(blank=True, max_length=1064)),
                ('params', models.TextField(blank=True, help_text='Additional params to allow processing')),
                ('icon', models.CharField(blank=True, max_length=35)),
                ('position', models.IntegerField(default=0)),
                ('home', models.BooleanField(default=False, help_text='Is home page?')),
                ('component', models.ForeignKey(blank=True, null=True, on_delete='cascades', to='draft.Component')),
                ('menu', models.ForeignKey(null=True, on_delete='cascade', to='draft.Menu')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='draft.MenuItem')),
            ],
        ),
    ]
