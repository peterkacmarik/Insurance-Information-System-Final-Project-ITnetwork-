class ValidationName:
    def __get__(self, instance, owner):
        """The method that is called when the value of the attribute is read.
        Args:
            instance (_type_): An instance of an object
            owner (_type_): The attribute owner class

        Returns:
            return: The method returns the compared input value if it is specified correctly, otherwise it throws a ValueError exception
        """
        return instance._name

    def __set__(self, instance, value):
        """The method compares the input value with the conditions

        Args:
            instance (_type_): An instance of an object
            value (str): The value it is trying to set

        Raises:
            ValueError: If the entered value is less than 3 characters, an error message is displayed.
            ValueError: If the entered value is other than letters, an error message will be displayed.
        """
        if len(value) < 3:
            raise ValueError(f"Entered name: '{value}' must have at least 3 characters.")
        if not value.isalpha():
            raise ValueError(f"Entered name: '{value}' can only contain letters.")
        instance._name = value

class ValidationSurname:
    def __get__(self, instance, owner):
        """The method that is called when the value of the attribute is read
        Args:
            instance (_type_): An instance of an object
            owner (_type_): The attribute owner class

        Returns:
            return: The method returns the compared input value if it is specified correctly, otherwise it throws a ValueError exception
        """
        return instance._surname

    def __set__(self, instance, value):
        """The method compares the input value with the conditions

        Args:
            instance (_type_): An instance of an object
            value (str): The value it is trying to set

        Raises:
            ValueError: If the entered value is less than 3 characters, an error message is displayed.
            ValueError: If the entered value is other than letters, an error message will be displayed.
        """
        if len(value) < 3:
            raise ValueError(f"Entered last name: '{value}' must have at least 3 characters.")
        if not value.isalpha():
            raise ValueError(f"Entered last name: '{value}' can only contain letters.")
        instance._surname = value
        
class ValidationPhone:
    def __get__(self, instance, owner):
        """The method that is called when the value of the attribute is read
        Args:
            instance (_type_): An instance of an object
            owner (_type_): The attribute owner class

        Returns:
            return: The method returns the compared input value if it is specified correctly, otherwise it throws a ValueError exception
        """
        return instance._phone

    def __set__(self, instance, value):
        """The method compares the input value with the conditions

        Args:
            instance (_type_): An instance of an object
            value (int): The value it is trying to set

        Raises:
            ValueError: If no number is entered, an error message will be displayed
        """
        if not value.isdigit():
            raise ValueError(f"Entered phone number: '{value}' must contain only numbers.")
        instance._phone = value
        
class ValidationAge:
    def __get__(self, instance, owner):
        """The method that is called when the value of the attribute is read
        Args:
            instance (_type_): An instance of an object
            owner (_type_): The attribute owner class

        Returns:
            return: The method returns the compared input value if it is specified correctly, otherwise it throws a ValueError exception
        """
        return instance._age

    def __set__(self, instance, value):
        """The method compares the input value with the conditions

        Args:
            instance (_type_): An instance of an object
            value (int): The value it is trying to set

        Raises:
            ValueError: If no number is entered, an error message will be displayed
        """
        if not value.isdigit():
            raise ValueError(f"Age specified: '{value}' must contain only numbers.")
        instance._age = value
        
class ValidationCriteria(Exception):
    # Created custom exceptions to validate search criteria
    def __init__(self, criterion):
        self.criterion = criterion
        self.message = f"Error: Invalid search criteria entered: {self.criterion}"
        super().__init__(self.message)
    
    def validate_criterion(self, criterion):
        """The method verifies whether the criterion has min. character length and contains only alphabetic characters 

        Args:
            criterion (str): The input value of the criterion

        Raises:
            ValidationCriteria: If the condition is not met, an error message is displayed
            ValidationCriteria: If the condition is not met, an error message is displayed

        Returns:
            return: Return a validated criterion
        """
        if not criterion.isalpha():
            raise ValidationCriteria(f"The first or last name can only contain letters.")
        elif len(criterion) < 3:
            raise ValidationCriteria(f"The first or last name must have at least 3 characters.")
        else:
            return criterion

class ValidationInputNumber(Exception):
    # Created custom exceptions for input password validation
    def __init__(self, select_action) -> None:
        self.select_action = select_action
        self.message = f"Error: Invalid value {self.select_action}"
        super().__init__(self.message)
        
    def validate_select_action(self, select_action):
        """The method returns select_action if no exception occurs

        Args:
            select_action (int): Input value for validation

        Raises:
            ValidationInputNumber: If the correct number is not entered, an error message will be displayed

        Returns:
            return: Return the validated value
        """
        if select_action < 1 or select_action >= 7:  
            # If the condition is not met, a warning will be displayed
            raise ValidationInputNumber("Enter only a number between 1 - 6")
        else:
            return select_action