
people = [
    {"name": "Natalia", "age": 35, "gender": "M"},
    {"name": "Kirill", "age": 36, "gender": "F"},
    {"name": "Denis", "age": 24, "gender": "M"},
    {"name": "Vladislav", "age": 31, "gender": "M"},
    {"name": "Olesia", "age": 29, "gender": "F"},
]

def average_age_by_gender(people, gender):
    ages = []
    for person in people:
        if person ["gender"] == gender:
            ages.append(person["age"])
        if len(ages) > 0:
            avg_age = sum(ages)/len(ages)
        else:
            avg_age = 0
        return avg_age


avg_age_females = average_age_by_gender(people, "F")
print("Average age for females:", avg_age_females)

avg_age_males = average_age_by_gender(people, "M")
print("Average age for males:", avg_age_males)
