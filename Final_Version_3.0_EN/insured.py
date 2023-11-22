# Imports input validation classes from another file
from validation import ValidationName, ValidationSurname, ValidationPhone, ValidationAge  


class Insured:
    def __init__(self, name: str, surname: str, phone: str, age: str):
        """The constructor of the Insured class initializes a new insured

        Args:
            name (str): Object name in string format
            surname (str): Object surname in string format
            phone (str): Object phone in string format
            age (str): Object age in string format
        """
        self.name = name
        self.surname = surname
        self.phone = phone
        self.age = age
        
    # Instantiation of descriptors to validate input values
    name = ValidationName()
    surname = ValidationSurname()
    phone = ValidationPhone()
    age = ValidationAge()

    def __str__(self) -> str:
        """Redefined method for formatting insured output

        Returns:
            str: The method returns the text form of the object
        """
        return f"name: {self.name} surname: {self.surname} phone: {self.phone} age: {self.age}"
