class PropertyTaxResponse:
    def __init__(self, response_json):
        print(response_json)
        try:
            tax_history_raw = response_json['data']['home']['tax_history'] or []
        except (KeyError, TypeError):  # No schools data
            tax_history_raw = []

        self.tax_history = []
        for tax_year in tax_history_raw:
            land = tax_year['assessment']['land']
            building = tax_year['assessment']['building']
            self.tax_history.append({
                'year': tax_year['year'],
                'tax': tax_year['tax'],
                'total_assessment': tax_year['assessment']['total'],
                'land_building_ratio': land / building if (land and building) else None
            })

    def to_dict(self):
        return self.__dict__
