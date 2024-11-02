class PropertyTaxResponse:
    def __init__(self, response_json):
        try:
            tax_history_raw = response_json['data']['home']['tax_history'] or []
        except (KeyError, TypeError):  # No tax data
            tax_history_raw = []

        max_year = 0
        self.tax_history = []
        self.last_tax_assessment = None
        self.last_tax_paid = None
        for tax_year in tax_history_raw:
            assessment = tax_year['assessment'] or tax_year['market']
            if assessment is None:
                continue
            land = assessment['land']
            building = assessment['building']
            self.tax_history.append({
                'year': tax_year['year'],
                'tax': tax_year['tax'],
                'total_assessment': assessment['total'],
                'land_building_ratio': land / building if (land and building) else None
            })

            if tax_year['year'] > max_year:
                max_year = tax_year['year']
                self.last_tax_assessment = assessment['total']
                self.last_tax_paid = tax_year['tax']

    def to_dict(self):
        return self.__dict__
