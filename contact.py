from dataclasses import dataclass
from save import load, loadConfig

@dataclass
class Contact:
    first_name: str
    middle_name: str
    last_name: str 
    phone: str
    email_address: str
    addressLine1: str
    addressLine2: str
    city: str
    state: str
    zip: str
    first_last: str
    last_first: str
    full_address: str
    full_name: str
    unique_id: str

