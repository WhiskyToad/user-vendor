from django.apps import apps
from django.contrib import admin
from .models import ExtendUser

admin.site.register(ExtendUser)

app = apps.get_app_config("graphql_auth")

## looks for anything available above and adds to admin area
for model_name, model in app.models.items():
    admin.site.register(model)
