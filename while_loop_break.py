secret_code="chupacabra"
user=input("Enter the word:")
while True:
    if secret_code==user:
        break
    user=input("Enter the word:")
print("You've successfully left the loop.")    
    