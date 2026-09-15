from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person: Person = {'name':'vimal singh', 'age':'22'}

print(new_person)