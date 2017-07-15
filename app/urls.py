from django.conf.urls import url
from .views import TrackList

app_name = 'app'

urlpatterns = [
    url(r'^tracks/', view=TrackList.as_view())
]
