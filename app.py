import openai
import gradio
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

messages = []
messages.append({ "role" : "system", "content" : "You are a cake recipe book, you ask the user what cake they want to make and respond back with the recipe for that cake." })

def respond(history, new_message):

    # Add the user input to the messages
    messages.append({ "role" : "user", "content" : new_message })

    # Send the api call
    response = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=messages )

    # Obtain response text
    assistant_message = response.choices[0].message

    # Expanding the conservation
    messages.append(assistant_message)

    return history + [[new_message, assistant_message.content]]

with gradio.Blocks() as chat_bot:

    chatbot = gradio.Chatbot()
    user_input = gradio.Text()

    user_input.submit(respond, [chatbot, user_input], chatbot)

chat_bot.launch()
