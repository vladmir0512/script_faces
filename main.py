import cv2

def check_face(img_dir):
    img = cv2.imread(img_dir) #Прочитать то, что даем на вход
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cv2.CascadeClassifier('faces.xml')
    results = faces.detectMultiScale(img, scaleFactor=2, minNeighbors=1)
    count = 0

    for (x, y, w, h) in results:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)
        count += 1
    if count == 1:
        count == True
    elif count == 0:
        count == False
    else:
        print("Error. Count not equals 1")

    ##__________Показать_окно с распознованием_____________#
    #cv2.imshow("Result", img) ############################
    #cv2.waitKey(0) #######################################
    #______________________________________________________#

    return bool(count)

im = input('Enter the name of file in Images folder. Example: 1.jpg\n')

if (check_face('images/'+ im)):
    print("Authenticated.")
