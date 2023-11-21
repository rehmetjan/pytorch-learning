'''
months using 3 letters
'''
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


print(months[1])
print(months[2])
print(months[3])
print(months[3])
print(months[4])
print(months[5])
print(months[6])
print(months[7])
print(months[7])
print(months[8])
print(months[9])
print(months[10])


# please draw a triangle using number "1",

for i in range(1, 11):
    print(i * "1")


# please draw a triangle using number "2",
for i in range(1, 11):
    print(i * "2")

# draw a tranglee using number when its layers counts
for i in range(1, 11):
    print(i * str(i))
    if i == 10:
        break
