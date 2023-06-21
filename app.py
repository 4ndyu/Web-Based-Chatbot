import openai

# Reads a txt file that contains the API key
apiKey = open(".apikey", "r")

openai.api_key = apiKey.read()

messages = []
messages.append({ "role" : "system", "content" : "You are a cake recipe book, you ask the user what cake they want to make and respond back with the recipe for that cake." })


while True:
    

    # Send the api call
    response = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=messages )

    # Display response in console
    print(response.choices[0].message.content)

    # Expanding the conservation
    messages.append(response.choices[0].message)

    # Capture user input
    user_input = input("Enter your answer: ")

    # Quit loop if user presses 'q'
    if user_input == 'q':
        exit()

    # Prop preparation
    messages.append({ "role" : "user", "content" : user_input })
