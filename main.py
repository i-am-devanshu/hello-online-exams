import requests ,webbrowser
from bs4 import  BeautifulSoup
print(
"""
 _   _        _  _           ___          _  _                _____                               _ 
| | | |  ___ | || |  ___    / _ \  _ __  | |(_) _ __    ___  | ____|__  __  __ _  _ __ ___   ___ | |
| |_| | / _ \| || | / _ \  | | | || '_ \ | || || '_ \  / _ \ |  _|  \ \/ / / _` || '_ ` _ \ / __|| |
|  _  ||  __/| || || (_) | | |_| || | | || || || | | ||  __/ | |___  >  < | (_| || | | | | |\__ \|_|
|_| |_| \___||_||_| \___/   \___/ |_| |_||_||_||_| |_| \___| |_____|/_/\_\ \__,_||_| |_| |_||___/(_)
                                                                                                    
                                                                                     Author - Devanshu 
""")
print("Change The Code NOT the Credits.....\n")
def getquestions():
     url=input("Enter The Google Forms URL : ")
     data = requests.get(url).content
     result = BeautifulSoup(data,'html.parser').find_all(class_="freebirdFormviewerComponentsQuestionBaseTitle") # Extracting Questions
     for question in result:
          webbrowser.open_new_tab("https://www.google.com/search?q=" + question.get_text())
     
getquestions()
