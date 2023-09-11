from . import models


class Person:
    @staticmethod
    def create_person(person_data: dict) -> "Person":
        """
        Create Person
        :param person_data: dictionary containing Person details
        :return: Person
        """
        return models.Person.objects.create(name=person_data.get("name"))

    @staticmethod
    def get_person(person_id: int) -> "Person":
        """
        Retreive Person
        :param person_id: id of Person to retreive
        :return: Person
        """
        try:
            person = models.Person.objects.filter(id=person_id).first()
        except models.Person.DoesNotExist:
            return None
        return person

    @staticmethod
    def update_person(person_id: int, person_data: dict) -> "Person":
        """
        Update Person
        :param person_id: id of Person to update
        :param person_data: dictionary containing validated data to update with
        :return: Person
        """
        person = Person.get_person(person_id)
        if person is None:
            return None
        person.name = person_data.get("name")
        person.save()
        return person

    @staticmethod
    def delete_person(person_id: int) -> bool:
        """
        Delete Person
        :param person_id: id of Person to delete
        """
        person = Person.get_person(person_id)
        if person is None:
            return None
        person.delete()
        return True
