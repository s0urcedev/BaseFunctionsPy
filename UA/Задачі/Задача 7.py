people = [] # основний масив
'''структура словаря
{
    "firstName": "",
    "secondName": "",
    "age": "",
    "country": "",
    "city": ""
}
'''

def create_people(first_name, second_name, age, country, city):
    people.append({
        "firstName": first_name,
        "secondName": second_name,
        "age": age,
        "country": country,
        "city": city
    })