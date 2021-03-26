import cv2
import numpy as np
import sched, time
s = sched.scheduler(time.time, time.sleep)
def fonk(sc):
    #

    kamera = cv2.VideoCapture(0)

    while True:
        ret, kare = kamera.read()
        gri_kare = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)

        esik_degeri = 0.45
        esik_degeri2 = 0.5

        nesne = cv2.imread("spor_araba.jpg",0)
        nesne2 = cv2.imread("vosvos.jpg", 0)

        w, h = nesne.shape
        w2, h2 = nesne2.shape

        res = cv2.matchTemplate(gri_kare, nesne, cv2.TM_CCOEFF_NORMED)
        res2 = cv2.matchTemplate(gri_kare, nesne2, cv2.TM_CCOEFF_NORMED)

        loc = np.where(res > esik_degeri)
        loc2 = np.where(res2 > esik_degeri2)

        for j in zip(*loc[::-1]):
            print("spor araba")
            #cv2.rectangle(kare, j, (j[0]+h, j[1]+w), (0,255,0),1)
            #cv2.putText(kare,"spor", (j[0]+10, j[1]-10), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 1)

        for j in zip(*loc2[::-1]):
            print("vosvos")
            #cv2.rectangle(kare, j, (j[0]+h2, j[1]+w2), (0,255,0),1)
            #cv2.putText(kare,"vosvos", (j[0]+10, j[1]-10), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 1)

        #cv2.imshow("ekran", kare)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    kamera.release()
    cv2.destroyAllWindows()
    #
    s.enter(1, 1, fonk, (sc,))

s.enter(1, 1, fonk, (s,))
s.run()