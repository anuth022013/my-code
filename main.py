import cv2



def faceBox(faceNet,frame):
    print(frame)
    frameHeight=frame.shape[0]
    frameWidht=frame.shape[1]
    cv2.dnn.blobFromImage(frame, 1.0, (277,277), [104,117,123], swapRB=False)
    faceNet.setInput(blob)
    detection=facNet.forward()
    # for i in range(detection.shape[2]):
    #    confidence=detection[0,0,i,2]
    #   if confidence>0.7:
    #        detection[0,0,i,3]*
    return detection


faceProto = "opencv_face_detector.pbtxt"
faceModel = "opencv_face_detector_uint8.pb"


faceNet=cv2.dnn.readnet(faceModel, faceProto)


video=cv2.VideoCapture(0)

while True:
    ret,frame=video.read()
    detect=faceBox(faceNet,frame)
    cv2.imshow("Age-gender",frame)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
video.realease()
cv2.destroyAllWIndows()
