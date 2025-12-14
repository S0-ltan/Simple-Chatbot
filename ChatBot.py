from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot=ChatBot("chatbot",read_only=False,logic_adapters=[



    {
        "import_path":"chatterbot.logic.BestMatch",
        "default_response":"I am sorry, I do not understand",
        "maximum_similarity_threshold":0.90


    }


     ])
list_to_train=[
               "hi",
               "Hi there! Welcome to my personal chatbot 😊",
               "what's your name",
               "I'm a Sultan F Amin",
               "how old are you",
               "I'm 20 years old",
               "thank you",
               "you're welcome",                                          
               "why you are mad",
               "I'm not",
               "what i do ",
               "nothing bad",

]
list_to_train2=[
               "hey",
               "Hi there! Welcome to my personal chatbot 😊",
               "what's your name",
               "I'm a Sultan F Amin",
               "what is your age?",
               "guess",
               "bye",
               "see you",
               "thank you",
               "hmmmm",
               "why you are mad",
               "becuse of you ",
               "what i do ",
               "you really ask!!",
]


list_to_train3=[
                "he",
                "Welcome ,Hi there! Welcome to my personal chatbot 😊",
                "age",
                "I'm 20 years old",
                "name",
                "I'm a Sultan F Amin",
                "city",
                "Dirout - Assiut",
                "study",
                "Computers and Artificial Intelligence",
                "languages",
                "Arabic , English, Russian",
]

                


list_trainer=ListTrainer(bot)
list_trainer.train(list_to_train)
list_trainer.train(list_to_train2)
list_trainer.train(list_to_train3)


while True:
    user_response = input("User: ")
    if user_response.lower() == "bye":
        print("Bot: Goodbye! 👋")
        break
    print("Bot:", bot.get_response(user_response))
