"""firstdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import show_persons, edit_person, add_person, delete_person,  \
    show_contacts, edit_contact, add_contact, delete_contact, person_contacts, \
    show_contacts_type, edit_contact_type, add_contact_type, delete_contact_type, \
    show_location, edit_location, add_location, delete_location, \
    show_relations_type, edit_relation_type, add_relation_type, delete_relation_type, \
    show_relations, edit_relation, add_relation, delete_relation, show_person_relations, \
    show_meetings, edit_meeting, add_meeting, delete_meeting, \
    show_person_meetings, edit_person_meeting, add_person_meeting, delete_person_meeting, show_my_person_meetings

urlpatterns = [
    #################-PERSONS-##################
    path('', show_persons, name='persons'),
    path('add/', add_person, name='add_person'),
    path('<int:person_id>/', edit_person, name='edit_person'),
    path('del/<int:person_id>/', delete_person, name='delete_person'),
    #################-LOCATIONS-##################
    path('locations/', show_location, name='locations'),
    path('locations/<int:id_location>/', edit_location, name='edit_location'),
    path('locations/add/', add_location, name='add_location'),
    path('locations/del/<int:id_location>/', delete_location, name='delete_location'),
    #################-MEETINGS-##################
    path('meetings/', show_meetings, name='meetings'),
    path('meetings/<int:id_meeting>/', edit_meeting, name='edit_meeting'),
    path('meetings/add/', add_meeting, name='add_meeting'),
    path('meetings/del/<int:id_meeting>/', delete_meeting, name='delete_meeting'),
    #################-PERSONS_MEETINGS-##################
    path('person_meetings/', show_person_meetings, name='person_meetings'),
    path('person_meetings/<int:id_person_meeting>/', edit_person_meeting, name='edit_person_meeting'),
    path('person_meetings/add/', add_person_meeting, name='add_person_meeting'),
    path('person_meetings/del/<int:id_person_meeting>/', delete_person_meeting, name='delete_person_meeting'),
    path('person_meetings/person/<int:id_person>/', show_my_person_meetings, name='show_my_person_meetings'),
    #################-CONTACTS-##################
    path('contacts/', show_contacts, name='contacts'),
    path('contacts/<int:id_contact>/', edit_contact, name='edit_contact'),
    path('contacts/add/', add_contact, name='add_contact'),
    path('contacts/del/<int:id_contact>/', delete_contact, name='delete_contact'),
    path('contacts/person/<int:id_person>/', person_contacts, name='person_contacts'),
    #################-CONTACTS_TYPE-##################
    path('contacts_type/', show_contacts_type, name='contacts_type'),
    path('contacts_type/<int:id_contact_type>/', edit_contact_type, name='edit_contact_type'),
    path('contacts_type/add/', add_contact_type, name='add_contact_type'),
    path('contacts_type/del/<int:id_contact_type>/', delete_contact_type, name='delete_contact_type'),
    #################-RELATIONS_TYPE-##################
    path('relations_type/', show_relations_type, name='relations_type'),
    path('relations_type/<int:id_relation_type>/', edit_relation_type, name='edit_relation_type'),
    path('relations_type/add/', add_relation_type, name='add_relation_type'),
    path('relations_type/del/<int:id_relation_type>/', delete_relation_type, name='delete_relation_type'),
    #################-RELATIONS-##################
    path('relations/', show_relations, name='relations'),
    path('relations/<int:id_relation>/', edit_relation, name='edit_relation'),
    path('relations/add/', add_relation, name='add_relation'),
    path('relations/del/<int:id_relation>/', delete_relation, name='delete_relation'),
    path('relations/person/<int:id_person>/', show_person_relations, name='show_person_relations'),
]
