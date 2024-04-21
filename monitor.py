import os
import pyautogui
import pathlib
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timezone
import textwrap
from dotenv import load_dotenv
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import PIL.Image
import time

#nee to first run quickstart and then monitor would work. check why this happens.

#way apr 21
#now it can takes screenshoot, and 
load_dotenv()
GOOGLE_API_KEY= os.getenv('GEMINI_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
'''
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
'''

def take_screenshot_and_save():
    screenshot = pyautogui.screenshot()
    screenshot_path = 'current_screen.png'
    screenshot.save(screenshot_path)
    return screenshot_path

def get_current_event_description(service):
    now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=1, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        return "No event description available."
    return events[0].get('summary', 'description' )

def is_event_happening_now(service):
    now = datetime.utcnow().isoformat() + 'Z'
    print(now)
    # Get the current and next events
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=1, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    if (events):
        return True   
    else:
        return False  # No event is happening now


def check(service):
    # Take a screenshot
    screenshot_path = take_screenshot_and_save()

    # Get current event description
    event_description = get_current_event_description(service)
    prompt = f"Does this screenshot match the event description: '{event_description}'?"
    img = PIL.Image.open(screenshot_path)
    
    # ask gemini if this is the same event
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([prompt,img])
    print(response.text)
    #https://ai.google.dev/gemini-api/docs/get-started/python 


def main():
    # Setup Google Calendar API
    creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/calendar.readonly'])
    service = build('calendar', 'v3', credentials=creds)


    #about to write some logics in checking servise 
    #1 when there is an event going on, during the strat and the end time, check every 5 minutes
    while (is_event_happening_now(service)):
        print(is_event_happening_now(service))
        check(service)
        time.sleep(300) #check every 5 minuts



    '''
    #testing gemini-pro(text only)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("What is the meaning of life?")
    print(response.text)
    '''

   
    

if __name__ == '__main__':
    main()
