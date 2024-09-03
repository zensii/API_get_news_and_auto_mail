import requests
from email_sender import send_mail

api_key = '913df6cda36949daa496d0cc16e504cd'
url = f"https://newsapi.org/v2/everything?q=Jeronimo Martins&from=2024-07-30&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
content = request.json()
message = ''
for article in content['articles']:

    message += article['title'] + '\n'
    message += article['description'] + '\n' + '\n'

send_mail('Daily Digest', 'News', message)
