from jiwer import wer
import pandas as pd

ground_truth = []
hypothesis = []  
error_rate = []


data = pd.read_csv('transcript113-dirty-trained-2.csv', encoding = 'latin-1') 

full_data = pd.read_csv('full-transcript-dirty-dataset.csv', encoding = 'latin-1')


for i in range(len(data)):
  trans = data['Transcript'][i]
  file_name = data['File Name'][i]

  for j in range(len(full_data)):
  	real_name = full_data['fileName'][j]
  	real_trans = full_data['trnscrpt'][j]

  	if real_name == file_name: 

  		try:
	  		error_temp = wer(trans, real_trans)
	  		print(error_temp)
	  		error_rate.append(error_temp)
	  		ground_truth.append(real_trans)
	  		hypothesis.append(trans)
	  	except: 
	  		error_rate.append(" ")
	  		ground_truth.append(" ") 
	  		hypothesis.append(" ")
   
 



error = wer(ground_truth, hypothesis)

print(error)


df = pd.DataFrame({"Transcript" : ground_truth, "Prediction" : hypothesis, "Error Rate" : error_rate})
df.to_csv('transcript113-dirty-errorRate-after-train.csv', index=False)