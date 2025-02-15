# Drone Detection 
 
This project utilizes **YOLOv8** for real-time drone detection, trained on a **custom dataset** and deployed on both a **DJI Tello drone** and a **webcam**.

![Image](https://github.com/user-attachments/assets/d2283d8e-79f6-4bf4-a886-7ea7a524865a)

the video ref: [Here](https://www.youtube.com/watch?v=0UqXRkjDJGo).

## Project Overview  
- **Model Training & Testing**: Conducted in **Google Colab**. 
- **Deployment**: Runs on a webcam and DJI Tello drone.
- **Test Data**: Sample **images** for evaluation.  



## Model Training & Testing  
Model training and testing are **performed in Google Colab**.
- **`AI_DroneDetection.ipynb`** 



## Deploying 

### Dependencies to be installed
- python 3.10
- opencv
- ultralytics
- djitellopy → to control dji tello drone 

### Deployment Files
- **`deployment/`**
   -  **`drone_detection_tello.py`** → Runs YOLO detection on Tello.
   -  **`drone_detection_webcam.py`** → Runs YOLO detection on webcam.
   -  **`best.onnx`** → trained model.

## Testing & results 

- **`test_data/`** → test data files.
- **`results/`**  → test data files after detection.

## Refrences

 - Drone Dataset: [Kaggle - Drone Detection Dataset](https://www.kaggle.com/datasets/muki2003/yolo-drone-detection-dataset?resource=download)

- YOLO Training Docs: [YOLO Training Guide](https://docs.ultralytics.com/modes/train/#resuming-interrupted-trainings)
- YOLO Predict Docs: [YOLO Predict Guide](https://docs.ultralytics.com/modes/predict/#inference-sources)
