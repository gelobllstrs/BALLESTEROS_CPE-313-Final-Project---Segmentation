# CPE-313 Final Project Segmentation

👨‍💻 About Me

I am Angelo Ballesteros, a Computer Engineering student at the Technological Institute of the Philippines – Quezon City (TIP QC). This project was completed as part of the requirements for CPE313 Data Science Track Elective 3, focusing on applying machine and deep learning techniques in real-world scenarios.

📌 Description of the Project:

This project aims to develop an accurate fire detection system through instance segmentation of fire images using a specialized dataset from Roboflow, enhancing early fire detection and safety monitoring applications.

I implemented and trained three state-of-the-art deep learning models for instance segmentation:

🧠 **YOLOv11** – a recent version of the well-known YOLO object detection framework enhanced for instance segmentation.

⚡ **YOLOv8** – the latest version of YOLO providing improved precision and speed.

🎯 **Mask R-CNN** – a reliably recognized two-phase detector known for excellent instance segmentation quality.
    
Every model underwent training and assessment using the identical dataset to evaluate performance regarding accuracy, speed, and segmentation quality.

📊 **Evaluation Metrics:**

I used the following key performance metrics:

➡️ mAP@0.50 and mAP@0.50:0.95 (mean Average Precision) as the primary indicators of detection quality

➡️ Precision, Recall, and Accuracy as supporting performance metrics

🧪 **Model Testing:**

Model testing and visualization can be performed through an interactive Streamlit application developed for this project.

📁 **Model Uploads:**

Due to file size limitations, only the YOLOv11 .pt model file was uploaded following the submission guidelines. The Mask R-CNN model was not uploaded because of its large file size.

🏆 **Final Model Choice**

I used the YOLOv8 model in my final implementation because it achieved the highest metrics in terms of accuracy, speed, and segmentation quality among the models I evaluated.
