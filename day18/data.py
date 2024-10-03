import requests

class Question_data:
    def __init__(self):
        url = 'https://opentdb.com/api.php?amount=10&category=18&type=boolean'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        self.question_data = data['results']