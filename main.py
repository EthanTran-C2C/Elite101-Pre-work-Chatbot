print("Welcome to the chatbot!")
print("My name is Ethan")
name = input("What is your name? ")
age = input("Hello " + name + ", how old are you? ")
print("Nice to meet you " + name + " , who is " + age + " years old")

while True:
  prompt_user = input("Do you want to continue the conversation? Choose yes or no: ")
  if prompt_user == "yes":
    run = True
  else:
    run = False
    print("Thanks for chatting " + name + "!")
    break
  user_input = input("What do you want to learn about? Here are some options: Geography, history, food, math ")

  if user_input == "geography":
    print("Did you know that Antartica is the largest desert?")
    
  if user_input == "history":
    print("Did you know that the Credit Mobilier was a fraudulent railroad company that was involved in political corruption during the construction of the Union Pacific Railroad? ")

  if user_input == "food":
    print("Did you know that a gram of protein has 4 calories?")

  if user_input == "math":
    print("Did you know that Calculus is not fun?")
    
    
    
