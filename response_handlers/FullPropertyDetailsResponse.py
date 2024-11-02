class FullPropertyDetailsResponse:
    def __init__(self, response_json):
        self.home_data = response_json['data']['home']

        # General info
        self.price = self.home_data['list_price']
        self.date_listed = self.home_data['list_date']  # To parse: datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        self.realtor_url = self.home_data['href']

        # Mortgage info (default None if missing)
        self.property_tax_rate = None
        self.insurance_rate = None
        self.monthly_payment_estimate = None

        # Description info (default None or sensible defaults)
        self.baths_3qtr = 0
        self.baths_full = 0
        self.baths_half = 0
        self.beds = 0
        self.sqft = None
        self.lot_sqft = None
        self.year_built = None
        self.property_type = None
        self.description_text = None

        # Photos
        self.photos = []

        # Location info
        self.address = None
        self.street_view_url = None
        self.neighborhood = None
        self.neighborhood_median_listing_price = None

        # Parse additional data
        self.parse_mortgage_data()
        self.parse_description()
        self.parse_photos()
        self.parse_location()

        # Now handled in PropertyTaxResponse
        # self.tax_paid_previous_year = self.home_data['source']['raw']['tax_amount']

    def parse_mortgage_data(self):
        mortgage = self.home_data['mortgage']
        self.property_tax_rate = mortgage['property_tax_rate']
        self.insurance_rate = mortgage['insurance_rate']
        self.monthly_payment_estimate = mortgage['estimate']['monthly_payment']

    def parse_description(self):
        description = self.home_data['description']
        self.baths_3qtr = description['baths_3qtr'] or 0
        self.baths_full = description['baths_full'] or 0
        self.baths_half = description['baths_half'] or 0
        self.beds = description['beds'] or 0
        self.sqft = description['sqft']
        self.lot_sqft = description['lot_sqft']
        self.year_built = description['year_built']
        self.property_type = description['type']  # Ex: "townhomes", also there's sub_type which would be "townhouse"
        self.description_text = description['text']

    def parse_photos(self):
        self.photos = []
        for photo in self.home_data['photos']:
            # title = photo['title']
            # description = photo['description']
            low_quality_photo_url = photo['href']
            high_quality_photo_url = low_quality_photo_url.replace('s.jpg', 'rd-w960_h720.webp')
            # tags = [tag['label'] for tag in photo['tags']]
            self.photos.append(high_quality_photo_url)
            # self.photos.append({
            #     'title': title,
            #     'description': description,
            #     'high_quality_photo_url': high_quality_photo_url,
            #     'tags': tags
            # })

    def parse_location(self):
        location = self.home_data['location']
        address = location['address']
        self.address = f"{address['line']}, {address['city']} {address['state_code']} {address['postal_code']}"  # Address like "123 Main St, Bethlehem PA 18018"
        self.street_view_url = location['street_view_url']
        has_neighborhood = type(location['neighborhoods']) is list
        if has_neighborhood:
            neighborhood = location['neighborhoods'][0]
            self.neighborhood = neighborhood['slug_id']
            self.neighborhood_median_listing_price = neighborhood.get('geo_statistics', {}).get('housing_market', {}).get('median_listing_price')

    def to_dict(self):
        dict = self.__dict__.copy()
        dict.pop('home_data')
        return dict
