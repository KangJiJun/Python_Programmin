# condition : if, match(3.10 or more)
age = 17

if age >= 18:
    print("adult")
else:
    print("non-adult")
score = 85
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('D')
    
# match
grade = "A"

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Not bad")
    case "C" | "D":
        print("Usual")
    case _:
        print("Bad")