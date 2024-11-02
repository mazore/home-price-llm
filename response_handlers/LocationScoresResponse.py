SCORE_LABELS = ['Walking', 'Cycling', 'Transit', 'Driving', 'Parks', 'Groceries', 'Shopping', 'Nightlife', 'Restaurants', 'Cafes', 'Daycares', 'Quiet', 'Vibrant', 'Wellness']

class LocationScoresResponse:
    def __init__(self, response_json):
        local = response_json['data']['home']['local']
        point_scores = local['location_scores']['point_scores']
        self.scores = {score['label']: score['value'] for score in point_scores}

    def to_dict(self):
        d = {}
        # print(list(self.scores.keys()))
        for score in SCORE_LABELS:
            d[score.lower() + '_score'] = self.scores.get(score, None)
        return d
