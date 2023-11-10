from iso639 import Lang  # to retrieve language code
import whisper  # importing whisper model to transcribe the audio
from googletrans import Translator  # to translate the transcribed audio


def whisper_model(audio_file):
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    text_result = result["text"]
    return text_result


def translate_text(text_translate):
    translator = Translator()
    translate_to = translator.translate(text=text_translate, dest=translator_lang)
    translated = translate_to.text
    return translated


# ------------------------Using Whisper Model to transcribe the audio------------------------
audio = "audio_file.mp3"
text = whisper_model(audio)
print(f"The audio transcription: {text}")

# ----------------Asking for user for their preferred translation language---------------
user_lang = input("\nWhat language do you want the translation in?: ").capitalize()

try:  # try block to catch any invalid entry by user
    lg = Lang(user_lang)
    translator_lang = lg.pt1
except:
    print("Language not recognized. Only use ISO 639 language.")
else:
    # ------------Using Translator to translate the transcribed audio text to other language-------
    translated_text = translate_text(text)

    print(f"\nThe translated text: {translated_text}")
