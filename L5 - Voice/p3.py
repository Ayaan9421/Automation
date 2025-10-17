from gtts import gTTS

text = input("Enter text: ")

tts = gTTS(text = text, lang='en')

fn = input("Enter filename: ")

tts.save(fn)
