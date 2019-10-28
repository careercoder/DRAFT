from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from importlib import import_module
from os import listdir
from os.path import isfile, join

class Command(BaseCommand):
    help = 'Installs Swish Apps'

    @staticmethod
    def handle(*args, **options):
        #import subprocess
        #subprocess.call(['manage.py --help'])   # run
        pass