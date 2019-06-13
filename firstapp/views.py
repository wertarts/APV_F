from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Person, Contact, Contact_type, Location, Relation_type, Relation, Meeting, Person_meeting

from .forms import PersonForm, LocationForm, ContactForm, ContactTypeForm, \
    RelationTypeForm, RelationForm, Person_meetingForm, MeetingForm

""" Persons """


def show_persons(request):
    return render(request, "index.html", {'persons': Person.objects.all()})


def edit_person(request, person_id):
    person = get_object_or_404(Person, id_person=person_id)

    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('persons'))
    else:
        form = PersonForm(instance=person)

    return render(request, "edit_person.html", {'form': form, 'title': 'Edit Person'})


def add_person(request):
    if request.method == 'POST':
        print(request)
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('persons'))
    else:
        form = PersonForm()
    return render(request, "edit_person.html", {'form': form, 'title': 'Add Person'})


def delete_person(request, person_id):
    person = Person.objects.get(id_person=person_id)
    person.delete()
    return HttpResponseRedirect(reverse('persons'))


"""End Persons
=========================================================================================================
Locations"""


def location(request, location_id):
    location = get_object_or_404(Location, id_location=location_id)
    return render(request, "location.html", {'location': location})


def show_location(request):
    return render(request, "locations.html", {'locations': Location.objects.all()})


def edit_location(request, id_location):
    location = get_object_or_404(Location, id_location=id_location)

    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('locations'))
    else:
        form = LocationForm(instance=location)

    return render(request, "edit_location.html", {'form': form, 'title': 'Edit Location'})


def add_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('locations'))
    else:
        form = LocationForm()
    return render(request, "edit_location.html", {'form': form, 'title': 'Add Location'})


def delete_location(request, id_location):
    location = Location.objects.get(id_location=id_location)
    location.delete()
    return HttpResponseRedirect(reverse('locations'))


"""End Locations
=========================================================================================================
Meeting"""


def show_meetings(request):
    return render(request, "meetings.html", {'meetings': Meeting.objects.all()})


def edit_meeting(request, id_meeting):
    meeting = get_object_or_404(Meeting, id_meeting=id_meeting)

    if request.method == 'POST':
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
        else:
            print(request.body)
            return HttpResponseRedirect(reverse('meetings'))
    else:
        form = MeetingForm(instance=meeting)

    return render(request, "edit_meeting.html", {'form': form, 'title': 'Edit Meeting'})


def add_meeting(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('meetings'))
    else:
        form = MeetingForm()
    return render(request, "edit_meeting.html", {'form': form, 'title': 'Add Meeting'})


def delete_meeting(request, id_meeting):
    meet = Meeting.objects.get(id_meeting=id_meeting)
    meet.delete()
    return HttpResponseRedirect(reverse('meetings'))


"""End Meetings
=========================================================================================================
Persons <=> Meeting"""


def show_person_meetings(request):
    return render(request, "person_meetings.html", {'person_meetings': Person_meeting.objects.all()})


def edit_person_meeting(request, id_person_meeting):
    pm = get_object_or_404(Person_meeting, pk=id_person_meeting)

    if request.method == 'POST':
        form = Person_meetingForm(request.POST, instance=pm)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('person_meetings'))
    else:
        form = Person_meetingForm(instance=pm)

    return render(request, "edit_person_meeting.html", {'form': form, 'title': 'Edit Person Meeting'})


def add_person_meeting(request):
    if request.method == 'POST':
        form = Person_meetingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('person_meetings'))
    else:
        form = Person_meetingForm()
    return render(request, "edit_person_meeting.html", {'form': form, 'title': 'Add Person Meeting'})


def delete_person_meeting(request, id_person_meeting):
    pm = Person_meeting.objects.get(pk=id_person_meeting)
    pm.delete()
    return HttpResponseRedirect(reverse('person_meetings'))


def show_my_person_meetings(request, id_person):
    person_meetings = Person_meeting.objects.filter(id_person__id_person=id_person)
    return render(request, "person_meetings.html", {'person_meetings': person_meetings})


