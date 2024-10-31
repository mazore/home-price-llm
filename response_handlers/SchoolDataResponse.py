from collections import defaultdict

ATTRS_TO_SCRAPE = [
    'distance_in_miles',
    'student_teacher_ratio',
    'rating',
    'student_count'
]

class SchoolDataResponse:
    def __init__(self, response_json):
        schools = response_json['data']['home']['schools']['schools']

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
        print(self.averages)

    def to_dict(self):
        return {'school_avg_' + key: val for (key, val) in dict(self.averages).items()}
