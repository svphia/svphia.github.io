print("----------------------------------")
print("Rock, Paper, Scissors Account Setup")
print("----------------------------------")
while True: 
  username = input("Create a username: ")
  password = input("Create a password: ")
  confirm = input("Confirm your password: ")

  if password != confirm: 
    print("Your passwords don't match")

  if password == confirm:
    print("Your account has been set up!")
    textfile = open("acc.csv","a")
    textfile.write(",")
    textfile.write(username)
    textfile.write(",")
    textfile.write(password)
    textfile.close()
    break