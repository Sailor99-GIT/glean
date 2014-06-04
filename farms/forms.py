import sys
from django import forms
from django.forms import ModelForm
from django.forms.fields import ChoiceField
from crispy_forms.bootstrap import (FieldWithButtons,
                                    InlineCheckboxes,
                                    StrictButton,
                                    AppendedText)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Layout,
                                 Fieldset,
                                 ButtonHolder,
                                 Field,
                                 Row,
                                 Submit,
                                 Div,
                                 HTML)
from constants import STATES, COLORS, LINE_TYPE
from farms.models import Farm
from counties.models import County
from memberorgs.models import MemOrg


class FarmForm(ModelForm):
    class Meta:
        model = Farm
        exclude = ['farmers']


class NewFarmForm(ModelForm):
    'A crispyform class for creating a new farm object'
    
    version = '0.1'

    def __init__(self, *args, **kwargs):
        super(NewFarmForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_errors = False
        self.helper.form_id = "id-New-Farm-Form"
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Fieldset(
                "",
                Div(
                    Row("name"),
                    Row("address_one", "address_two"),
                    Row("city", "state"),
                    Row("zipcode"),
                    "directions",
                    "instructions",
                    "counties",
                    css_class="crispy_column_left"),
                Div(
                    HTML("<i style='color: red;'>Information in this column is visable only by administrators</i>"),
                    "physical_is_mailing",
                    Row("mailing_address_one", "mailing_address_two"),
                    Row("mailing_city", "mailing_state"),
                    "mailing_zip",
                    "description",
                    Row("phone_1", "phone_1_type"),
                    Row("phone_2", "phone_2_type"),
                    "email",
                    css_class="crispy_column_left yellow-left")
            ),
            HTML("</div>"),
            HTML("<input type='submit' "
                 "class='glean-button green-button' "
                 "name='submit' value='Add Farm'>"),
            HTML("</div>")
        )

    name = forms.CharField(max_length=200)
    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(
            attrs={'cols': '100', 'rows': '10', 'style': 'width: 450px'}),
        required=False)
    address_one = forms.CharField(label='Address:', max_length=200)
    address_two = forms.CharField(label='Address (line two):', max_length=200, required=False)
    city = forms.CharField(label='City:', max_length=200)
    state = forms.ChoiceField(
        label="State", choices=STATES, required=False)
    zipcode = forms.CharField(label='Zip Code:', max_length=11)
    
    physical_is_mailing = forms.BooleanField(label='Physical Address is Mailing Address', required=False)
    mailing_address_one = forms.CharField(label='Address: ', max_length=200, required=False)
    mailing_address_two = forms.CharField(label='Address (line two):', max_length=200, required=False)
    mailing_city = forms.CharField(label='City:', max_length=200, required=False)
    mailing_state = forms.ChoiceField(
        label="State", choices=STATES, required=False)
    mailing_zip = forms.CharField(label='Zip Code:', max_length=11, required=False)

    phone_1 = forms.CharField(label='Primary phone #:', max_length=200)
    phone_1_type = forms.ChoiceField(
        label='Primary Phone Type', choices=LINE_TYPE, required=False)
    phone_2 = forms.CharField(label='Secondary phone #:', max_length=200, required=False)
    phone_2_type = forms.ChoiceField(
        label='Primary Phone Type', choices=LINE_TYPE, required=False)
    email = forms.CharField(label="Email:")
    directions = forms.CharField(
        label='Directions:',
        widget=forms.Textarea(
            attrs={'cols': '100', 'rows': '10', 'style': 'width: 450px'}),
        required=False)
    instructions = forms.CharField(
        label='Instructions:',
        widget=forms.Textarea(
            attrs={'cols': '100', 'rows': '10', 'style': 'width: 450px'}),
        required=False)
    counties = forms.ModelChoiceField(label="County", queryset=County.objects.all())
    member_organization = forms.ModelMultipleChoiceField(label="member_organization", queryset=MemOrg.objects.all(), required=False)

    class Meta:
        model = Farm
        exclude = ("farmers")


class EditFarmForm(ModelForm):
    'A crispyform class for editing a farm object'
    
    version = '0.1'

    def __init__(self, *args, **kwargs):
        super(EditFarmForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_errors = False
        self.helper.form_id = "id-New-Farm-Form"
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Fieldset(
                "",
                Div(
                    Row("name"),
                    Row("address_one", "address_two"),
                    Row("city", "state"),
                    Row("zipcode"),
                    "directions",
                    "instructions",
                    "counties",
                    css_class="crispy_column_left"),
                Div(
                    HTML("<i style='color: red;'>Information in this column is visable only by administrators</i>"),
                    "physical_is_mailing",
                    Row("mailing_address_one", "mailing_address_two"),
                    Row("mailing_city", "mailing_state"),
                    "mailing_zip",
                    "description",
                    Row("phone_1", "phone_1_type"),
                    Row("phone_2", "phone_2_type"),
                    "email",
                    css_class="crispy_column_left yellow-left")
            ),
            HTML("</div>"),
            HTML("<input type='submit' "
                 "class='glean-button green-button' "
                 "name='submit' value='Save Changes'>"),
            HTML("</div>")
        )

    name = forms.CharField(max_length=200)
    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(
            attrs={'cols': '100', 'rows': '10', 'style': 'width: 450px'}),
        required=False)
    address_one = forms.CharField(label='Address:', max_length=200)
    address_two = forms.CharField(label='Address (line two):', max_length=200, required=False)
    city = forms.CharField(label='City:', max_length=200)
    state = forms.ChoiceField(
        label="State", choices=STATES, required=False)
    zipcode = forms.CharField(label='Zip Code:', max_length=11)
    
    physical_is_mailing = forms.BooleanField(label='Physical Address is Mailing Address', required=False)
    mailing_address_one = forms.CharField(label='Address: ', max_length=200, required=False)
    mailing_address_two = forms.CharField(label='Address (line two):', max_length=200, required=False)
    mailing_city = forms.CharField(label='City:', max_length=200, required=False)
    mailing_state = forms.ChoiceField(
        label="State", choices=STATES, required=False)
    mailing_zip = forms.CharField(label='Zip Code:', max_length=11, required=False)

    phone_1 = forms.CharField(label='Primary phone #:', max_length=200)
    phone_1_type = forms.ChoiceField(
        label='Primary Phone Type', choices=LINE_TYPE, required=False)
    phone_2 = forms.CharField(label='Secondary phone #:', max_length=200, required=False)
    phone_2_type = forms.ChoiceField(
        label='Primary Phone Type', choices=LINE_TYPE, required=False)
    email = forms.CharField(label="Email:")
    directions = forms.CharField(
        label='Directions:',
        widget=forms.Textarea(
            attrs={'cols': '100', 'rows': '10', 'style': 'width: 450px'}),
        required=False)
    instructions = forms.CharField(
        label='Instructions:',
        widget=forms.Textarea(
            attrs={'cols': '100', 'rows': '10', 'style': 'width: 450px'}),
        required=False)
    counties = forms.ModelChoiceField(label="County", queryset=County.objects.all())
    member_organization = forms.ModelMultipleChoiceField(label="member_organization", queryset=MemOrg.objects.all(), required=False)

    class Meta:
        model = Farm
        exclude = ("farmers","member_organization")