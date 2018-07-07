import string
import cognitive_face as CF
import requests
import serial
import cv2
import sys
import time

ser = serial.Serial('//dev//tty96B0', 9600)
KEY = '96ac51d9ccf74f258ecfc1ae8ece5e44'
CF.Key.set(KEY)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)

def compare_image_paths(original_image_path, input_image_path):
        img_paths = [original_image_path, input_image_path]

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
	return similarity['isIdentical']

def main():
        cascade_Path = "haarcascade_frontalface_default.xml"
        face_Cascade = cv2.CascadeClassifier(cascade_Path)
        video_capture = cv2.VideoCapture(0)
        old_time = time.time()

	while True:
            #Capture frame-by-frame
            ret, frame = video_capture.read()
            frame_small = cv2.resize(frame, (300,300), interpolation=cv2.INTER_AREA)

            gray = cv2.cvtColor(frame_small, cv2.COLOR_BGR2GRAY)

            faces = face_Cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )

            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame_small, (x, y), (x+w, y+h), (0, 255, 0), 2)

            if len(faces) > 0 and (time.time() - old_time > 3000):
                #compare detected face with image from original_image_path (call compare_image_paths)
                cv2.imwrite("tmp.jpg", frame)
                old_time = time.time()
                if(compare_image_paths(original_image_path='./test_images/baran.jpg',input_image_path='./tmp.jpg')):
                        #do serial stuff
                        ser.write("on")
                else:
                        ser.write("off")

            # Display the resulting frame
            cv2.imshow('Video', frame_small)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


        # When everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
	main()
