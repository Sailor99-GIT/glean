from django.db import models
from django.forms import ModelForm

from django.contrib.auth.models import User

from gleanevent.models import GleanEvent
from memberorgs.models import MemOrg


class Template(models.Model):
	template_name = models.CharField(max_length=40)
	member_organization = models.ForeignKey(MemOrg, editable=False)
	body = models.TextField()
	def __unicode__(self):
		return self.member_organization.name + ' - ' + self.template_name

class TemplateForm(ModelForm):
	class Meta:
		model = Template

class PartialTemplateForm(ModelForm):
	class Meta:
		model = Template
		exclude = ('template_name')

class Announcement(models.Model):
	email_recipients = models.ManyToManyField(User, null=True, blank=True, related_name="invitees", editable=False)
	phone_recipients = models.ManyToManyField(User, null=True, blank=True, related_name="Phone List", editable=False)
	datetime = models.DateTimeField(auto_now_add=True, editable=False)
	glean = models.ForeignKey(GleanEvent, blank=True, null=True, editable=False)
	title = models.CharField(max_length=50)
	message = models.TextField()
	template = models.ForeignKey(Template, blank=True, null=True)
	sent = models.BooleanField(default=False, editable=False)
	sent_by = models.ForeignKey(User, editable=False, null=True)

	def __unicode__(self):
		return self.datetime.strftime('%y:%m:%d %H:%M:%S') + ' ' + self.glean.title + ' ' + self.title

class AnnouncementForm(ModelForm):
	class Meta:
		model = Announcement

class RsvpModel(models.Model):
	key = models.CharField(max_length=25, primary_key=True)
	user = models.ForeignKey(User)
	created = models.DateTimeField(auto_now_add=True)

class UnsubscribeModel(models.Model):
	key = models.CharField(max_length=25, primary_key=True)
	user = models.ForeignKey(User)