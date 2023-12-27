#Api Key
with open("Data\\Api.txt","r",encoding='UTF-8') as file:
    API = file.read()

import openai
from dotenv import load_dotenv

openai.api_key = API
load_dotenv()
completion = openai.Completion()

def QuestionAnswer(question, chat_log = None):
    FileLog = open("Database\\qna_log.txt", "r",encoding='UTF-8')
    chat_log_template = FileLog.read()
    FileLog.close()

    if chat_log is None:
        chat_log = chat_log_template

    prompt = f"{chat_log}Question : {question}\nAnswer : "
    response = completion.create(model = "text-davinci-002",
                                 prompt = prompt,
                                 temperature = 0,
                                 max_tokens = 100,
                                 top_p = 1,
                                 frequency_penalty = 0,
                                 presence_penalty = 0)
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nQuestion : {question} \nAnswer : {answer}"
    FileLog = open("Database\\qna_log.txt","w",encoding='UTF-8')
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer