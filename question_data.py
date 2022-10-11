import requests


def new_request():
    global question_data
    global response

    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    question_data = response.json()


parameters = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = response.json()

