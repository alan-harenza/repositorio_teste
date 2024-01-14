import speech_recognition as sr

# esse é o recognizer
rec = sr.Recognizer()

with sr.AudioFile("teste.wav") as arquivo_audio:
    audio = rec.record(arquivo_audio)
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)
