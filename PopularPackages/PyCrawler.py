import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")

soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".question-summary")

print(questions[0].get("id"))

print(type(questions))


for question in questions:
    print(question.select_one(".question-hyperlink").getText())
