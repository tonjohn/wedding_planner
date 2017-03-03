from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import PhoneNumberField, USPostalCodeField, USStateField, USZipCodeField
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import *


# Create your models here.
class Wedding(models.Model):
	title = models.CharField( max_length=50 )
	bride = models.ForeignKey(User, related_name="bride_in")
	groom = models.ForeignKey(User, related_name="groom_in")
	hashtag = models.CharField(max_length=50)
	email = models.EmailField()
	budget = models.IntegerField()
	max_guests = models.IntegerField()
	event_date = models.DateTimeField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
	created_at = models.DateTimeField(auto_now_add=True, editable=False )
	updated_at = models.DateTimeField(auto_now=True, editable=False)


class Household(models.Model):
	title = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	address2 = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = USStateField()
	zip = USZipCodeField()
	created_at = models.DateTimeField( auto_now_add=True )
	updated_at = models.DateTimeField( auto_now=True )


class Guest(models.Model):
	ADULT = 1
	TEEN = 2
	CHILD = 3
	BABY = 0
	AGE_CHOICES = (
		(ADULT, 'Adult(21+)'),
		(TEEN, 'Teenager'),
		(CHILD, 'Child'),
		(BABY, 'Infant/Toddler')
	)

	MISC = 0
	BRIDE_FAMILY = 1
	GROOM_FAMILY = 2
	BRIDE_FRIEND = 3
	GROOM_FRIEND = 4
	MUTUAL_FRIEND = 5

	RELATIONSHIP_CHOICES = (
		(BRIDE_FAMILY, 'Bride Family'),
		(GROOM_FAMILY, 'Groom Family'),
		(BRIDE_FRIEND, 'Bride Friend'),
		(GROOM_FRIEND, 'Groom Friend'),
		(MUTUAL_FRIEND, 'Mutual Friend'),
		(MISC, 'Other')
	)

	first_name = models.CharField(max_length=50, validators=[MinLengthValidator(1)])
	last_name = models.CharField(max_length=50)
	nickname = models.CharField( max_length=255 )
	age_group = models.SmallIntegerField(choices=AGE_CHOICES, default=ADULT,)
	email = models.EmailField()
	relationship = models.SmallIntegerField(choices=RELATIONSHIP_CHOICES, default=MISC,)
	visibility = models.SmallIntegerField()
	user = models.ForeignKey(User)
	household = models.ForeignKey(Household)
	wedding = models.ForeignKey(Wedding)
	tier = models.SmallIntegerField(default=10)
	position = models.IntegerField()
	created_at = models.DateTimeField( auto_now_add=True )
	updated_at = models.DateTimeField( auto_now=True )


class SuggestedGuest(models.Model):
	guest = models.ForeignKey(Guest)
	suggested_by = models.ForeignKey(User, related_name="suggested_guests")
	approved_by = models.ForeignKey(User, related_name="approved_guests")
	created_at = models.DateTimeField( auto_now_add=True )
	updated_at = models.DateTimeField( auto_now=True )


class WeddingParty(models.Model):
	user = models.ForeignKey(User)
	role = models.IntegerField()
	# permissions = models.BinaryField()

# class GuestList(models.Model)
# 	wedding
# 	guest
# 	family
# 	tier

# class Budget