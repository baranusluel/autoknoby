import string
import cognitive_face as CF
#import cv2 
import requests

KEY = '96ac51d9ccf74f258ecfc1ae8ece5e44'
CF.Key.set(KEY)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)


def compare_image_paths(original_image_path, input_image_path):
	img_paths = ['./test_images/ken1.jpg', 
		'./test_images/ken2.jpg']
	
	headers = {'Content-Type': 'application/octet-stream',
				'Ocp-Apim-Subscription-Key': '96ac51d9ccf74f258ecfc1ae8ece5e44'}
	

	params = {
			'returnFaceId': 'true'
                }


	path_to_face_api = '/detect'
	
	images = []
	
	for i in range(len(img_paths)):
		with open(img_paths[i], 'rb') as f:
			images.append(f.read())
	
	responses = []
	for i in range(len(images)):
		response = requests.post(BASE_URL + path_to_face_api, data = images[i], headers = headers)
		print(response.json())                
                
                responses.append(response.json())
			
	

	#faces = [CF.face.detect(img) for img in images]

	similarity = CF.face.verify(responses[0][0]['faceId'], responses[1][0]['faceId'])
	
	print(similarity)

 
def main():
	#clears all images in input
	
	#while(face not detected):
		#run in infinite loop
	
	
	#snap picture of detected face -> saves to input directory
	
	#compare detected face with image from original_image_path (call compare_image_paths)
	
	#pass serial stuff to arduino here
	
	compare_image_paths("hello", "bye")
	
	
	
	

if __name__ == "__main__":
	main()

