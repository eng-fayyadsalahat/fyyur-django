import datetime
from django.core.handlers import exception
from django.db import transaction
from django.shortcuts import render, redirect
from .models import Venue, Artist, Show
from django.views.decorators.csrf import csrf_exempt
from . import forms
from django.views.defaults import *


# Create your views here.


def index(request):
    return render(request, "pages/home.html")


@csrf_exempt
def venues(request):
    try:
        def add_venue(area):
            venues = []
            for venue in area:
                venues.append({"id": venue.id, "name": venue.name, "num_upcoming_show": len(
                    Show.objects.filter(venue_id=venue.id).filter(start_time__gte=datetime.datetime.now()).all()
                )})
            return venues

        data = []
        areas = Venue.objects.values_list("state", "city").order_by("state", "city").distinct("city", "state")
        for area in areas:
            area_venue = Venue.objects.filter(state=area[0]).filter(city=area[1]).all()
            data.append({"city": area[1], "state": area[0], "venues": add_venue(area_venue)})

        return render(request, "pages/venues.html", {"areas": data})
    except Exception:
        not_found_error(request, exception)
    except:
        server_error(request, exception)


@csrf_exempt
def search_venue(request):
    try:
        if request.method == "POST":
            search = request.POST["search_term"]
            venue_search = Venue.objects.filter(name__icontains=search).all()

            count = Venue.objects.filter(name__icontains=search).all().count()
            data = []
            for searched in venue_search:
                data.append({
                    "id": searched.id,
                    "name": searched.name,
                    "num_upcoming_shows": count

                })
        response = {
            "count": count,
            "data": data
        }

        return render(request, "pages/search_venues.html", {"results": response})
    except HttpResponseNotFound:
        page_not_found(request, template_name="errors/404.html")
    except HttpResponseServerError:
        server_error(request, template_name="errors/500.html")


@csrf_exempt
def show_venue(request, venue_id):
    try:
        venues_query = Venue.objects.get(id=venue_id)
    except HttpResponseNotFound:
        page_not_found(request, exception, template_name="errors/404.html")
    except HttpResponseServerError:
        server_error(request, template_name="errors/500.html")
    past_show_query = Show.objects.select_related("artist_id").filter(venue_id=venue_id).filter(
        start_time__lte=datetime.datetime.now()).all()

    past_show = []
    for past in past_show_query:
        past_show.append({
            "artist_id": past.artist_id.id,
            "artist_name": past.artist_id.name,
            "artist_image_link": past.artist_id.image_link,
            "StartTime": past.start_time.strftime('%Y-%m-%d %H:%M:%S')
        })
    upcoming_show_query = Show.objects.select_related("artist_id").filter(venue_id=venue_id).filter(
        start_time__gte=datetime.datetime.now()).all()
    upcoming_shows = []

    for show in upcoming_show_query:
        upcoming_shows.append({
            "artist_id": show.artist_id.id,
            "artist_name": show.artist_id.name,
            "artist_image_link": show.artist_id.image_link,
            "StartTime": show.start_time.strftime('%Y-%m-%d %H:%M:%S')
        })
    data = {
        "id": venues_query.id,
        "name": venues_query.name,
        "address": venues_query.address,
        "city": venues_query.city,
        "genres": venues_query.genres,
        "state": venues_query.state,
        "phone": venues_query.phone,
        "website": venues_query.website,
        "facebook_link": venues_query.facebook_link,
        "seeking_talent": venues_query.seekingTalent,
        "seeking_description": venues_query.seekingDescription,
        "image_link": venues_query.image_link,
        "past_shows": past_show,
        "upcoming_shows": upcoming_shows,
        "past_shows_count": len(past_show),
        "upcoming_shows_count": len(upcoming_shows),
    }
    print(venues_query.genres)
    return render(request, "pages/show_venue.html", {"venue": data, "venue_id": venue_id})


@csrf_exempt
def create_venue_form(request):
    try:
        venues_form = forms.VenueForm(request.POST or None)
        if venues_form.is_valid():
            name = venues_form.cleaned_data.get("name")
            city = venues_form.cleaned_data.get("city")
            state = venues_form.cleaned_data.get("state")
            address = venues_form.cleaned_data.get("address")
            phone = venues_form.cleaned_data.get("phone")
            genres = venues_form.cleaned_data.get("genres")
            facebook_link = venues_form.cleaned_data.get("facebook_link")
            image_link = venues_form.cleaned_data.get("image_link")
            website_link = venues_form.cleaned_data.get("website_link")
            seeking_talent = venues_form.cleaned_data.get("seeking_talent")
            seeking_description = venues_form.cleaned_data.get("seeking_description")
            new_venue = Venue.objects.create(name=name, city=city, state="".join(state), address=address,
                                             genres=" ".join(genres),
                                             phone=phone, facebook_link=facebook_link, image_link=image_link,
                                             website=website_link, seekingTalent=seeking_talent,
                                             seekingDescription=seeking_description)
            new_venue.save()
        return render(request, "forms/new_venue.html", {"form": venues_form})
    except HttpResponseNotFound:
        page_not_found(request, exception, template_name="errors/404.html")
    except HttpResponseServerError:
        server_error(request, template_name="errors/500.html")


