import json
from pathlib import Path

# Define the file paths for contacts.json and config.json
contacts_file_path = Path(__file__).parent / "contacts.json"
config_file_path = Path(__file__).parent / "config.json"

def save(contacts):
    """
    Save the contacts to the contacts.json file.

    :param contacts: The contacts data to save.
    """
    with open(contacts_file_path, "w") as file:
        json.dump(contacts, file, indent=4)

def load():
    """
    Load the contacts from the contacts.json file.

    :return: The contacts data.
    """
    if not contacts_file_path.exists():
        return {"contacts": []}
    with open(contacts_file_path, "r") as file:
        return json.load(file)

def loadConfig():
    """
    Load the configuration from the config.json file.

    :return: The configuration data.
    """
    if not config_file_path.exists():
        return {}
    with open(config_file_path, "r") as file:
        return json.load(file)
