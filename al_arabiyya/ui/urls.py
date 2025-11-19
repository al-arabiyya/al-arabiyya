"""URLConf for al_arabiyya.ui"""

from django.urls import path

from al_arabiyya.ui import views

# Create your URLConf here.
app_name = "app"

urlpatterns = [
    path("search/", views.SearchView.as_view(), name="search"),
]
