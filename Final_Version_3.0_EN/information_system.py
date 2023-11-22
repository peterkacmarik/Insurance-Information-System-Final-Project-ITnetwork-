from insured import Insured  # Import class from another file


class UserDatabase:
    def __init__(self, list_all_insureds=[]) -> None:
        """The class constructor initializes an empty list of insured persons

        Args:
            list_all_insureds (list, optional): List of all insured persons. Defaults to [].
        """
        self.list_all_insureds = list_all_insureds
    
    def display_all_insureds(self):
        """The method returns a list of all insured persons

        Returns:
            list_all_insureds (list): List of all insured persons
        """
        return self.list_all_insureds
    
class UserManagement():
    def create_user(self, user_database: UserDatabase, name: str, surname: str, phone: str, age: str):
        """The method of creating a new insured and adding it to the insured's database

        Args:
            user_database (UserDatabase): Database of all insured persons
            name (str): Name of the insured
            surname (str): Surname of the insured
            phone (str): Phone of the insured
            age (str): Age of the insured

        Returns:
            new_insured (object): The method returns the object of the created insured
        """
        new_insured = Insured(name, surname, phone, age)
        user_database.list_all_insureds.append(new_insured)
        return new_insured

class ManageInsured():
    def find_insured(self, criterion: str, list_all_insured: list):
        """The method of searching for the insured person from the list of all insured persons by first or last name

        Args:
            criterion (str): Criterion on the basis of which the insured is searched
            list_all_insured (list): Database of all insured persons

        Returns:
            list_wanted_insureds (list): The method returns the list of searched insured persons
        """
        self.list_wanted_insureds = []
        
        for insured in list_all_insured:
            if criterion == insured.name or criterion == insured.surname:
                self.list_wanted_insureds.append(insured)
        return self.list_wanted_insureds
    
    def edit_insured(self, insured, new_name: str, new_surname: str, new_phone: str, new_age: str):
        """Method for editing the insured, overwriting building data with new data

        Args:
            insured (object): Flood object intended for editing
            new_name (str): New name for editing
            new_surname (str): New surname for editing
            new_phone (str): New phone for editing
            new_age (str): New age for editing
        """
        insured.name = new_name
        insured.surname = new_surname
        insured.phone = new_phone
        insured.age = new_age
        
    def remove_insured(self, criterion: str, list_all_insured: list):
        """Method for removing the insured from the list of insured

        Args:
            criterion (str): Criterion on the basis of which the insured is searched
            list_all_insured (list): Database of all insured persons

        Returns:
            insured (object): The method returns the deleted object
        """
        for insured in list_all_insured:
            if insured.name == criterion or insured.surname == criterion:
                list_all_insured.remove(insured)
        return insured
        
                
        