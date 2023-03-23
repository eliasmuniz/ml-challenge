# dealing with white space: strip, lstrip and rstrip
string_with_white_space = " smith  "
print("Value:%s!" % string_with_white_space.strip())
print("Value:%s!" % string_with_white_space.lstrip())
print("Value:%s!" % string_with_white_space.rstrip())

# converting case: upper, lower, capitalize
last_name = string_with_white_space.strip()
print("Lower case: %s" % last_name.lower())
print("Upper case: %s" % last_name.upper())
print("Capitalized: %s" % last_name.capitalize())