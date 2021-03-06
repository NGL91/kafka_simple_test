import time
import cv2
from kafka import SimpleProducer, KafkaClient

#Connect to kafka
kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)

#Assign a topic
topic = 'movie'

def video_emitter(video):
	#open video
	video = cv2.VideoCapture(video)
	print 'emitting ......'


	#read the file
	while (video.isOpened):
		#Read the image in each frame
		success, image = video.read()

		#CHeck if the file has read to the end
		if not success:
			break

		#Convert the image png
		ret, jpeg = cv2.imencode('.png', image)
		#Convert the image to bytes and send to kafka
		producer.send_messages(topic, jpeg.tobytes())
		#To reduce CPU usage create sleep time of 0.2 sec
		time.sleep(0.06)

	#clear the capture
	video.release()
	print 'done emitting'

if __name__ == '__main__':
	video_emitter('video.flv')