#!/usr/bin/python

from model import Contact
from validators import validate_input
from logger import log_info
from execute_around_querie import timer

c = Contact("John F Kidd", "+4478866662", "john@test.com")

validate_input(log_info, c)
query = timer(log_info)

query(lambda: "test", lambda: "test 1")
