from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from importlib import import_module
from os import listdir
from os.path import isfile, join

class Command(BaseCommand):
    help = 'Installs Swish Apps'

    @staticmethod
    def handle(*args, **options):

        for app in apps.get_app_configs():

            if 'django.contrib' in app.name: continue   # Ignore Django Contrib Apps

            print(f"---> Processing : {app.name}")

            try:
                im = import_module(app.name + '.swish')
                swish_app = getattr(im, str(app.name).capitalize() + 'SwishApp')

                print(f"Version : {swish_app.__version__}")

                app_component_path = f'{app.name.lower()}\\components'
                app_actions = [f for f in listdir(app_component_path) if isfile(join(app_component_path, f))]

                for app_action in app_actions:
                    if app_action == '__init__.py' or '.pyc' in app_action: continue  # Skip __inits__ and ignore .pyc
                    print(f"Processing App Action : {app_action}")
                    app_action = app_action.replace('.py', '')
                    swish_app_action_im = import_module(app.name + '.components.' + app_action)
                    class_format = f"{app.name.capitalize()}{app_action.capitalize()}Component"
                    swish_app_action_im_class = getattr(swish_app_action_im, class_format)

                    print(swish_app_action_im_class.__description__)


            except TypeError as e:
                print("Not a Swish App!")

            except Exception as e:
                print("---> Does not appear to be a Swish App")
                print(f"Error Details: {e}")
