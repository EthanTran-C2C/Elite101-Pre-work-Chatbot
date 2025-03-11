# Greets the user and gives them a list of options to choose from
print("Hello, how may I assist you today?")
# To be added: 4: Other; Then allow the user to talk to the chatbot for a different issue
# Add a help option
def get_user_info():
    while True:
        prompt_user = input("1: Refund\n 2: Track your order\n 3: Contact customer service")

        if prompt_user == 1:
            billing_information = input("Please enter your credit card information")
            return billing_information
            break
            #Do a refund
        if prompt_user == 2:
            zipcode = input("Please enter the address your order is being shipped to")
            return zipcode
            break
        if prompt_user != 1, 2, 3:
            System.out.println("Please choose a value from the list")

        if prompt_user == 3:
            print("---------")
            print("Connecting you with customer service")
            print("Please wait one moment")
            customer_service = True
            return customer_service
            break

def refundCustomer(billing):
    