@csrf_exempt
def delete_venue(request, venue_id):
    try:
        Venue.objects.filter(id=venue_id).delete()
    except:
        transaction.rollback()
    return redirect(request, "page/home.html")


@csrf_exempt
def edit_venue(request, venue_id):
    venues_form = forms.VenueForm(request.POST or None)
    venue = Venue.objects.get(id=venue_id)
    venue_data = {
        "id": venue_id,
        "name": venue.name
    }

    try:
        if venues_form.is_valid():
            name = venues_form.cleaned_data.get("name")
            city = venues_form.cleaned_data.get("city")
            state = venues_form.cleaned_data.get("state")
            genres = venues_form.cleaned_data.get("genres")
            address = venues_form.cleaned_data.get("address")
            phone = venues_form.cleaned_data.get("phone")
            facebook_link = venues_form.cleaned_data.get("facebook_link")
            image_link = venues_form.cleaned_data.get("image_link")
            website_link = venues_form.cleaned_data.get("website_link")
            seeking_talent = venues_form.cleaned_data.get("seeking_talent")
            seeking_description = venues_form.cleaned_data.get("seeking_description")
            if not name:
                pass
            else:
                venue.name = name

            venue.city = city
            venue.state = "".join(state)
            venue.genres = " ".join(genres)
            venue.address = address
            if not phone:
                pass
            else:
                venue.phone = phone

            if not facebook_link:
                pass
            else:
                venue.facebook_link = facebook_link

            if not image_link:
                pass
            else:
                venue.image_link = image_link

            if not website_link:
                pass
            else:
                venue.website = website_link

            if not seeking_description:
                pass
            else:
                venue.seekingDescription = seeking_description
            venue.seekingTalent = seeking_talent
            venue.save()
        return render(request, "forms/edit_venue.html", {"form": venues_form, "venue": venue_data})

    except HttpResponseNotFound:

        page_not_found(request, exception, template_name="errors/404.html")

    except HttpResponseServerError:

        server_error(request, template_name="errors/500.html")


# Artist
@csrf_exempt
def artist(request):
    try:
        artists = Artist.objects.all()
        return render(request, "pages/artists.html", {"artists": artists})
    except HttpResponseNotFound:
        page_not_found(request, exception, template_name="errors/404.html")
    except HttpResponseServerError:
        server_error(request, template_name="errors/500.html")


@csrf_exempt
def search_artist(request):
    try:
        count = 0
        data = []
        if request.method == "POST":
            search = request.POST["search_term"]
            artist_search = Artist.objects.filter(name__icontains=search).all()
            count = Artist.objects.filter(name__icontains=search).all().count()

            for searched in artist_search:
                data.append({
                    "id": searched.id,
                    "name": searched.name,
                    "num_upcoming_shows": count

                })
        response = {
            "count": count,
            "data": data
        }

        return render(request, "pages/search_artists.html", {"results": response})
    except HttpResponseNotFound:
        page_not_found(request, exception, template_name="errors/404.html")
    except HttpResponseServerError:
        server_error(request, template_name="errors/500.html")


@csrf_exempt
def show_artist(request, artist_id):
    try:
        artist_query = Artist.objects.get(id=artist_id)
        if not artist_query:
            return render(request, "errors/404.html")
        past_show_query = Show.objects.select_related("venue_id").filter(artist_id=artist_id).filter(
            start_time__lte=datetime.datetime.now()).all()
        past_show = []
        for past in past_show_query:
            past_show.append({
                "venue_id": past.venue_id.id,
                "venue_name": past.venue_id.name,
                "venue_image_link": past.venue_id.image_link,
                "StartTime": past.start_time
            })
        upcoming_show_query = Show.objects.select_related("venue_id").filter(artist_id=artist_id).filter(
            start_time__gte=datetime.datetime.now()).all()
        upcoming_shows = []

        for show in upcoming_show_query:
            upcoming_shows.append({
                "venue_id": show.venue_id.id,
                "venue_name": show.venue_id.name,
                "venue_image_link": show.venue_id.image_link,
                "start_time": show.start_time
            })
        data = {
            "id": artist_query.id,
            "name": artist_query.name,
            "genres": str(artist_query.genres),
            "city": artist_query.city,
            "state": artist_query.state,
            "phone": artist_query.phone,
            "website": artist_query.website,
            "facebook_link": artist_query.facebook_link,
            "seeking_venue": artist_query.seekingVenue,
            "seeking_description": artist_query.seekingDescription,
            "image_link": artist_query.image_link,
            "past_shows": past_show,
            "upcoming_shows": upcoming_shows,
            "past_shows_count": len(past_show),
            "upcoming_shows_count": len(upcoming_shows),
        }

        return render(request, "pages/show_artist.html", {"artist": data})
    except HttpResponseNotFound:
        page_not_found(request, exception, template_name="errors/404.html")
    except HttpResponseServerError:
        server_error(request, template_name="errors/500.html")


