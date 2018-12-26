from django.db import models

TYPES = (
    (1, 'domowy'),
    (2, 'służbowy'),
    (3, 'faks'),
    (4, 'inny'),
)


class Address(models.Model):
    city = models.CharField(max_length=64, verbose_name=u"Miasto")
    street = models.CharField(max_length=64, verbose_name=u"Ulica")
    street_number = models.CharField(max_length=8, verbose_name=u"Nr domu")
    flat_number = models.CharField(max_length=8, verbose_name=u"Nr mieszkania")

    def __str__(self):
        return f"ul./al. {self.street} nr {self.flat_number} m. {self.street_number} {self.city}"


class Group(models.Model):
    group_name = models.CharField(max_length=16, verbose_name=u"Nazwa")
    group_desc = models.TextField(verbose_name=u"Opis")

    def __str__(self):
        return f"{self.group_name}"


class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    description = models.TextField()
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.SET_NULL)
    groups = models.ManyToManyField(Group, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class PhoneNumber(models.Model):
    p_num = models.CharField(max_length=16, verbose_name=u"Numer telefonu")
    p_type = models.IntegerField(choices=TYPES, verbose_name=u"Rodzaj telefonu")
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"telefon: {self.p_num} {self.p_type}"


class EmailAddress(models.Model):
    mail = models.EmailField(verbose_name=u"Adres email")
    m_type = models.IntegerField(choices=TYPES, verbose_name=u"Rodzaj maila")
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"mail: {self.mail} {self.m_type}"
