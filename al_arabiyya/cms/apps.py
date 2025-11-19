"""AppConf for al_arabiyya.cms"""

from django.apps import AppConfig


# Create your config here.
class CMSConfig(AppConfig):
    """App configuration for al_arabiyya.cms"""

    name = "al_arabiyya.cms"
    label = "app_cms"
    default_auto_field = "django.db.models.BigAutoField"
