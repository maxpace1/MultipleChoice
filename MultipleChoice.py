#Have a mc question, n answers, find the best one.
from bs4 import BeautifulSoup
import requests

question = "What restaurant franchise advises you to Eat Fresh?"
answers = ["Subway", "Taco Bell", "KFC", "McDonald's"]

question = "Who was the president during World War I?"
answers = ["Woodrow Wilson", "Franklin Delano Roosevelt", "George Washington", "Joe Biden"]

def search(q):
    params={"q":q,"tbs":"li:1"}
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}
    #r = requests.get("http://www.google.com/search?", params=params, headers=header)
    print("https://www.google.com/search?q="+q)
    r = requests.get("http://www.google.com/search?q="+q, headers=header)

    soup = BeautifulSoup(r.text, 'html.parser')
    extract = soup.find(id='result-stats')

    print(r.text)
    return int(extract.text[6:extract.text.find(' result')].replace(',',''))

results = [search(question+" "+answer) for answer in answers]
print(results)
print(answers[results.index(max(results))]) 