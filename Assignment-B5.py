import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os
import time
import datetime
import numpy as np

class ChatBot:
    def __init__(self, channel):
        print(f"----- Starting up {channel} -----")
        self.channel = channel
        self.chat_history_ids = None
        self.bot_input_ids = None
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
        self.model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

    def speech_to_text(self, only_text=False):
        if only_text:
            print("Me  --> ", end="")
            self.text = input()
            return
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic)
            print("Listening...")
            audio = recognizer.listen(mic)
            self.text = "ERROR"
        try:
            self.text = recognizer.recognize_google(audio)
            print("Me  --> ", self.text)
        except:
            print("Me  -->  ERROR")

    def text_to_speech(self, text, only_text=False):
        print(f"{self.channel} --> {text}")
        if only_text:
            return
        speaker = gTTS(text=text, lang="en", slow=False)
        speaker.save("res.mp3")
        playsound("res.mp3")
        os.remove("res.mp3")

    def wake_up(self, text):
        return True if self.channel.lower() in text.lower() else False

    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime("%H:%M")

    def generate_response(self, user_input):
        # Encode input and append to history
        new_input_ids = self.tokenizer.encode(user_input + self.tokenizer.eos_token, return_tensors='pt')
        if self.chat_history_ids is not None:
            self.bot_input_ids = torch.cat([self.chat_history_ids, new_input_ids], dim=-1)
        else:
            self.bot_input_ids = new_input_ids

        # Generate response
        self.chat_history_ids = self.model.generate(
            self.bot_input_ids,
            max_length=1000,
            pad_token_id=self.tokenizer.eos_token_id
        )
        response = self.tokenizer.decode(self.chat_history_ids[:, self.bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        return response


# Running the chatbot
if __name__ == "__main__":
    channel = "Dev"
    ai = ChatBot(channel=channel)
    ex = True
    while ex:
        ai.speech_to_text(only_text=True)

        if ai.wake_up(ai.text):
            res = "Hello, I am Dave the AI. What can I do for you?"
        elif "time" in ai.text:
            res = ai.action_time()
        elif any(i in ai.text for i in ["thank", "thanks"]):
            res = np.random.choice([
                "You're welcome!",
                "Anytime!",
                "No problem!",
                "Cool!",
                "I'm here if you need me!",
                "Mention not"
            ])
        elif any(i in ai.text for i in ["exit", "close", "bye"]):
            res = np.random.choice([
                "Tata",
                "Have a good day",
                "Bye",
                "Goodbye",
                "Hope to meet soon",
                "Peace out!"
            ])
            ex = False
        elif ai.text == "ERROR":
            res = "Sorry, could you repeat that?"
        else:
            res = ai.generate_response(ai.text)

        try:
            ai.text_to_speech(res, only_text=False)
        except:
            pass

    print(f"----- Closing down {channel} -----")
