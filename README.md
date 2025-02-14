# Drone Detection 
 
This project utilizes **YOLOv8** for real-time drone detection, trained on a **custom dataset** and deployed on both a **DJI Tello drone** and a **webcam**.


## Project Overview  
- **Model Training & Testing** → Conducted in **Google Colab**. 
- **Deployment** → Runs YOLOv8 **inference on DJI Tello and webcam**.  
- **Test Data** → Sample **images** for evaluation.  



## Model Training & Testing  
Model training and testing are **performed in Google Colab**.
- **`AI_DroneDetection.ipynb`** 



## Deploying 
After training, the **trained model** has been deployed on the **webcam & dji tello drone**.  

### Dependencies to be installed
- python 3.10
- opencv
- numpy 
- djitellopy → to control dji tello drone 

### Deployment Files
- **`deployment/`**
   -  **`drone_detection_tello.py`** → Runs YOLO detection on Tello.
   -  **`drone_detection_webcam.py`** → Runs YOLO detection on webcam.
   -  **`best.onnx`** → trained model.

## Testing & results 

- **`test_data/`**  

- **`results/`**


## Refrences

 - Drone Dataset: [Kaggle - Drone Detection Dataset](https://www.kaggle.com/datasets/muki2003/yolo-drone-detection-dataset?resource=download)

- YOLO Training Docs: [YOLO Training Guide](https://docs.ultralytics.com/modes/train/#resuming-interrupted-trainings)
- YOLO Predict Docs: [YOLO Predict Guide](https://docs.ultralytics.com/modes/predict/#inference-sources)
