print("Enter the word:")
user=input()
user=user.upper()
for i in range(len(user)):
    if user[i] in "AEIOU":
        continue
    print(user[i])