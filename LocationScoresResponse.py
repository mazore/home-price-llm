class LocationScoresResponse:
    def __init__(self, response_json):
        local = response_json['data']['home']['local']
        point_scores = local['location_scores']['point_scores']
        self.scores = {score['label']: score['value'] for score in point_scores}

    def to_dict(self):
        d = {}
        for key, value in self.scores.items():
            d[key.lower() + 'Score'] = value
        return d
