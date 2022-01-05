from django.urls import path, re_path
from django.views.generic import RedirectView

from . import views
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.static import serve
urlpatterns = [
    path('', views.index, name="index"),
    path(r"venues/", views.venues, name="venues"),
    path("venues/search", views.search_venue, name="search_venues"),
    path(r"venues/<int:venue_id>/", views.show_venue, name="show_venue"),
    path(r"venues/<int:venue_id>/edit", views.edit_venue, name="edit_venue"),
    path("venues/create", views.create_venue_form, name="venues_create"),
    path("artists/", views.artist, name="artist"),
    path("artists/search", views.search_artist, name="artist_search"),
    path("artists/<int:artist_id>/", views.show_artist, name="artist_show"),
    path("artists/create", views.create_artist_form),
    path("artists/<int:artist_id>/edit", views.edit_artist, name="edit_artist"),
    path("shows", views.shows, name="show"),
    path("shows/create", views.create_shows),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('ico/favicon.ico')))
]
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve),
    ]
else:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    ]

handler404 = views.not_found_error
handler500 = views.server_error
