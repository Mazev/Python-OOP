class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def __repr__(self):
        return f"{self.id}: {self.name} ({creation_month} {creation_year}) has age restriction {self.age_restriction}.\n" \
               f" Status: {self.is_rented}"

    def from_date(self, id, name, date, age_restriction):
        pass

