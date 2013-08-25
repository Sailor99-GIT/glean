from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from userprofile.models import Profile
from announce.models import Template
from farms.models import Farm, FarmLocation, Contact
from memberorgs.models import MemOrg
from recipientsite.models import RecipientSite
from announce.models import Announcement
from distro.models import Distro
from counties.models import County
from gleanevent.models import GleanEvent, PostGlean
from posts.models import Post
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# Create your views here.


def create(request):
	if request.user.is_superuser and not Group.objects.all():
		vol = Group(name="Volunteer")
		vol.save()
		ed = Group(name="Member Organization Executive Director")
		ed.save()
		mc = Group(name="Member Organization Glean Coordinator")
		mc.save()
		sal = Group(name="Salvation Farms Administrator")
		sal.save()
		salc = Group(name="Salvation Farms Coordinator")
		salc.save()

	else:
		return HttpResponseRedirect(reverse('home'))

	ed = Group.objects.get(name="Member Organization Executive Director")
	if not ed.permissions.all():

		mo_list = [Announcement, Template, Distro, GleanEvent, Farm, PostGlean, RecipientSite, Profile, MemOrg, Post]
		uni_list = [Announcement, Template, Distro, GleanEvent, Farm, FarmLocation, Contact, PostGlean, RecipientSite, Profile, MemOrg, County, Post]

		mc = Group.objects.get(name="Member Organization Glean Coordinator")
		sal = Group.objects.get(name="Salvation Farms Administrator")
		salc = Group.objects.get(name="Salvation Farms Coordinator")

		## --- add the memorg permissions -- ##
		for model in mo_list:
			content_type = ContentType.objects.get_for_model(model)
			perm = Permission.objects.get(codename='auth', content_type=content_type)
			ed.permissions.add(perm)
			mc.permissions.add(perm)
			sal.permissions.add(perm)
			salc.permissions.add(perm)

		## -- add the sal farms permissions -- ##
		for model in uni_list:
			content_type = ContentType.objects.get_for_model(model)
			perm = Permission.objects.get(codename='uniauth', content_type=content_type)
			sal.permissions.add(perm)
			salc.permissions.add(perm)

		## --- basically shortchange the MemC --- ##
		content_type = ContentType.objects.get_for_model(Profile)
		perm = Permission.objects.get(codename='promote', content_type=content_type)
		ed.permissions.add(perm)
		sal.permissions.add(perm)
		salc.permissions.add(perm)
		## --- end shortchanging --- ##

	if not MemOrg.objects.all():
		new_memorg = MemOrg(name="Salvation Farms")
		new_memorg.save()
		new_memorg.volunteers.add(request.user)


	return HttpResponse('it worked from scratch')	
	return HttpResponseRedirect(reverse('home'))