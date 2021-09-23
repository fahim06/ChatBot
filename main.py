from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("My Bot")

message = [
    "hello",
    "hi there !",
    "how are you ?",
    "I am doing great these days",
    "What can I do for you?",
    "Good Morning Doctor. I don’t feel good.",
    "Come and sit here.",
    "Open your mouth.",
    "Since how long are you not feeling well?",
    "Since yesterday.",
    "No problem. Did you have motions yesterday?",
    "No Doctor. Not so freely.",
    "Doctor I feel weak and do not feel like eating.",
    "Ok. And what else?",
    "I feel like vomiting.",
    "Do you drink a lot of water?",
    "No Doctor, I don’t have water too much.",
    "Did you took any medicine?",
    "Yes Doctor, I took a Crocin.",
    "who asked you to take it?",
    "No one Doctor. I took it myself.",
    "why did you take it?",
    "Because I felt a headache.",
    "Nothing to be worried at.",
    "Do you need quick relief?",
    "No Doctor. It is enough you give me medicines for now.",
    "Good Morning doctor.",
    "Good morning! You seem pale and your voice sounds different.",
    "Yes doctor. I’m having a temperature and even a sore throat.",
    "Let me check.",
    "You have a moderate fever. Let me check your temperature.",
    "That’s really great.",
    "Yes it is.",
    "Temperature is not too high, around 99.8. Let me check your blood pressure as well.",
    "Your blood pressure is fine.",
    "It seems a bit scruffy. Not good.",
    "Yes, it has been quite bad.",
    "Do you sweat and shiver?",
    "Not sweating, but I feel slightly cold when I sit under a fan.",
    "Do you have any other questions?",
    "No, doctor. Thank you."
]
trainer = ListTrainer(bot)
# now training the bot with the help of trainer
trainer.train(message)
print("Bot is opening...........")
while True:
    query = input("Doctor : ")
    if query == "exit":
        break
    answer = bot.get_response(query)
    print("Patient : ", answer)
