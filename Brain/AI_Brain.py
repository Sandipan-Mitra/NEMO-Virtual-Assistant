# Api Key
with open("Data\\Api.txt", "r", encoding='UTF-8') as file:
    API_List = file.readlines()


import openai
from dotenv import load_dotenv


def ReplyBrain(question, chat_log=None):
    count = 0
    for key in API_List:
        try:
            API = API_List[count].replace("\n", "")
            # print(count)
            openai.api_key = API
            load_dotenv()
            completion = openai.Completion()
            # Retrieve
            with open("Database\\chat_log.txt", "r", encoding='UTF-8') as f:
                chat_log_template = f.read()

            if chat_log is None:
                chat_log = chat_log_template

            prompt = f"{chat_log}You : {question}\nNemo : "
            response = completion.create(model="text-davinci-003",
                                         prompt=prompt,
                                         temperature=0,
                                         max_tokens=50
                                         )
            answer = response.choices[0].text.strip()
            chat_log_template_update = chat_log_template + \
                f"\nYou : {question} \nNemo : {answer}"
            # Update
            with open("Database\\chat_log.txt", "w", encoding='UTF-8') as f:
                f.write(chat_log_template_update)

            return answer

        except:
            count += 1
    return "It seems the API key has reached its limit!"


# while True:
#     question = input("Enter: ")
#     print(ReplyBrain(question))
