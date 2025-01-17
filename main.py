print("Welcome to the chatbot!")
print("My name is Ethan")
name = input("What is your name? ")
age = input("Hello " + name + ", how old are you? ")

while True:
  prompt_user = input("Do you want to continue the conversation? Choose yes or no: ")
  if prompt_user == "yes":
    run = True
  else:
    run = False
    print("Thanks for chatting!")
    break
  user_input = input("What do you want to learn about? I know a lot about geography or history")

  if user_input = "geography":
    print("Cool Geography fact")
  if user_input = "history":
    print("Cool history fact")
    
