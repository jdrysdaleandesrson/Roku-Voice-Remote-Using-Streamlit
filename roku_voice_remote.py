import streamlit as st
import os 
import time 
import speech_recognition as sr




IP = str(input("\nEnter Roku IP Address."))

up ="curl -d '' \"http://"+IP+":8060/keypress/up\""
down ="curl -d '' \"http://"+IP+":8060/keypress/down\""
right = "curl -d '' \"http://"+IP+":8060/keypress/right\""
left = "curl -d '' \"http://"+IP+":8060/keypress/left\""
home ="curl -d '' \"http://"+IP+":8060/keypress/home\""
select = "curl -d '' \"http://"+IP+":8060/keypress/select\""
search = "curl -d '' \"http://"+IP+":8060/search/a\""
net_flix = "curl -d '' \"http://"+IP+":8060/launch/12\""
p_rime = "curl -d '' \"http://"+IP+":8060/launch/13\""
hbo_max = "curl -d '' \"http://"+IP+":8060/launch/566347\""


def netflix():
    os.system(net_flix)
    time.sleep(2)
    os.system(select)
    
def prime():
    os.system(p_rime)
    time.sleep(10)
    os.system(select)

def off():
    os.system(home)
    os.system(right)
    os.system(up)
    os.system(right)
    os.system(select)
    
def toggle():
    recongizer = sr.Recognizer()
    with sr.Microphone() as mic:
        recongizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = recongizer.listen(mic)
        text = recongizer.recognize_google(audio)
        text = text.lower()
        st.write(text)
        if('netflix' in text):
            netflix()
            text = ' '
        if('home' in text or 'on' in text):
            os.system(home)
            text = ' '
        if('prime' in text):
            prime()
            text = ' '
        if('off' in text):
            off()
            text = ' '


st.title('Roku Voice Remote')
switch_state = st.checkbox("Tick Box to Start")

while switch_state:
    toggle()

    


            

    






    
