people = [
    {"name":"Daniel","house":"Gryfindor"},
    {"name":"Xerxes","house":"Ravenclaw"},
    {"name":"Bhobai","house":"Slytherin"}
]



people.sort(key=lambda person: person["name"])

print(people)