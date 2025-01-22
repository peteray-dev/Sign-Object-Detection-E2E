# Sign-Object-Detection-E2E

## Emotional AI for Mental Health Insight

# Watch the Demo



https://github.com/user-attachments/assets/471feb7d-c4b8-49a8-9650-a25ed8dc3246

### Project Overview
This project aims to leverage computer vision and artificial intelligence (AI) to gain mental health insights through facial expression analysis. The app captures facial expressions and determines the user's emotional state, including emotions such as happiness, fear, disgust, surprise, anger, and neutrality.

The app is built on a custom YOLOv5 (You Only Look Once) model for emotion detection, and it is designed to offer mental health insights based on real-time facial expression analysis.

#### Technology Stack
YOLOv5 – For custom object detection and emotion classification.
Python – For data processing, model training, and script automation.
Jenkins – For continuous integration and deployment.
Docker – For containerization and consistent deployment across different environments.
AWS (Amazon Web Services) – For cloud storage and deployment, including using S3 buckets for storing data.
OpenCV – For image and video processing to capture facial expressions.
#### Key Features
Facial Expression Detection: The app detects and classifies emotions based on facial expressions using a custom YOLOv5 model.
Emotion Classification: The app identifies a wide range of emotions, including happiness, fear, disgust, surprise, anger, and neutrality.
Data Ingestion & Validation: Python scripts are used for efficient data ingestion, validation, and preprocessing.
Model Training: A custom YOLOv5 model is trained on a labeled dataset to recognize different facial expressions accurately.
Cloud Integration: Data is pushed to an AWS S3 bucket for easy storage and retrieval.
#### Workflow
Data Collection: The first step is gathering a dataset of facial expressions that is pre-labeled with emotions. This data is sourced from publicly available datasets.
Data Ingestion & Preprocessing: A Python script handles data ingestion, cleaning, and validation to ensure the dataset is in the correct format for model training.
Model Training: The custom YOLOv5 model is trained on the facial expression dataset. The model learns to detect various emotions based on facial features.
Emotion Classification: Once the model is trained, it can classify emotions from new, unseen images in real-time.
#### Deployment:
The entire application is containerized using Docker, ensuring that the environment is consistent across different systems.
Jenkins automates the deployment process, ensuring continuous integration and updates.
The app is deployed on AWS, using S3 buckets for data storage and easy retrieval of model outputs.

#### Detailed Workflow Breakdown
Step 1: Data Ingestion
A Python script is used for ingesting image data into the system. It takes in raw images, validates them to ensure proper format, and prepares them for model training.

Step 2: Data Validation
Another script ensures the images are in the correct shape and contain the appropriate metadata (labels for emotions). This step is crucial for accurate model training.

Step 3: Model Training
The YOLOv5 model is customized to detect facial expressions. The model is trained with a labeled dataset and adjusted for optimal accuracy in detecting multiple emotional states. The training process includes:

Hyperparameter tuning.

Validation and testing of the trained model.

Output generation of prediction probabilities for emotions.

Result

![image](https://github.com/user-attachments/assets/dd6a9596-5ec0-4243-8011-2a8b56281b04)


Step 4: Emotion Classification
Once the model is trained, it is used for real-time emotion classification from facial images. The model is embedded into the application and processes images from the camera or uploaded media files.



Step 5: Data Storage
Results from emotion predictions are stored on AWS S3 buckets for easy access and long-term storage. This cloud integration enables remote access and scalability.

Step 6: Deployment
Using Docker, the application is packaged into containers, ensuring a seamless experience across different environments. Jenkins is then used to automate the deployment process. The app is deployed on AWS, where it is accessible from anywhere.





<!-- conda create -n signLang python=3.7 -y -->

<!-- conda activate signLang -->
<!-- pip install -r requirements.txt -->

## Workflows

-constants

-config_entity

-artifact_entity

-component

-pipeline

-app.py
