from django.db import models

TYPES = (
    (1, 'domowy'),
    (2, 'służbowy'),
    (3, 'faks'),
    (4, 'inny'),
)


class Address(models.Model):
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    street_number = models.CharField(max_length=8)
    flat_number = models.CharField(max_length=8)

    def __str__(self):
        return f"ul./al. {self.street} nr {self.flat_number} m. {self.street_number} {self.city}"


class PhoneNumber(models.Model):
    p_num = models.CharField(max_length=16)
    p_type = models.IntegerField(choices=TYPES)

    def __str__(self):
        return f"telefon: {self.p_num} {self.p_type}"


class EmailAddress(models.Model):
    mail = models.EmailField()
    m_type = models.IntegerField(choices=TYPES)

    def __str__(self):
        return f"mail: {self.mail} {self.m_type}"


class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    description = models.TextField()
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    mail = models.ForeignKey(EmailAddress, on_delete=models.SET_NULL, null=True)
    phone = models.ForeignKey(PhoneNumber, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Group(models.Model):
    group_name = models.CharField(max_length=16)
    group_desc = models.TextField()
    persons = models.ManyToManyField(Person)

    def __str__(self):
        return f"{self.group_name} {self.group_desc}"
