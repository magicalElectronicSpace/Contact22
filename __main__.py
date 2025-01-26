import sys
from contact import *
from save import *
from argument import *
from contactsApp import *


app = ContactsApp()
parser = getArgumentParser()
args = parser.parse_args()

if args.command is None:
    app.ui()
else:
    if args.command == 'add':
        app.add_contact()
    elif args.command == 'remove':
        app.remove_contact(args.identifier)
    elif args.command == 'edit':
        app.edit_contact(args.edit_identifier)
    elif args.command == 'search':
        contact = app.search_contact(args.query)
        if contact:
            for (key, value) in contact.__dict__.items():
                print(f"{key}: {value}")
        else:
            print("Contact not found.")
    elif args.command == 'list':
        app.list_contacts()


