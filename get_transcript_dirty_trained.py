import os
import time
import json
import uuid
import wave
import pyttsx3 
import pandas as pd 
import glob
from watson_developer_cloud import AssistantV1, SpeechToTextV1, TextToSpeechV1, AuthorizationV1

speech_to_text = SpeechToTextV1(
    iam_apikey='LAa_IklIKTqUPmhIU6ybd4EmUAwkItQ0s9eTVjOv7Svn',
    url='https://stream.watsonplatform.net/speech-to-text/api'
)


speech_model = speech_to_text.get_model('en-US_BroadbandModel').get_result()
print(json.dumps(speech_model, indent=2))
transcript = [] 
file = []


file_name = glob.glob("/Users/AnchalBhalla/Desktop/adnoc-chatbot/voice_dirty/*.wav") 

for name in file_name:

	audio_file = open(name, 'rb')

	r = speech_to_text.recognize(
	            audio=audio_file,
	            content_type='audio/wav', acoustic_customization_id = '63e0be52-4e18-47b2-87f8-88a12117bdec').get_result() 
	try:
		output = r['results'][0]['alternatives'][0]['transcript'] 
		transcript.append(output) 
	except: 
		output = "" 
		transcript.append(output)

	print(name)

	 
	file.append(name)
 

df = pd.DataFrame({"File Name" : file, "Transcript" : transcript})
df.to_csv('transcript113-dirty-trained-2.csv', index=False)




# file_name = '/Users/AnchalBhalla/Desktop/adnoc-chatbot/audio-samples-random/cmu_us_awb_arctic-0.90-release/cmu_us_awb_arctic/wav/arctic_a0100.wav' 
# audio_file = open(file_name, 'rb')

# r = speech_to_text.recognize(
# 	            audio=audio_file,
# 	            content_type='audio/wav', acoustic_customization_id='b0e11f8f-2ff5-40d0-aef0-8b6bcb6609d6').get_result() 
# output = r['results'][0]['alternatives'][0]['transcript']  
# print(output)
