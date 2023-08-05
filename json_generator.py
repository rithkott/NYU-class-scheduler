import requests

def generate_json(subject):
    TERM = 'sp2023'

    url = 'https://nyu.a1liu.com/api/courses/' + TERM + '/' + subject

    req = requests.get(url)

    return req.json()

#generates JSON file for given term, subject, and course number
