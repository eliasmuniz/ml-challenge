# open file
filename = './addresses.csv'
linecount = 0
with open(filename, 'r') as fl: # r is used for read permission
    for line in fl:
        print(line)
        linecount += 1
        if linecount > 10: break # let's not print too many lines to the console


# read the whole file
filename = './addresses.csv'
with open(filename, 'r') as fl:
  print(fl.read())

# read lines
with open(filename, 'r') as fl:
  print(fl.readlines())
