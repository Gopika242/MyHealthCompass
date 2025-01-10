import openai
openai.api_key = "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"
def chat_with_gpt(prompt):
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ =="__main__":
    while True:
        user_input=input("You: ")
        if user_input.lower() in ["quit","exit","bye"]:
            break
        response=chat_with_gpt(user_input)
        print("Chatbot: ",response)
