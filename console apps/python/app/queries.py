from model import Contact

class Query:

    def get_description(self):

        return self.__class__.__name__


class GetContact(Query):

    def with_contact_id(self, contact_id):
        self.contact_id = contact_id
        return self


    def query(self):s
        contact = Contact("John F Kidd", "+4478866662", "john@test.com")
        return contact
