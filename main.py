import random
print("Welcome to the chatbot!")
print("My name is Ethan")
name = input("What is your name? ")
print("Nice to meet you " + name + ", I look forward to assisting you!")
random_responses = []
run = True
while run = True:
  prompt_user = input("Do you want to continue the conversation? Choose yes or no: ")
  if prompt_user == "yes":
    run = True
  else:
    run = False
    print("Thanks for chatting " + name + "!")
    break
  user_input = input("What do you want to learn about? Here are some options: Geography, history, or math ")

  if user_input == "geography" or user_input == "Geography":
    random_responses =["Did you know that Antartica is the largest desert?", "Alaska is the biggest US State", "Canada has a lot of lakes"]
    random.shuffle(random_responses)
    randomResponse =  random.choice(my_list)
    print(randomResponse)
    
  if user_input == "history" or user_input == "History":
    random_responses =["Did you know that the Andrew Johnson suceeded Abraham Lincoln after his untimely passing?", "Mansa Musa was the richest person in the world", "The Mongols conquered the majority of Asia?"]
    random.shuffle(random_responses)
    randomResponse =  random.choice(my_list)
    print(randomResponse)

  if user_input == "math" or user_input == "Math":
    random_responses =["Did you know that factoring is one way to solve quadratics?", "Did you know that a lot was invented in 3000 BC?","The 5 12 13 right triangle is one example of a pythagorean triple"]
    random.shuffle(random_responses)
    randomResponse =  random.choice(my_list)
    print(randomResponse)
    
    
    
