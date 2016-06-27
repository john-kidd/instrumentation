#!/usr/bin/python

from model import Contact
from validators import validate_input
from logger import log_info
from execute_around_querie import timer
from queries import GetContact
from model import ContactId

c = Contact("John F Kidd", "+4478866662", "john@test.com")

validate_input(log_info, c)

contact_id = ContactId(12345)
get_contact = GetContact()
query = timer(log_info)

contact_12345 = query(get_contact.with_contact_id(contact_id).query, get_contact.get_description)

log_info(contact_12345)
