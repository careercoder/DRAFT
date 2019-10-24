# The purpose of this is to dynamically create a menu for the new Django Admin
# Swish Admin Menu Generation
from django.apps import apps


class SwishAdminMenu:

    def generate(self):

        for name, app in apps.app_configs.items():
            print(f"--> {name}")
            for model in apps.all_models[name]:
                print(f"{model}")


"""
from swish.admin.includes.generate_menu import *
s = SwishAdminMenu()
s.generate()
"""