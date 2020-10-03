with open("person.csv", "r") as person_file:
    persons = person_file.read()

persons = persons.splitlines()

print(persons)

for row in persons:
    person = row.split(", ")
    print(person)
