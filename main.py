# main code:--- 

# import pyautogui
# import time
# import pyperclip
# import cohere


# # Initialize the Cohere client with your API key
# co = cohere.Client('API key')  # Replace with your actual API key

# def last_message(chat_log, sender_name="Aman Kumar"):
#     # Split the chat log into individual messages
#     messages = chat_log.strip().split("\n")
#     # Get the last message
#     last_message = messages[-1] if messages else ""
#     # Check if the last message is from the specified sender
#     if sender_name in last_message:
#         return True, last_message
#     return False, ""

# def extract_message_text(message):
#     # Extract the text from the last message, ignoring the timestamp and sender name
#     return message.split(": ", 1)[-1].strip() if ": " in message else message.strip()

# # Click on the icon at (616, 788) to open whatsapp
# pyautogui.click(876, 792)
# time.sleep(1)

# while True:
#     # copy from top
#     pyautogui.moveTo(760, 94)
    
#     # Drag to select text to botom
#     pyautogui.dragTo(761, 709, duration=1, button='left')
#     pyautogui.hotkey('command', 'c') 
#     time.sleep(1)
#     # select on random area
#     pyautogui.click(760 , 94)
#     # Retrieve the text from the clipboard
#     chat_his = pyperclip.paste()

#     print("Copied text:", chat_his)

#     is_last_message_from_ashish, last_message_text = last_message(chat_his)
    
#     # Check if the last message is "bye"
#     if "bye" in last_message_text.lower():
#         print("User said 'bye'. Stopping the bot.")
#         break  # Exit the loop

#     if is_last_message_from_ashish:
#         # Extract just the text of the last message
#         user_message = extract_message_text(last_message_text)

#         # Define the prompt with the actual text
#         prompt = f"You're Ashish, a human guy chatting casually with a friend on WhatsApp. Respond like a normal person—friendly, chill, and natural. Keep it real and easy to understand. User asked: {user_message}"

#         # Call the Cohere generate method to get a completion
#         response = co.generate(
#             model='command-xlarge-nightly',
#             prompt=prompt,
#             max_tokens=50,  # Adjust this for a longer response
#             temperature=0.7  # Adjust creativity of the response
#         )

#         # Print the response generated by the model
#         response_text = response.generations[0].text.strip()
#         pyperclip.copy(response_text)

#         # Send the response on WhatsApp clipbord.
#         pyautogui.click(969,742)
#         time.sleep(1)
#         pyautogui.hotkey('command', 'v')
#         time.sleep(1)
#         pyautogui.press('return')


# new code :--

import pyautogui
import time
import pyperclip
import cohere


co = cohere.Client('API key')  # Replace with your actual API key

def last_message(chat_log, sender_name="Aman Kumar"):
    messages = chat_log.strip().split("\n")
    last_message = messages[-1] if messages else ""
    if sender_name in last_message:
        return True, last_message
    return False, ""

def extract_message_text(message):
    return message.split(": ", 1)[-1].strip() if ": " in message else message.strip()

pyautogui.click(876, 792)
time.sleep(1)

while True:
    # Copy chat history
    pyautogui.moveTo(760, 94)
    pyautogui.dragTo(761, 709, duration=1, button='left')
    pyautogui.hotkey('command', 'c')
    time.sleep(1)
    pyautogui.click(760, 94)
    
    chat_his = pyperclip.paste()
    print("Copied text:", chat_his)

    is_last_message_from_ashish, last_message_text = last_message(chat_his)

    if "bye" in last_message_text.lower():
        print("User said 'bye'. Stopping the bot.")
        break  

    if is_last_message_from_ashish:
        user_message = extract_message_text(last_message_text)

        # Define chat prompt
        prompt = f"You're Ashish, a human guy chatting casually with a friend on WhatsApp. Respond like a normal person—friendly, chill, and natural. Keep it real and easy to understand. User asked: {user_message}"

        # Use chat API instead of generate API
        response = co.chat(
            model='command-xlarge-nightly',
            message=prompt
        )

        response_text = response.text.strip()
        pyperclip.copy(response_text)

        # Send response in WhatsApp
        pyautogui.click(969, 742)
        time.sleep(1)
        pyautogui.hotkey('command', 'v')
        time.sleep(1)
        pyautogui.press('return')
