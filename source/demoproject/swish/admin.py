from django.contrib import admin
from django.apps import apps

from django.apps import apps, AppConfig
from django.contrib import admin
import json

class ListAdminMixin(object):
    def __init__(self, model, admin_site):

        # We know this is going to be constant for now...
        component_model = apps.get_model('swish', 'Component')
        model_meta = str(model._meta)
        try:
            print(model_meta)
            component = component_model.objects.get(linked_model=model_meta)
            params = json.loads(component.params)

            # List Display
            if params['admin']['list_display']:
                print("list_display")
                self.list_display = params['admin']['list_display']

            try:
                self.list_filter = params['admin']['list_filter']
            except Exception as e:
                pass

            try:
                if params['admin']['search_fields']:
                    print("Search Fields")
                    self.search_fields = params['admin']['search_fields']
            except Exception as e:
                pass

        # In case it fails for some reason, show default....
        except Exception as e:
            # limit this... as of now it shows EVERYTHING!
            self.list_display = [field.name for field in model._meta.fields if field.name != "id"]

        super(ListAdminMixin, self).__init__(model, admin_site)






class SwishApp(AppConfig):

    name = 'swish'

    def __init__(self):
        pass

    def ready(self):
        models = apps.get_models()
        for model in models:
            admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
            try:
                admin.site.register(model, admin_class)
            except admin.sites.AlreadyRegistered:
                pass
            # print(model._meta)

SwishApp().ready()
