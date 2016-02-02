import datetime

import models

FILENAME = 'student_names.txt'


def get_names_from_file():
    """Reads student names from a file and returns a list of student names
    
    The file must be in the following format:
        -One name per line
        -Names must be in the format <last_name>, <first_name> e.g. King, Daniel
    """
    
def put_names_in_database(name_list):
    """Puts a list of names into the database
    
    Args:
        name_list (list): Each element of this list must be a 2-tuple of the form
            ('<first_name>', '<last_name>') e.g. ('King', 'Daniel')
    """
    
def create_groupings():
    """Selects random groups of students from the database, in such a way that
    no student is working with a student they have worked with before.
    
    A file will be created with the name "groups <timestamp>.txt" containing the new pairings
    """

def delete_students_from_database():
    """Deletes all existing students from the database"""
    
def delete_groupings_from_database():
    """Deletes all existing groupings from the database"""
    