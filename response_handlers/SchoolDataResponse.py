from collections import defaultdict

ATTRS_TO_SCRAPE = [
    'distance_in_miles',
    'student_teacher_ratio',
    'rating',
    'student_count'
]

class SchoolDataResponse:
    def __init__(self, response_json):
        try:
            schools = response_json['data']['home']['schools']['schools']
        except (KeyError, TypeError):  # No schools data
            schools = []

        # Get all values for each attribute
        self.attr_values = defaultdict(list)
        for school in schools:
            for attr in ATTRS_TO_SCRAPE:
                if school.get(attr) is None:
                    continue
                self.attr_values[attr].append(school[attr])

        # Calculate averages
        self.averages = {}
        for key in self.attr_values:
            l = self.attr_values[key]
            if len(l) == 0:
                self.averages[key] = None
                continue
            self.averages[key] = sum(l) / len(l)

    def to_dict(self):
        return {'school_avg_' + key: self.averages.get(key) for key in ATTRS_TO_SCRAPE}
