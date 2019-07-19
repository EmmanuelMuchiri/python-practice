import pyperclip
import random


class Contact:
    contact_list = []

    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def save_contact(self):
        Contact.contact_list.append(self)

    def delete_contact(self):
        Contact.contact_list.remove(self)

    def generate_Password(self):
        print('''
        Password Generator
        ==================
        ''')
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
        length = 9

        print('\nhere are your passwords:')
        password = ''
        for c in range(0, length):
            password += random.choice(chars)
        print(password)
        # pass

    @classmethod
    def find_by_number(cls, number):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact

    @classmethod
    def contact_exist(cls, number):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                    return True

        return False

    @classmethod
    def display_contacts(cls):
        return cls.contact_list

    @classmethod
    def copy_email(cls, number):
        contact_found = Contact.find_by_number(number)
        pyperclip.copy(contact_found.email)
