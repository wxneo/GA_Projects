# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) CrowdSenseAI: Avert Crowd Crushing with Deep Learning

![Streamlit App](https://github.com/wxneo/GA_Projects/blob/main/Capstone/image/capstone_demo_short02.gif)

## Background
In today's world, public gatherings and events draw enormous crowds, making crowd safety a paramount concern. Crowd forces can escalate to levels beyond control, leading to tragic incidents of compressive asphyxia, where individuals are crushed due to excessive pressure. Tragically, media sensationalism often misrepresents the true causes of crowd disasters, attributing them to "panic" and "stampede," when in reality, inappropriate utilization of space and systematic failures in design and management are the real reason behind most cases. The stark reality is that major incidents arise from crowd compressive forces, not mere trampling.

The recent tragedy that occurred in South Korea on the night of 29 October 2022 serves as a somber reminder of the urgent need for effective crowd management and safety measures. During a Halloween party in Seoul, at least 150 people lost their lives, and approximately 150 others were injured in a devastating crush. The incident unfolded in the narrow streets of a neighborhood in the bustling South Korean capital, where hundred thousand of participants had gathered.

The tragedy that happen in South Korea was just one such event. There were many more around the world and this proves that time after time, lessons were not learnt from each incident. Such a calamitous event underscores the criticality of addressing crowd crushing disasters. The loss of lives and injuries in this incident highlight the devastating consequences of insufficient crowd control and the mismanagement of crowded spaces. It emphasizes the pressing need for technological interventions that can accurately detect and count crowd capacity, enabling the implementation of early warning systems to avert such tragedies in the future.

Source:
<br>[1] https://www.gkstill.com/ExpertWitness/CrowdDisasters.html
<br>[2] https://www.theguardian.com/world/2022/oct/29/the-deadliest-crowd-crushes-of-the-last-decade

<br>


## Problem Statement
The objective of this project is to address the critical issue of crowd safety during public gatherings and events. The primary problem to be tackled is the prevention of crowd crushing disasters caused by overcrowding and mismanagement of crowded spaces. To mitigate such incidents and protect lives, this project aims to develop a sophisticated deep learning model that can accurately detect crowd presence, estimate crowd capacity in real-time, and trigger early warnings to authorities in case of hazardous conditions. By providing an intelligent solution to address crowd-related risks, this project seeks to create safer environments for public assembly and gatherings, ultimately contributing to the preservation of human lives.

**Safety:** Address the critical issue of crowd safety during public gatherings and events.
<br>**Control:** Prevention of crowd crushing disasters caused by overcrowding and mismanagement of crowded spaces.
<br>**Detection:** Develop sophisticated deep learning model for real-time crowd presence detection.
<br>**Mitigation:** Early warnings to authorities in hazardous conditions to protect lives.


## Datasets:
The image datasets "peoplecounter" were obtained from Roboflow Universe repository. It comprises of 4161 images with labels to train the machine learning model on identifying a person's head or face.

**peoplecounter-xqtwr_dataset:** <br>
title = peoplecounter Dataset <br>
type = Open Source Dataset <br>
author = embien <br>
url = https://universe.roboflow.com/embien-7xos5/peoplecounter-xqtwr <br>
journal = Roboflow Universe <br>
publisher = Roboflow <br>
date = May 2023 <br>


## Modeling
Model training was carried out on 3 seperate jupyter notebook using Google Colab as the model requires very high computational power to process the images. With Google Colab, I had access to powerful GPU (NVIDIA A100-SXM4-40GB, 40514MiB) that help reduced the run time required for the image training.

|        **File**       | **Model** | **epoch** | **batch** |                                                                                   **Remark**                                                                                   |
|:---------------------:|:---------:|:---------:|:---------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|   yolov5_model.ipynb  |  YOLOv5s  |    100    |     16    | Training done on train set and validated on all 3 different dataset (train, valid, test).                                                                                                           |
| yolov8_model_01.ipynb |  YOLOv8s  |    100    |     8     | Training done on train set and validated on all 3 different dataset (train, valid, test). <br>Unable to set default batch size of 16 due GPU out of memory with Google Colab A100 GPU. |
| yolov8_model_02.ipynb |  YOLOv8s  |    200    |     8     | Training done on train set and validated on all 3 different dataset (train, valid, test). <br>Unable to set default batch size of 16 due GPU out of memory with Google Colab A100 GPU. |
<br>

## Summary of Model Perforamance

**Model Performance Overview**

|                    |  mAP50 (Train) |   mAP50 (Val)   |   mAP50 (Test)  | Precision (Train) | Precision (Val) | Precision (Test) |    Recall (Train)   |     Recall (Val)    |    Recall (Test)    |
|--------------------|:-------------:|:-------------:|:-------------:|:---------------:|:-------------:|:--------------:|:-------------:|:-------------:|:-------------:|
|  YOLOv5 (Baseline) |     46.7%     |     45.6%     |     45.8%     |      70.7%      |     69.6%     |      69.0%     |     37.3%     |     36.5%     |     36.9%     |
| YOLOv8 (100 Epoch) | 55.1% (+8.4%) | 52.9% (+7.3%) | 54.6% (+8.8%) |  75.6% (+4.9%)  | 73.8% (+4.2%) |  73.7% (+4.7%) | 44.4% (+7.1%) | 42.3% (+5.8%) | 44.6% (+7.7%) |
| YOLOv8 (200 Epoch) | 56.6% (+9.9%) | 54.1% (+8.5%) | 55.7% (+9.9%) |  77.6% (+6.9%)  | 74.8% (+5.2%) |  74.9% (+5.9%) | 45.3% (+8.0%) | 43.0% (+6.5%) | 45.3% (+8.4%) |

<br>


## Key Insights & Recommendations

* The model's predictions are influenced by the confidence level, which can be adjusted to meet specific requirements. Higher confidence levels result in stricter detection, potentially missing some objects that might be relevant for this project.
* To define overcrowding, it is crucial to consider the crowd density, which becomes a concern when it exceeds 4-5 people per square meter. Determining the area of surveillance is essential in setting the triggering limits for the early warning system.
* For optimal implementation of the early warning system, the surveillance footage should be static and provide a top-down view of the crowd area. This setup offers better coverage and monitoring capabilities.
* As the detections are conducted frame by frame from the input source, introducing a slight delay between each frame allows for a smoother frame rate and helps mitigate issues related to buffering or lagging.

## Limitations & Future Works
* The model training for this project requires a powerful GPU, and Google Colab is the chosen platform, which incurs a cost of S$14 per 100 credits.
* Despite using a powerful GPU like NVIDIA A100-SXM4-40GB, memory constraints have led to reduced batch sizes for YOLOv8 models. Upgrading to more powerful hardware will enable extensive training and model performance tuning.
* The current limitations on model performance stem from limited datasets and training time. Significantly larger datasets and sophisticated hardware with longer training epochs will substantially improve model accuracy.
* Estimating the crowd size limit before it becomes dangerous relies on area information not directly available from the footage. To address this, manual trigger limit settings are currently used, but automation can be achieved through area input or floor area calculations based on mapping data in future work.
* The existing early warning system includes visual on-screen and audio warnings. In the future, automation can extend to trigger alert messages to designated mobile phones and email accounts, notifying the authorities for immediate action.

## Conclusion
* Preemtive: Closing off high-risk areas during public gatherings and events before they become overcrowded.
* Proactive: Deployment of security personnel, regulation of crowd control at congregation areas and potential chokepoints.
* Predictive: Utilising CCTVs and drones with deep learning detection model to monitor the crowd capacity & provide early warning.

## Reference
[1] https://www.folio3.ai/blog/best-model-for-person-detection/
<br>[2] https://towardsdatascience.com/on-object-detection-metrics-with-worked-example-216f173ed31e
<br>[3] https://github.com/ultralytics/ultralytics/issues/2789
<br>[4] https://www.channelnewsasia.com/singapore/singapore-crowd-control-measures-police-events-seoul-itaewon-crush-3105106#:~:text=%22They%20may%20also%20include%20cordoning,and%20to%20respond%20to%20incidents.
<br>[5] https://www.theguardian.com/world/2022/oct/31/how-did-the-seoul-itaewon-halloween-crowd-crush-happen-unfolded-a-visual-guide#:~:text=3-,A%20densely%20packed%20group%20exert%20pressure%20on%20each%20other%2C%20but,effect%20of%20similar%20holes%20elsewhere.

