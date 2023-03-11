import speech_recognition as sr
import openai
from config import your_openai_api
openai.api_key = your_openai_api


def record_audio():
    #load the speech recognizer and set the initial energy threshold and pause threshold
    r = sr.Recognizer()
    r.energy_threshold = 180
    r.pause_threshold = 1.3
    r.dynamic_energy_threshold = False

    filename = "audio.wav"

    with sr.Microphone(sample_rate=16000) as source:
        print("Say something!")
        #get audio from the microphone
        audio = r.listen(source)
        
        #save audio to wav file
        with open(filename, "wb") as f:
            f.write(audio.get_wav_data())

        return filename



def transcribe_forever(filename):

    audio_file = audio_file= open(filename, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print(transcript)
    return transcript['text']

    #result_queue.put_nowait(result) #Complete result
