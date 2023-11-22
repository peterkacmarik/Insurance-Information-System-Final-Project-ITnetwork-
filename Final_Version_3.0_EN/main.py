# Import classes from other files
from validation import ValidationCriteria, ValidationInputNumber
from information_system import UserManagement, ManageInsured, UserDatabase
from menu import menu


user_management= UserManagement()  # Create an instance of the class to manage the insured
manage_insured = ManageInsured()  # Create an instance of the insurance company management class
validation_criteria = ValidationCriteria(Exception)  # Creating an instance of the class for validating the specified criteria
validation_input_number = ValidationInputNumber(Exception)  # Create an instance of the menu number validation class
user_database = UserDatabase()  # Creating an instance of a class to create a list of insured persons

# The main program loop
while True:
    # The menu function displays the main menu
    menu()
    
    try:
        select_action = int(input("Select a menu number: "))
        # Getting a number at the input to select an action
        validation_input_number.validate_select_action(select_action)
        # Validation of the input number
    except ValueError as e:
        print(e)
        continue
    
    if select_action == 6:
        print("The application has ended. Have a nice day :D")  
        # If the user chooses action 6, the program will exit
        break
        # Exiting the main loop of the program, which leads to the termination of the program 

    elif select_action == 1:
        # When action 1 is selected, the method for entering input data and subsequently creating a new insured is called
        input_name = input("Enter the name:\n").strip().capitalize()
        input_surname = input("Enter the last name:\n").strip().capitalize()
        input_phone = input("Enter a phone number:\n").strip()
        input_age = input("Enter age:\n").strip()
        
        try:
            created_insured = user_management.create_user(user_database, input_name, input_surname, input_phone, input_age)
            print(f"An insured has been created: {str(created_insured)}")
            # Caught exceptions if invalid input data is entered
        except ValueError as e:
            print(e)
            
    elif select_action == 2:  
        # When action 2 is selected, a list of all insured persons is displayed
        list_all_insureds = user_database.display_all_insureds()
        if not list_all_insureds:
            print("There is no other insured in the list.")
        else:
            print("\nList of all insured persons:")
            for insured in list_all_insureds:
                print(str(insured))

    elif select_action == 3:  
        # When action 3 is selected, the insured is searched based on the entered criteria
        criterion = input("Enter first or last name to search:\n").strip().capitalize()
        
        try:
            validation_criteria.validate_criterion(criterion)
            # Validation of the input criteria
        except ValidationCriteria as e:
            print(f"{e.message}")
        
        found_insured = manage_insured.find_insured(criterion, user_database.list_all_insureds)  
        # Call method to find the insured
        
        if not found_insured:
            print("The wanted insured was not found.")
        else:
            print(f"Results:")
            for insuredh in found_insured:
                print(str(insured))
            
    elif select_action == 4:  
        # With option 4, the insured person will be searched based on the criteria and his data will be adjusted
        criterion = input("Enter first or last name to search:\n").strip().capitalize()
        
        try:
            validation_criteria.validate_criterion(criterion)  
            # Validation of the input criteria
        except ValidationCriteria as e:
            print(f"{e.message}")
            
        for insured in user_database.display_all_insureds():
            # In the cycle, all insured persons are checked and if they match the criteria, they are displayed
            if insured.name == criterion or insured.surname == criterion:
                print(f"Found insured: {insured}")
                
                # Enter new data
                new_name = input("Enter a new name: ").strip().capitalize()
                new_surname = input("Enter a new surname: ").strip().capitalize()
                new_phone = input("Enter a new phone: ").strip()
                new_age = input("Enter a new age: ").strip()
                
                manage_insured.edit_insured(insured, new_name, new_surname, new_phone, new_age)
                # The method that modifies the insured data is called
                print("The data of the insured has been successfully modified.") 
            else:
                print("The insured was not found.")  
        
    elif select_action == 5:  
        # With option 5, the insured will be removed from the list of insured persons based on the search criteria
        criterion = input("Enter first or last name to search:\n").strip().capitalize()
        
        try:
            validation_criteria.validate_criterion(criterion)
            # Validation of the input criteria
        except ValidationCriteria as e:
            print(f"{e.message}")
            
        insured_removed = manage_insured.remove_insured(criterion, user_database.list_all_insureds)
        # The method for removing the insured is called
        print(f"The insured {insured_removed} has been successfully removed from the database.")
        