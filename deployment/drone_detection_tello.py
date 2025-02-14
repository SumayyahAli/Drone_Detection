import cv2
import numpy as np
from djitellopy import Tello
from ultralytics import YOLO


model = YOLO('best.onnx')


sumayyah = Tello()
sumayyah.connect()
sumayyah.streamon()

#---------------------[Functions]----------------------------
def controlTello():
    # Basic flight commands
    sumayyah.takeoff()
    sumayyah.move_up(50)
    #sumayyah.rotate_counter_clockwise(90)

def BatteryStatus():
    return sumayyah.get_battery()


def VideoStreamingON():
    global prev_frame
    frame = sumayyah.get_frame_read().frame
    frame = cv2.resize(frame, (640, 500))

    # ++++++[Detection]++++++++
    results = model.predict(frame)
    annotated_frame = results[0].plot()
    cv2.imshow("Drone Detection", annotated_frame)
    #cv2.imshow("Original", frame)
    return True

def TelloLand():
    sumayyah.streamoff()
    sumayyah.land()

# -------------------------------------------------------------

if __name__ == "__main__":
    controlTello()

    run = True
    while run:
    
        battery = BatteryStatus()
        print(f"Battery status: {battery} %")
        
        if not VideoStreamingON():
            break
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            run = False
            break
            
    TelloLand()
    cv2.destroyAllWindows()
