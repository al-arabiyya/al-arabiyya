"""AppConf for al_arabiyya.api"""

from django.apps import AppConfig


# Create your AppConf here.
class APIConfig(AppConfig):
    """App Configuration for al_arabiyya.api"""

    name = "al_arabiyya.api"
    label = "app_api"
    default_auto_field = "django.db.models.BigAutoField"
