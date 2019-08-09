#####################################
#https://github.com/abdullahkitr0   #
#https://abdullahki.tk              #
#By Abdullah                        #
#Botun İsmi: Akro                   #
#####################################
#!/usr/bin/ python
import time

import speech_recognition as sr


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
           successful
    "error":   `None` if no error occured, otherwise a string containing
           an error message if the API could not be reached or
           speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
           otherwise a string containing the transcribed text
    """
    
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] =    recognizer.recognize_google(audio)
    except sr.RequestError:
        
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
    
        response["error"] = "Unable to recognize speech"

    return response


if __name__ == "__main__":

    NUM_GUESSES = 1
    PROMPT_LIMIT = 2
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

## Kelime Belirt
    word1 = "hello"
    word2 = "hi"
    word3 = "my name is"
    word4 = "Turkish"
    print("word1= hello")
    print("word2= hi")
    print("word3= My Name İs")
    print("word4= Turkish")
    ##------------
    ##Word1
    time.sleep(0)
    for i in range(NUM_GUESSES):
        for j in range(PROMPT_LIMIT):
            print('Word{} deki Kelimeyi Söyle!'.format(i+1))
            guess = recognize_speech_from_mic(recognizer, microphone)
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            print("Anlayamadım")

       
        if guess["error"]:
            print("ERROR: {}".format(guess["error"]))
            break

        
        print("Şunu Dedin : {}".format(guess["transcription"]))

        # determine if guess is correct and if any attempts remain
        guess_is_correct = guess["transcription"].lower() == word1.lower()
        user_has_more_attempts = i < NUM_GUESSES - 1

        if guess_is_correct:
            print("Doğru!".format(word1))
            break
        elif user_has_more_attempts:
            print("Yanlış. Tekrar Dene.\n")
        else:
            print("Hata, çıktıya benzer değil '{}'.".format(word1))
            break
##------------
    ##Word2
    time.sleep(0)
    for i in range(NUM_GUESSES):
        for j in range(PROMPT_LIMIT):
            print('Word{} deki Kelimeyi Söyle!'.format(i+2))
            guess = recognize_speech_from_mic(recognizer, microphone)
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            print("Anlayamadım")

       
        if guess["error"]:
            print("ERROR: {}".format(guess["error"]))
            break

        
        print("Şunu Dedin : {}".format(guess["transcription"]))

        # determine if guess is correct and if any attempts remain
        guess_is_correct = guess["transcription"].lower() == word2.lower()
        user_has_more_attempts = i < NUM_GUESSES - 1

        if guess_is_correct:
            print("Doğru!".format(word2))
            break
        elif user_has_more_attempts:
            print("Yanlış. Tekrar Dene.\n")
        else:
            print("Hata, çıktıya benzer değil '{}'.".format(word2))
            break
        ##------------
    ##Word3
    time.sleep(0)
    for i in range(NUM_GUESSES):
        for j in range(PROMPT_LIMIT):
            print('Word{} deki Kelimeyi Söyle!'.format(i+3))
            guess = recognize_speech_from_mic(recognizer, microphone)
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            print("Anlayamadım")

       
        if guess["error"]:
            print("ERROR: {}".format(guess["error"]))
            break

        
        print("Şunu Dedin : {}".format(guess["transcription"]))

        # determine if guess is correct and if any attempts remain
        guess_is_correct = guess["transcription"].lower() == word3.lower()
        user_has_more_attempts = i < NUM_GUESSES - 1

        if guess_is_correct:
            print("Doğru!".format(word3))
            break
        elif user_has_more_attempts:
            print("Yanlış. Tekrar Dene.\n")
        else:
            print("Hata, çıktıya benzer değil '{}'.".format(word3))
            break

##------------
    ##Word4
    time.sleep(0)
    for i in range(NUM_GUESSES):
        for j in range(PROMPT_LIMIT):
            print('Word{} deki Kelimeyi Söyle!'.format(i+4))
            guess = recognize_speech_from_mic(recognizer, microphone)
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            print("Anlayamadım")

       
        if guess["error"]:
            print("ERROR: {}".format(guess["error"]))
            break

        
        print("Şunu Dedin : {}".format(guess["transcription"]))

        # determine if guess is correct and if any attempts remain
        guess_is_correct = guess["transcription"].lower() == word4.lower()
        user_has_more_attempts = i < NUM_GUESSES - 1

        if guess_is_correct:
            print("Doğru!".format(word4))
            break
        elif user_has_more_attempts:
            print("Yanlış. Tekrar Dene.\n")
        else:
            print("Hata, çıktıya benzer değil '{}'.".format(word4))
            break
##Bazı Hataları Var Ama Sonuç Olarak Güzel Bir Şekilde Çalışıyor 
##Botun İsmi: Akro 
##Botun Sahibi: Abdullah
##Botun Sürümü : 1.0.0
##MIT Lisansı Tarafından Yasal Hakları Korunmaktadır.
##İstek,Şikayet,Öneri İçin https://abdullahki.tk
##Github:https://github.com/abdullahkitr0
##Web Site : https://abdullahki.tk