def show_contacts(request):
    return render(request, "contacts.html", {'contacts': Contact.objects.all()})


def edit_contact(request, id_contact):
    contact = get_object_or_404(Contact, id_contact=id_contact)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('contacts'))
    else:
        form = ContactForm(instance=contact)

    return render(request, "edit_contact.html", {'form': form, 'title': 'Edit Contact'})


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('contacts'))
    else:
        form = ContactForm()
    return render(request, "edit_contact.html", {'form': form, 'title': 'Add Contact'})


def delete_contact(request, id_contact):
    contact = Contact.objects.get(id_contact=id_contact)
    contact.delete()
    return HttpResponseRedirect(reverse('contacts'))


def person_contacts(request, id_person):
    return render(request, "contacts.html", {'contacts': Contact.objects.filter(id_person__id_person=id_person)})


"""End Persons <=> Meeting
=========================================================================================================
Contacts"""


def show_contacts_type(request):
    return render(request, "contacts_type.html", {'contacts_type': Contact_type.objects.all()})


def edit_contact_type(request, id_contact_type):
    ct = get_object_or_404(Contact_type, id_contact_type=id_contact_type)

    if request.method == 'POST':
        form = ContactTypeForm(request.POST, instance=ct)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('contacts_type'))
    else:
        form = ContactTypeForm(instance=ct)

    return render(request, "edit_contact_type.html", {'form': form, 'title': 'Edit Contact Type'})


def add_contact_type(request):
    if request.method == 'POST':
        form = ContactTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('contacts_type'))
    else:
        form = ContactTypeForm()
    return render(request, "edit_contact_type.html", {'form': form, 'title': 'Add Contact Type'})


def delete_contact_type(request, id_contact_type):
    ct = Contact_type.objects.get(id_contact_type=id_contact_type)
    ct.delete()
    return HttpResponseRedirect(reverse('contacts_type'))


"""End Contacts
=========================================================================================================
Relations Type"""


def show_relations_type(request):
    return render(request, "relations_type.html", {'relations_type': Relation_type.objects.all()})


def edit_relation_type(request, id_relation_type):
    rt = get_object_or_404(Relation_type, id_relation_type=id_relation_type)

    if request.method == 'POST':
        form = RelationTypeForm(request.POST, instance=rt)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('relations_type'))
    else:
        form = RelationTypeForm(instance=rt)

    return render(request, "edit_relation_type.html", {'form': form, 'title': 'Edit Relation Type'})


def add_relation_type(request):
    if request.method == 'POST':
        form = RelationTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('relations_type'))
    else:
        form = RelationTypeForm()
    return render(request, "edit_relation_type.html", {'form': form, 'title': 'Add Relation Type'})


def delete_relation_type(request, id_relation_type):
    rt = Relation_type.objects.get(id_relation_type=id_relation_type)
    rt.delete()
    return HttpResponseRedirect(reverse('relations_type'))


"""End Relations Type
=========================================================================================================
Relations"""


def show_relations(request):
    return render(request, "relations.html", {'relations': Relation.objects.all()})


def edit_relation(request, id_relation):
    rt = get_object_or_404(Relation, id_relation=id_relation)

    if request.method == 'POST':
        form = RelationForm(request.POST, instance=rt)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('relations'))
    else:
        form = RelationForm(instance=rt)

    return render(request, "edit_relation.html", {'form': form, 'title': 'Edit Relation'})


def add_relation(request):
    if request.method == 'POST':
        form = RelationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('relations'))
    else:
        form = RelationForm()
    return render(request, "edit_relation.html", {'form': form, 'title': 'Add Relation'})


def delete_relation(request, id_relation):
    rt = Relation.objects.get(id_relation=id_relation)
    rt.delete()
    return HttpResponseRedirect(reverse('relations'))


def show_person_relations(request, id_person):
    relations = Relation.objects.filter(id_person1=id_person) | Relation.objects.filter(id_person2=id_person)
    return render(request, "relations.html", {'relations': relations})
