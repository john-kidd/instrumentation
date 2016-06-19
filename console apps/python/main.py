from model import Contact
from validators import validate_input
from logger import log_info

c = Contact("John F Kidd", "+4478866662", "john@test.com")

validate_input(log_info, c)
