# Importing the random library to deliver randomized responses
import random
# Greet the user and get their name
print("Welcome to the chatbot!")
print("My name is Ethan")
name = input("What is your name? ")
print("Nice to meet you " + name + ", I look forward to assisting you!")
random_responses = []
run = True
# Loop to keep chatting with the user
while run == True:
  prompt_user = input("Do you want to continue the conversation? Please choose yes or no: ")
  # If the user selects yes, the loop will continue to run and the conversation will continue
  if prompt_user == "yes":
    run = True
  else:
    # If the user selects, no, then the loop breaks and the conversation stops
    run = False
    print("Thanks for chatting " + name + "!")
    break
  # Prompts the user for which subject they want to learn about
  user_input = input("What do you want to learn about? Here are some options: geography, history, or math ")

  # Displays a random geography fact if the user selects geography
  if user_input == "geography" or user_input == "Geography":
    random_responses =["Did you know that Antartica is the largest desert?", "Alaska is the biggest US State", "There are 195 countires in the world"]
    random.shuffle(random_responses)
    randomResponse =  random.choice(random_responses)
    print(randomResponse)
  # Displays a random history fact if the user selects history
  if user_input == "history" or user_input == "History":
    random_responses =["Did you know that the Andrew Johnson suceeded Abraham Lincoln?", "Mansa Musa was the richest person in the world", "The Mongols conquered the majority of Asia?"]
    random.shuffle(random_responses)
    randomResponse =  random.choice(random_responses)
    print(randomResponse)
  # Displays a random math fact if the user selects math
  if user_input == "math" or user_input == "Math":
    random_responses =["Did you know that factoring is one way to solve quadratics?", "Did you know that a lot was invented in 3000 BC?","The 5 12 13 right triangle is one example of a pythagorean triple"]
    random.shuffle(random_responses)
    randomResponse =  random.choice(random_responses)
    print(randomResponse)
    
# Suggestions for future updates: Make the conversaton seem less robotic, its very structured instead of naturally flowing. Dialogue more engaging and interesting. More subjects to talk about.
# Allow the user to respond to the bots fun fact, and use sentiment analysis to determine which responses the user likes and print out those types of fun facts.
    
