import argparse
from contactsApp import *
from save import *



def getArgumentParser():
    parser = argparse.ArgumentParser(description='Process contacts.')
    subparsers = parser.add_subparsers(dest='command', help='subcommand help')

    # Add contact command
    subparsers.add_parser('add', help='Add a contact')

    # Remove contact command
    remove_parser = subparsers.add_parser('remove', help='Remove a contact')
    remove_parser.add_argument('identifier', help='Identifier of the contact to remove')

    # Search contact command
    search_parser = subparsers.add_parser('search', help='Search for a contact')
    search_parser.add_argument('query', help='Query to search for a contact')

    edit_parser = subparsers.add_parser('edit', help='Edit a contact')
    edit_parser.add_argument('edit_identifier', help='Identifier of the contact to edit')
    
    # List contacts command
    subparsers.add_parser('list', help='List all contacts')

    return parser
