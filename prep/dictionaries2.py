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

print(offices)
print("San Francisco phone: %s" % offices["sf"]["phone"])
if "sf" in offices:
  print("sf key is in the offices dictionary")

if "ny" not in offices:
  print("ny key is NOT in the offices dictionary")


print(offices.keys())
print(offices.values())
print(offices["sf"].values())