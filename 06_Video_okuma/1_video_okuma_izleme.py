import cv2

capture=cv2.VideoCapture(0)#webcamdan görüntü alma işlemi 0 seçimi ile sağlandı.

while True:
    ret,frame=capture.read()
    #ret True ve false döndürür.
    #frame->
    
    #frame ter çevirme işlemi yapılıyor.
    frame=cv2.flip(frame,1)#y eksenine gçre tersi alındı
    
    cv2.imshow("Webcam",frame)
    #her bir frame 30mili/saniye kadar ekranda tutulur.
    if cv2.waitKey(1) & 0Xff==ord("q"):
        break
    
capture.release()#videoyu serbest bırakma işlemi yapıldı.
cv2.destroyAllWindows()