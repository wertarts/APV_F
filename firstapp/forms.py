from django.forms import ModelForm
from .models import Person, Location, Contact, Contact_type, Relation_type, Relation, Person_meeting, Meeting
from django import forms


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    years = range(1900, 2018, 1)
    birth_day = forms.DateField(
        widget=forms.SelectDateWidget(years=years)
    )


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactTypeForm(ModelForm):
    class Meta:
        model = Contact_type
        fields = '__all__'


class RelationTypeForm(ModelForm):
    class Meta:
        model = Relation_type
        fields = '__all__'


class RelationForm(ModelForm):
    class Meta:
        model = Relation
        fields = '__all__'


class Person_meetingForm(ModelForm):
    class Meta:
        model = Person_meeting
        fields = '__all__'


class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'

    years = range(1900, 2018, 1)
    start_date = forms.DateField(
        widget=forms.SelectDateWidget(years=years)
    )

