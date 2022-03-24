"""
@Author: Sanatan Das
@Date: March 15, 2022,
This python module contains different regular expressions used for matching the text
"""
import re

"Search the string to see if it starts with \"The\" and ends with \"Spain\":"
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

"Print a list of all matches:"
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

"Return an empty list if no match was found:"
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

"Search for the first white-space character in the string:"
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

"Make a search that returns no match:"
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

"Split at each white-space character:"
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

"Split the string only at the first occurrence:"
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

"Replace every white-space character with the number 9:"
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

"Replace the first 2 occurrences:"
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

"Do a search that will return a Match Object:"
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)

"Print the position (start- and end-position) of the first match occurrence."
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

"Print the string passed into the function:"
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

"Print the part of the string where there was a match:"
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
















