email = str(input("Введите почту: \n"))
x = email.find("@") + 1
domen = email[x:]
print("Домен: " + domen)
