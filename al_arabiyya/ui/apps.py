"""AppConf for al_arabiyya.ui"""

from django.apps import AppConfig


# Create your config here.
class UIConfig(AppConfig):
    """App configuration for al_arabiyya.ui"""

    name = "al_arabiyya.ui"
    label = "app_ui"
    default_auto_field = "django.db.models.BigAutoField"
