"""Script to seed Skilljar lesson database."""
import os
import json
from datetime import datetime

import requests

import crud
import model
import server

os.system("dropdb lessons")
os.system("createdb lessons")

model.connect_to_db(server.app)
model.db.create_all()

# Dynamically load lesson data from skilljar

#per Skilljar API docs, needed base64 encoded key
headers = {
    "Authorization":  os.environ['SKILLJAR_KEY'],
    "Content": "application/json",
    "Accept": "application/json"
}
url = "https://api.skilljar.com/v1"
res = requests.get(url+"/domains/academy.circleci.com/published-courses", headers = headers)
data = json.loads(res.content)
# print(json.dumps(data,indent=4))



for course in data['results']:
    print(course['id'],course['course_url'])
    res = requests.get(url+"/domains/academy.circleci.com/published-courses/"+course['id']+"?include_searchable_content=True", headers = headers)
    coursedetails = json.loads(res.content)
    res = requests.get(url+"/domains/academy.circleci.com/published-courses/"+course['id']+"/enrollments", headers = headers)
    enrollmentcount = json.loads(res.content)["count"]
    for lesson in coursedetails['course']['lesson_list']:
        #skip Surveys as these aren't developed by SMEs or pertinent to this project
        if lesson['title'] == "Survey":
            continue
        print(" ",lesson['id'],lesson['title'])

        db_lesson = crud.create_lesson(lesson_name = lesson['title'],
                    publish_date="1/1/2000", #to be implemented in a further sprint
                    enrollments=enrollmentcount)

        #print(lesson)


#seed smes
# smeF = crud.create_sme(first_name="Fred",
                #   last_name="Bret-Mounet",
                #   job_title="CISO",
                #   email="freedomfred@gmail.com")

smeA = crud.create_sme(first_name="Amina",
                  last_name="Khattak",
                  job_title="Director, Technical Training and Content",
                  email="amina@circleci.com")

lessonA = crud.get_lesson_by_id(9)
print(lesson_name)
# lessonA.sme_id = smeA.sme_id
smeA.lessons.append(lessonA)
print(smeA)
model.db.session.commit()