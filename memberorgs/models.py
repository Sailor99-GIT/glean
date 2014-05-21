from django.db import models

from counties.models import County

from django import forms
from django.contrib.auth.models import User

from django.contrib import admin
from constants import STATES, LINE_TYPE, ACCESS_LEVELS, COLORS
# Create your models here.


class MemOrg(models.Model):
    name = models.CharField(max_length=200)
    website = models.CharField('Website', max_length=50, blank=True, null=True)
    description = models.TextField('Description', blank=True, null=True)
    counties = models.ManyToManyField(County, related_name="member_organizations", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    volunteers = models.ManyToManyField(
        User, editable=False, related_name="member_organizations")

    color = models.CharField(
        'Color', choices=COLORS, max_length=20, default='muted')

    address_one = models.CharField(
        'Physical Address (line one)', max_length=30, blank=True, null=True)
    address_two = models.CharField(
        'Physical Address (line two)', max_length=30, blank=True, null=True)
    city = models.CharField('City', max_length=15, blank=True, null=True)
    state = models.CharField(
        "State", choices=STATES, default="VT", max_length=2, blank=True)
    zipcode = models.CharField(
        "Zipcode", max_length=11, blank=True, null=True)
    physical_is_mailing = models.BooleanField(
        'Physical Address is Mailing Address', default=True)

    mailing_address_one = models.CharField(
        'Mailing Address (line one)', max_length=200, blank=True)
    mailing_address_two = models.CharField(
        'Mailing Address (line two)', max_length=200, blank=True)
    mailing_city = models.CharField(
        'Mailing Address (City)', max_length=200, blank=True)
    mailing_state = models.CharField(
        'Mailing Address (State)', choices=STATES, max_length=2, blank=True)
    mailing_zip = models.CharField(
        'Mailing Address Zipcode', max_length=11, blank=True)

    phone_1 = models.CharField(
        'Primary phone', max_length=200, blank=True)
    phone_1_type = models.CharField(
        'Primary Phone Type', choices=LINE_TYPE, max_length=10, blank=True)
    phone_2 = models.CharField(
        'Secondary phone', max_length=200, blank=True)
    phone_2_type = models.CharField(
        'Secondary Phone Type', choices=LINE_TYPE, max_length=10, blank=True)

    first_name = models.CharField(
        "Executive Director First Name", max_length=20, blank=True)
    last_name = models.CharField(
        "Executive Director Last Name", max_length=20, blank=True)
    phone = models.CharField(
        "Director's Direct Phone Number", max_length=15, blank=True, null=True)

    notify = models.BooleanField(
        'Notify on New Volunteer Signup?', default=False)

    testing = models.BooleanField(
        "Relay Announcement Emails to Testing Address", default=True)

    testing_email = models.CharField(
        "Primary Email Address", max_length="200", blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        permissions = (
            ("auth", "Member Organization Level Permissions"),
            ("uniauth", "Universal Permission Level"),
        )


class MemOrgForm(forms.ModelForm):
    class Meta:
        model = MemOrg


class NewAdminForm(forms.Form):
    member_organization = forms.ModelChoiceField(
        queryset=MemOrg.objects.all(), empty_label=None)
    access_level = forms.ChoiceField(choices=ACCESS_LEVELS, required=False)
    username = forms.CharField(max_length=20, required=False)
    password = forms.CharField(max_length=50, required=False)
    verify = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(required=False)
    first_name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=20, required=False)
    phone = forms.CharField(max_length=20, required=False)

admin.site.register(MemOrg)
