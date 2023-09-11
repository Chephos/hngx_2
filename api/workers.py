from . import models


class Person:
    @staticmethod
    def create_person(person_data):
        return models.Person.objects.create(name=person_data.get("name"))

    @staticmethod
    def get_person(person_id):
        try:
            person = models.Person.objects.filter(id=person_id).first()
        except models.Person.DoesNotExist:
            return None
        return person

    @staticmethod
    def update_person(person_id, person_data):
        person = Person.get_person(person_id)
        if person is None:
            return None
        person.name = person_data.get("name")
        person.save()
        return person

    @staticmethod
    def delete_person(person_id):
        person = Person.get_person(person_id)
        if person is None:
            return None
        person.delete()
        return True
