#Have a mc question, n answers, find the best one.
from googlesearch import search
import requests

def make_guess(question, answers):
    results = dict.fromkeys(answers, 0)
    for hit, i in zip(search(question, tld="com", num=10, stop=10), range(10, 1, -1)):
        r = requests.get(hit)
        question_map = dict.fromkeys(answers, 0)
        total = 0
        for answer in answers:
            count = r.text.upper().count(answer.upper())
            question_map[answer] += count
            total += count
        if total != 0:
            for k in question_map:
                results[k] += question_map[k]/total * i

    best = max(results, key=results.get)
    conf = max(results.values())/sum(results.values())
    return (best,conf)

questions = [
   (
    "What restaurant has the motto, 'Eat Fresh?'",
   ["Subway", "Taco Bell", "KFC", "McDonald's"]
   ),
   (
    "Who was the president during World War I?",
   ["Joe Biden", "Woodrow Wilson", "Abraham Lincoln", "Franklin Roosevelt"]
   ),
   (
    "Which country produces the most coffee in the world?",
   ["Brazil", "United States", "Colombia", "Italy"]
   ),
   (
    "What is the capital of Spain?",
   ["Barcelona", "Madrid", "Granada", "Valencia"]
   ),
   (
    "What is Chandler's last name in the sitcom Friends?",
   ["Bing", "Geller", "Halpert", "Tribbiani"]
   ),
   (
    "What is the third sign of the zodiac?",
    ["Gemini", "Cancer", "Aries", "Capricorn"]
   ),
   (
    "In what year was the first-ever Wimbledon Championship held?",
    ["1877", "1921", "2022", "2012"]
   ),
   (
    "What was the first state?",
    ["New York", "Connecticut", "Delaware", "Virginia"]  
   )
]

for q in questions:
    print(q[0])
    guess, conf = make_guess(q[0],q[1])
    print(f"Best guess is {guess} with confidence {int(conf*100)}%")