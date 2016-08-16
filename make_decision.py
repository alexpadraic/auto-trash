# uses the output from inception, meaning many confidence percentages of each object it may be, 
# to send the raspberry pi either a 1 or 2 representing compost and recycle respectively. This class 
# is really what is going to interact with the raspberry pi. 

#possible decision making algorithms: 

# add up confidences for objects that are classified as compost and all other classifications 
# make the decision based on the one with the highest summation. 
# this may be flawed due to the fact that the first guess could be right but the second not even close. 

# We should do a weighted sum...the first guess should count the most, and if the first guess doesn't 
# fall into a recycle or compost classification, then look to the other guessess...

from classify_image import run_inference_on_image 


def predict_top_5(image_url):
	return run_inference_on_image(image_url)

def top_prediction_tuple(predictions_list):
	return predictions_list[0]

def top_prediction_name(prediction):
	return prediction[0]

def top_prediction_number(prediction):
	return prediction[1]





# predictions_list = run_inference_on_image('banana.jpg')






