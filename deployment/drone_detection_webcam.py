import cv2
from ultralytics import YOLO

# Drone Detection Trained model
model = YOLO('best.onnx')

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while True:

    success, frame = cap.read()
    if not success:
        print("Failed to grab frame")
        break

    results = model.predict(frame, conf=0.5)  # confidence threshold 0.5
    
    annotated_frame = results[0].plot()
    
    cv2.imshow("DroneDetection", annotated_frame)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
