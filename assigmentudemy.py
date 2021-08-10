import re
import  requests
from bs4 import BeautifulSoup
import sqlite3 as sql


conn=sql.connect("udemydata.db")
curs=conn.cursor()
# curs.execute("create table udemy_scrap( questions text ,answers text ,relatedPg text,relatedpgUrl text)")
# conn.close()
# print("Table created")






Url="https://www.udemy.com/topic/python/"


def getudemy_scrap(Url):
    res = requests.get(url=Url).content
    soup = BeautifulSoup(res, 'html.parser')

    questions = []
    answers = []
    relPages = []
    relpgurl = []

    qns = soup.find_all('span', attrs={"class": "udlite-accordion-panel-title"})

    ans = soup.find_all('div', attrs={"class": "udlite-text-sm questions-and-answers--answer--2PMFk"})

    pages = soup.find_all('div', attrs={"class": "udlite-heading-md questions-and-answers--link--11XUK"})

    for i in qns:
        questions.append(i.text)
        # print(i.text)
    # print(questions)

    for a in ans:
        answers.append(a.text)

    for p in pages:
        relPages.append(p.a.text)
        # print(p.a.text)
        relpgurl.append(p.a.get('href'))
        # print(p.a.get('href'))


    for q, a, rp,ru in zip(questions, answers, relPages,relpgurl):
        question = q
        answer = a
        relpg = rp
        rurl= ru
        print(q)
        print(p)
        print(rp)
        print(ru)
        curs.execute('''insert into udemy_scrap values(?,?,?,?)''', (question, answer, relpg,rurl))





getudemy_scrap(Url)

conn.commit()
print('complete')
curs.execute('''select * from udemy_scrap''')
results=curs.fetchall()
print(results)
conn.close()


#print(a.text)










