with open("person.csv", "r") as person_file:
    persons = person_file.read()

persons = persons.splitlines()     #split a string into a list where each line is a list item

print(persons)

for row in persons:
    person = row.split(",")  #split each list item to more words, each word is a list item
    print("{0} is {1} years old and {2}." .format(person[0], person[1], person[2]))

