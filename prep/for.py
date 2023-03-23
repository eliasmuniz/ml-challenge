# example
sentence = "This is Anyone AI"

# for letter in sentence:
#     print(letter)


offices = {
    "atlanta": {
        "phone": "8885551212",
        "city": "Atlanta",
        "state": "GA"
    },
    "sf": {
        "phone": "8005551212",
        "city": "San Francisco",
        "state": "CA"
    }
}

for key in offices.keys():
  print(key)

phonebook = {
    "John": "3105551212",
    "Bob": "9496667777",
    "Alice": "7144445555"
}

# similar to a simple loop, but items() returns to values: key and the value from the dictionary
for key, item in phonebook.items():
  print("Here is a key item combo. Key: %s, Number: %s" % (key, item))

my_list_of_numbers = []
for number in range(1, 100):
  # add all numbers to the list except the 15
  if number == 15 or number == 10:
    continue
  my_list_of_numbers.append(number)

print(my_list_of_numbers)

total_loop_count = 0

for first in range(0, 100):
  for second in range(0, 100):
    for third in range(0, 100):
      total_loop_count += 1

print("total_loop_count is %s" % total_loop_count)

example = [{"elem":1, "elem2": 2}, "banana", "cherry", "kiwi", "mango"]
fruits = ["apple", "banana", "cherry", "kiwi", "mango", "anana"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#another way to write it
fruits = ["apple", "banana", "cherry", "kiwi", "mango", "anana"]
newlist = [fruit for fruit in fruits if "a" in fruit]

print(newlist)