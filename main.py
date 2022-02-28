from helper import create_days_dictionary, user_input_message
import helper
import os
from datetime import datetime
import logging

# logger = logging.getLogger("MAIN")
# logger.error("Error happened in the app")


print(datetime.utcnow())
print(os.name)
user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_unit_dictionary = create_days_dictionary(user_input)
    helper.validade_and_execute(days_and_unit_dictionary)