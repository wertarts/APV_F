from django.db import models


class Location(models.Model):
    id_location = models.AutoField(primary_key=True)
    city = models.CharField(max_length=100, null=True)
    street_name = models.CharField(max_length=100, null=True)
    street_number = models.IntegerField(null=True)
    zip = models.IntegerField(null=True)
    country = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    latitude = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    longitude = models.DecimalField(max_digits=6, decimal_places=3, null=True)

    def __str__(self):
        # print('Name', type(self.name), '\nCountry', type(self.country), '\nCity', self.city)
        return str(self.name) + ' - ' + str(self.country) + ': ' + str(self.city)


class Person(models.Model):
    id_person = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    id_location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, default=52)
    birth_day = models.DateField(default='1900-01-01')
    height = models.IntegerField(null=True)
    GENDER = (
        ('Female', 'Female'),
        ('Male', 'Male'),
    )
    gender = models.CharField(max_length=20, choices=GENDER, null=True)

    def __str__(self):
        return str(self.nickname) + ' ' + self.last_name + '' + self.first_name


class Contact_type(models.Model):
    id_contact_type = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    validation_regexp = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Contact(models.Model):
    id_contact = models.AutoField(primary_key=True)
    id_person = models.ForeignKey(Person, on_delete=models.PROTECT)
    id_contact_type = models.ForeignKey(Contact_type, on_delete=models.PROTECT, null=True)
    contact = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id_person) + ' ' + str(self.contact)


class Relation_type(models.Model):
    id_relation = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Relation(models.Model):
    id_relation = models.AutoField(primary_key=True)
    id_person1 = models.ForeignKey(Person, on_delete=models.PROTECT, related_name="who1")
    id_person2 = models.ForeignKey(Person, on_delete=models.PROTECT, related_name="who2")
    description = models.CharField(max_length=100, null=True)
    id_relation_type = models.ForeignKey(Relation_type, on_delete=models.CASCADE)


class Meeting(models.Model):
    id_meeting = models.AutoField(primary_key=True)
    start_date = models.DateField(max_length=100)
    start_time = models.TimeField(max_length=100)
    description = models.CharField(max_length=100, null=True, default='')
    duration = models.DurationField(default=0)
    id_location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.start_time) + " - " + str(self.start_date) + " " + str(self.duration) + " " + str(
            self.description) + " " + str(self.id_location)


class Person_meeting(models.Model):
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    id_meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, unique=False)
