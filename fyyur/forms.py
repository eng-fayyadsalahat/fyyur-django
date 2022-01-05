import datetime
from django import forms
from django.core.validators import RegexValidator

Genres_Choices = [
    ('Alternative', 'Alternative'),
    ('Blues', 'Blues'),
    ('Classical', 'Classical'),
    ('Country', 'Country'),
    ('Electronic', 'Electronic'),
    ('Folk', 'Folk'),
    ('Funk', 'Funk'),
    ('Hip-Hop', 'Hip-Hop'),
    ('Heavy Metal', 'Heavy Metal'),
    ('Instrumental', 'Instrumental'),
    ('Jazz', 'Jazz'),
    ('Musical Theatre', 'Musical Theatre'),
    ('Pop', 'Pop'),
    ('Punk', 'Punk'),
    ('R&B', 'R&B'),
    ('Reggae', 'Reggae'),
    ('Rock n Roll', 'Rock n Roll'),
    ('Soul', 'Soul'),
    ('Other', 'Other'),
]
State_Choices = [
    ('AL', 'AL'),
    ('AK', 'AK'),
    ('AZ', 'AZ'),
    ('AR', 'AR'),
    ('CA', 'CA'),
    ('CO', 'CO'),
    ('CT', 'CT'),
    ('DE', 'DE'),
    ('DC', 'DC'),
    ('FL', 'FL'),
    ('GA', 'GA'),
    ('HI', 'HI'),
    ('ID', 'ID'),
    ('IL', 'IL'),
    ('IN', 'IN'),
    ('IA', 'IA'),
    ('KS', 'KS'),
    ('KY', 'KY'),
    ('LA', 'LA'),
    ('ME', 'ME'),
    ('MT', 'MT'),
    ('NE', 'NE'),
    ('NV', 'NV'),
    ('NH', 'NH'),
    ('NJ', 'NJ'),
    ('NM', 'NM'),
    ('NY', 'NY'),
    ('NC', 'NC'),
    ('ND', 'ND'),
    ('OH', 'OH'),
    ('OK', 'OK'),
    ('OR', 'OR'),
    ('MD', 'MD'),
    ('MA', 'MA'),
    ('MI', 'MI'),
    ('MN', 'MN'),
    ('MS', 'MS'),
    ('MO', 'MO'),
    ('PA', 'PA'),
    ('RI', 'RI'),
    ('SC', 'SC'),
    ('SD', 'SD'),
    ('TN', 'TN'),
    ('TX', 'TX'),
    ('UT', 'UT'),
    ('VT', 'VT'),
    ('VA', 'VA'),
    ('WA', 'WA'),
    ('WV', 'WV'),
    ('WI', 'WI'),
    ('WY', 'WY'),
]


class VenueForm(forms.Form):
    name = forms.CharField(
        label='name', required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Venue',
                "autofocus": "true"
            }
        ))
    city = forms.CharField(
        label='city', required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'City',
                "autofocus": "true"
            }
        )
    )
    state = forms.CharField(label='state', required=True,
                            widget=forms.Select(attrs={
                                'class': 'form-control',
                                'placeholder': 'State',
                                "autofocus": "true"
                            }, choices=State_Choices))
    address = forms.CharField(
        label='address',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Address',
                "autofocus": "true"
            }
        )
    )
    phone = forms.CharField(
        label='phone',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'xxx-xxx-xxxx',
                "autofocus": "true"
            }, )
    )
    image_link = forms.URLField(
        label='image_link',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'http://',
                "autofocus": "true"
            }
        )
    )

    genres = forms.MultipleChoiceField(label='genres', required=True,
                                       widget=forms.SelectMultiple(
                                           attrs={
                                               'class': 'form-control',
                                               'placeholder': 'Genres, separated by commas',
                                               "autofocus": "true"
                                           }),
                                       choices=Genres_Choices)
    facebook_link = forms.URLField(
        label='facebook_link', required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'http://',
                "autofocus": "true"
            }
        )
    )
    website_link = forms.URLField(
        label='website_link', required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'http://',
                "autofocus": "true"
            }
        )
    )

    seeking_talent = forms.BooleanField(label='seeking_talent', required=False,
                                        widget=forms.CheckboxInput(
                                            attrs={
                                                'class': 'form-control',
                                                'placeholder': 'Talent',
                                                "autofocus": "true"
                                            }
                                        )

                                        )

    seeking_description = forms.CharField(
        label='seeking_description', required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Description',
                "autofocus": "true"
            }
        )
    )


class ShowForm(forms.Form):
    artist_id = forms.IntegerField(
        label='artist_id', required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "autofocus": "true"
            }
        )
    )
    venue_id = forms.IntegerField(
        label='venue_id', required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "autofocus": "true"
            }
        )
    )
    start_time = forms.CharField(
        label='start_time',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD HH:MM',
                "autofocus": "true"
            }
        )
    )


class ArtistForm(forms.Form):
    name = forms.CharField(
        label='name', required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Artist',
                "autofocus": "true"
            }
        )
    )
    city = forms.CharField(
        label='City', required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'City',
                "autofocus": "true"
            }
        )
    )
    state = forms.CharField(
        label='State', required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'State',
                "autofocus": "true"
            }, choices=State_Choices
        )

    )
    phone = forms.CharField(
        label='Phone', required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'xxx-xxx-xxxx',
                "autofocus": "true"
            }
        )
    )
    image_link = forms.URLField(
        label='ImageLink',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'http://',
                "autofocus": "true"
            }
        )
    )
    genres = forms.MultipleChoiceField(label='genres', required=True,
                                       widget=forms.SelectMultiple(attrs={
                                           'class': 'form-control',
                                           'placeholder': 'Genres, separated by commas',
                                           "autofocus": "true"
                                       }),
                                       choices=Genres_Choices)

    facebook_link = forms.URLField(
        label='FacebookLink', required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'http://',
                "autofocus": "true"
            }
        )
    )

    website_link = forms.URLField(
        label='Website', required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'http://',
                "autofocus": "true"
            }
        )
    )

    seeking_talent = forms.BooleanField(label='seeking_talent', required=False,
                                        widget=forms.CheckboxInput(
                                            attrs={
                                                'class': 'form-control',
                                                'placeholder': 'Venue Talent',
                                                "autofocus": "true"
                                            }
                                        ))

    seeking_description = forms.CharField(
        label='SeekingDescription', required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Description',
                "autofocus": "true"
            }
        )
    )
