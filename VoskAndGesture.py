import json
import serial
import time
import cv2
import pyaudio
from vosk import Model, KaldiRecognizer
import handTrackingModule as htm

# Replace 'COMx' with the appropriate Bluetooth serial port for your system
port = 'COM7'
baud_rate = 9600

# Connect to the Arduino Uno through the HC-05 Bluetooth module
ser = serial.Serial(port, baud_rate)
time.sleep(0.2)

def hey():
    ser.write(b'f') 
    time.sleep(0.5) 
    ser.write(b's') 
    time.sleep(1) 
    ser.write(b'b')
    time.sleep(1) 
    ser.write(b's')
    ser.write(b'r') # send the command to make the car go in a circle
    time.sleep(4) # wait for 5 seconds
    ser.write(b's') # send the command to stop the car
def getNumber(ar):#[0,1,1,0,0] ==>"01100"
    s=""
    for I in ar:
       s+=str(ar[I]);
       
    if(s=="00000"):#10001 
        return (0)
    elif(s=="01000"):
        return(1)
    elif(s=="01100"):
        return(2) 
    elif(s=="01110"):
        return(3)
    elif(s=="01111"):
        return(4)
    elif(s=="11111"):
        return(5) 
    elif(s=="01001"):
        return(6)
    elif(s=="01011"):
        return(7)      


# Continuously read data from the audio stream and transcribe it using the recognizer

# Create a Model object using a specified language model
model = Model(r"en")

# Create a KaldiRecognizer object using the model and a specified sample rate
recognizer = KaldiRecognizer(model, 16000)

# Create a PyAudio object
cap = pyaudio.PyAudio()

# Open an audio stream using the PyAudio object with specified parameters
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

# Start the audio stream
stream.start_stream()

while True:
    # Read 4096 frames from the audio stream
    data = stream.read(4096)
    # Check if the recognizer has finished transcribing the audio
    if recognizer.AcceptWaveform(data):
        # Load the result of the transcription as a JSON object
        result = json.loads(recognizer.Result())
        print(result)
        # Check if the keyword "start" is in the transcribed text
        if "start" == result['text']:
            print(result['text'])
            while True:
                data = stream.read(15360, False)
                recognizer.AcceptWaveform(data)
                result2 = json.loads(recognizer.Result())
                if "forward" == result2['text']:
                    print('forward')
                    ser.write("f".encode("utf-8"))
                elif "back" == result2['text']:
                    print('backward')
                    ser.write("b".encode("utf-8"))
                elif "left" == result2['text']:
                    print('left')
                    ser.write("l".encode("utf-8"))
                elif "right" == result2['text']:
                    print('right')
                    ser.write("r".encode("utf-8"))
                elif "stop" == result2['text']:
                    print('stop')
                    ser.write("s".encode("utf-8"))
                elif "hey buddy" == result2['text']:
                    print("hi ya 3aref")
                    hey()
                elif "mode" == result2['text']:
                    print('mode')
                    break
                else:
                    print(result2['text'])
        elif "hand" == result['text']:
            wcam, hcam = 640, 480
            capcam = cv2.VideoCapture(0)
            capcam.set(3, wcam)
            capcam.set(4, hcam)
#
#
#           
            startTime = -1
            prevSignal = ''

            readings = [0, 0, 0, 0, 0, 0]
            def clearArray():
                for i in range(0,6):
                    readings[i]=0

            signals = ['f', 'b', 'r', 'l', 's','d']
            def clearArray():
                for i in range(0,6):
                    readings[i]=0
            
            detector = htm.handDetector(detectionCon=0.75)
            while True:
                success,img=capcam.read()
                img = detector.findHands(img, draw=True )
                lmList=detector.findPosition(img,draw=False)
                #print(lmList)
                tipId=[4,8,12,16,20]
                if(len(lmList)!=0):
                    fingers=[]#[0|1|0|0|0]//01000
                    #thumb
                    if(lmList[tipId[0]][1]>lmList[tipId[0]-1][1]):#[4|cx|cy] lmList[4][1]
                            fingers.append(1)
                    else :
                            fingers.append(0)
                    #4 fingers
                    for id in range(1,len(tipId)):

                        if(lmList[tipId[id]][2]<lmList[tipId[id]-2][2]):
                            fingers.append(1)

                        else :
                            fingers.append(0)#01000
                    totFingers=getNumber(fingers)
                    
#   01000                                         1.3          1 fffffffffffffffffffffffffrfffffffff
                    if (startTime != -1 and time.time() - startTime > .25):
                        startTime = -1
                        maxValue = max(readings)#  65
                        maxIndex = readings.index(maxValue)#2   
                        clearArray()
                        if (prevSignal != signals[maxIndex]):
                            ser.write(signals[maxIndex].encode())
                            print(signals[maxIndex])# remember that signals = ['f', 'b', 'r', 'l', 's', 'd']  ,signals[0] ==> f

                        prevSignal = signals[maxIndex]


                    if (totFingers is not None) and (1 <= totFingers <= 7):
                        if startTime == -1:#if not , so the time has been already set
                            startTime = time.time()#it can be     [6,3,35,1,5,0] fffffffffffffffffffff3b 
                        readings[totFingers-1] += 1#[0,0,0,0,0,0]==>[1,0,0,0,0,0] -if only my index finger is up- readings[0]


                    cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)   
                    cv2.putText(img,str(getNumber(fingers)),(45,375),cv2.FONT_HERSHEY_PLAIN,
                                                 10,(255,0,0),20)  



                cv2.imshow("image",img)
                if(cv2.waitKey(1) & 0xFF== ord('q')):
                    break
