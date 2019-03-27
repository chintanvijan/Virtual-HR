import cv2
import face_recognition as fr
import time
def saveimg(image):
	cv2.imwrite(image,"temp.jpg")
	#cv2.imshow('image',image)
	#known_image = fr.load_image_file("Chintan.jpg")
	#camera = cv2.VideoCapture(0)
	#retval,im=camera.read()
	#cv2.imwrite('uk.jpg',im)
	#del(camera)
	#unknown_image = fr.load_image_file(image)
	"""be = fr.face_encodings(known_image)[0]
	ue = fr.face_encodings(image)[0]
	r = fr.compare_faces([be],ue)
	print(r[0])
	return r[0] """

def comp(image):
	known_image = fr.load_image_file("media/"+image)
	
	camera = cv2.VideoCapture(0)
	while True:
		ret_val,img=camera.read()
		cv2.namedWindow("my webcam",cv2.WINDOW_NORMAL)
		#cv2.setWindowProperty("my webcam")
		#cv2.moveWindow("my webcam",40,40)
		cv2.imshow('my webcam',img)
		if cv2.waitKey(1) == 27:
			cv2.imwrite('media\\uk.jpg',img)
			break  # esc to quit
	cv2.destroyAllWindows()

	"""time.sleep(5)
	retval,im=camera.read()
	cv2.imwrite('media\\uk.jpg',im)
	del(camera)
"""
	#print(retval)
	try:
		unknown_image = fr.load_image_file("media/uk.jpg")
		be = fr.face_encodings(known_image)[0]
		ue = fr.face_encodings(unknown_image)[0]
		r = fr.compare_faces([be],ue)
		print(r[0])
		t=r[0]
	except:
		t=False
		print(t)
	return t
"""
def tt():
	i = request.files['image']  # get the image
	 f = ('%s.jpeg' % time.strftime("%Y%m%d-%H%M%S"))
	 i.save('%s/%s' % (PATH_TO_TEST_IMAGES_DIR, f))
	 return Response("%s saved" % f)"""