@csrf_exempt
def create_artist_form(request):
    try:
        artist_form = forms.ArtistForm(request.POST or None)
        if artist_form.is_valid():
            name = artist_form.cleaned_data.get("name")
            city = artist_form.cleaned_data.get("city")
            state = artist_form.cleaned_data.get("state")
            genres = artist_form.cleaned_data.get("genres")
            facebook_link = artist_form.cleaned_data.get("facebook_link")
            image_link = artist_form.cleaned_data.get("image_link")
            website_link = artist_form.cleaned_data.get("website_link")
            seeking_venue = artist_form.cleaned_data.get("seeking_talent")
            seeking_description = artist_form.cleaned_data.get("seeking_description")
            new_artist = Artist(name=name, city=city, genres=" ".join(genres), state="".join(state),
                                facebook_link=facebook_link, image_link=image_link,
                                seekingVenue=seeking_venue, website=website_link,
                                seekingDescription=seeking_description)
            new_artist.save()
        return render(request, "forms/new_artist.html", {"form": artist_form})
    except HttpResponseNotFound:
        page_not_found(request, exception, template_name="errors/404.html")
    except HttpResponseServerError:
        server_error(request, template_name="errors/500.html")


@csrf_exempt
def edit_artist(request, artist_id):
    try:
        artist_form = forms.ArtistForm(request.POST or None)
        artist = Artist.objects.get(id=artist_id)
        artist_data = {
            "id": artist_id,
            "name": artist.name
        }
        if artist_form.is_valid():
            name = artist_form.cleaned_data.get("name")
            city = artist_form.cleaned_data.get("city")
            state = artist_form.cleaned_data.get("state")
            phone = artist_form.cleaned_data.get("phone")
            genres = artist_form.cleaned_data.get("genres")
            facebook_link = artist_form.cleaned_data.get("facebook_link")
            image_link = artist_form.cleaned_data.get("image_link")
            website_link = artist_form.cleaned_data.get("website_link")
            seeking_venue = artist_form.cleaned_data.get("seeking_venue")
            seeking_description = artist_form.cleaned_data.get("seeking_description")
            artist.name = name
            artist.city = city
            artist.state = "".join(state)
            artist.genres = " ".join(genres)

            if not phone:
                pass
            else:
                artist.phone = phone

            if not facebook_link:
                pass
            else:
                artist.facebook_link = facebook_link

            if not image_link:
                pass
            else:
                artist.image_link = image_link

            if not website_link:
                pass
            else:
                artist.website = website_link

            if not seeking_description:
                pass
            else:
                artist.seekingDescription = seeking_description

            artist.seekingVenue = seeking_venue
            if not seeking_description:
                pass
            else:
                artist.seekingDescription = seeking_description
            artist.save()

        return render(request, "forms/edit_artist.html", {"form": artist_form, "artist": artist_data})
    except HttpResponseNotFound:
        page_not_found(request, exception, template_name="errors/404.html")
    except HttpResponseServerError:
        server_error(request, template_name="errors/500.html")


# Shows

@csrf_exempt
def shows(request):
    try:
        show_query = Show.objects.select_related("artist_id").all()
        data = []

        for show in show_query:
            artist_show = Artist.objects.get(id=show.artist_id.id)
            venue_show = Venue.objects.get(id=show.venue_id.id)
            data.append({
                "artist_id": artist_show.id,
                "artist_name": artist_show.name,
                "artist_image_link": artist_show.image_link,
                "venue_id": venue_show.id,
                "venue_name": venue_show.name,
                "start_time": show.start_time,
            })
        return render(request, "pages/shows.html", {"shows": data})
    except HttpResponseNotFound:
        page_not_found(request, exception, template_name="errors/404.html")
    except HttpResponseServerError:
        server_error(request, template_name="errors/500.html")


@csrf_exempt
def create_shows(request):
    try:
        shows_form = forms.ShowForm(request.POST or None)
        if shows_form.is_valid():
            artist_id = shows_form.cleaned_data.get("artist_id")
            venue_id = shows_form.cleaned_data.get("venue_id")
            start_time = shows_form.cleaned_data.get("start_time")
            artist = Artist.objects.get(id=int(artist_id))
            venue = Venue.objects.get(id=int(venue_id))
            aid = artist.id
            vid = venue.id
            new_show = Show()
            new_show.start_time = start_time
            new_show.artist_id_id = aid
            new_show.venue_id_id = vid
            new_show.save()
        return render(request, "forms/new_show.html", {"form": shows_form})
    except HttpResponseNotFound:
        page_not_found(request, exception, template_name="errors/404.html")
    except HttpResponseServerError:
        server_error(request, template_name="errors/500.html")


def not_found_error(request, *args, **kwargs):
    return render(request, 'errors/404.html', status=404)


def server_error(request, *args, **kwargs):
    return render(request, 'errors/500.html', status=500)
