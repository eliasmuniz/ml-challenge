months = ('January','February','March','April','May','June',\
'July','August','September','October','November','  December')

user = ('Elias','Muniz')

print(months)
# tuples are inmutables
# tuples are use when the order of the elements is very important
# tuples are unpackable or can be destructured in different variables
name, lastname = user
print(name, lastname )
print(months[10] )


for index, month in enumerate(months):
    print(f"Month {month}, Index {index+1}")