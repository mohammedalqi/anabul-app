# Bangkit Team C22-PS164, Anabul
![Anabul Logo Transparent](https://github-production-user-asset-6210df.s3.amazonaws.com/18515456/246032566-fb77a4be-f00a-4d3d-b841-d067a4aa1d60.png)
# Product-based Capstone Bangkit Academy 2022
# Member:
1. Machine Learning:
- Muhammad Ashim Izzuddin (M010DSX1883) - Institut Informatika Dan Bisnis Darmajaya
- Muhammad Galih Fadhillah (M151DSX1906) - Universitas Brawijaya
- Dendi Mulyana (M295DSX0304) - Universitas Padjadjaran
2. Cloud Computing
- Muhammad Zidane Vigamada (C360DSX0879) - Universitas Telkom
- Muhammad Alqi Fahrezi (C125DKX4533) - UIN Jakarta
3. Mobile Development
- Bagas Satria Fadhlillah (A181DSX3478) - Universitas Indonesia
# Final Selected Themes:
Human Healthcare and Living Wellbeings
# Title of The Project:
Anabul - Your Guide to Happy and Healthy Pets!
# Summary of Project:
The pet economy industry in Indonesia experienced growth during the Covid-19 pandemic, causing the habit of adopting animals to increase. Data from LandX in 2021 shows that 47% of respondents keep cats, and 10% of respondents keep dogs at home. The problem statement of this project is that many people have difficulty finding knowledge such as cat/dog classifications, breeds, food types, and diseases. In addition, the number of abandoned animals causes the need for an application with social features such as adoption, donation, and consultation. Research questions are how do cat/dog lovers find knowledge related to the classification of cats and dogs along with their breeds to food type information? How do we integrate the application's social features, such as adoption, donation, and consultation? What is the impact of this application on the community of cat and dog lovers in Indonesia? Background 
information is that there are many characteristics, uniqueness, and types of cats and dogs that are complicated and time-consuming to learn. This project should be completed to make it easier for cat and dog lovers to find knowledge about cats and dogs integrated with social features such as adoption, donation, and consultation. This project should be completed to make it easier for cat and dog lovers to find knowledge about cats and dogs integrated with social features such as adoption, donation, and consultation.
# Step to Replicate:
1. Machine Learning:
- Dataset ingestion (from Kaggle)
- Preprocessing (binary encoding, dividing data, check numbers of data, and scaling the data to prepare for the ML training)
- Define deep learning model using TensorFlow
- Save and load model to evaluate model performance
2. Cloud Computing:
- Create a project on Google Cloud Platform
- Set default region as asia-southeast2 (Jakarta)
``$gcloud config set compute/region asia-southeast2`` 
- Project Structure for Deployment
  - main.py
  - skin_disease_dogs.h5 (ML model)
  - .dockerignore
  - Dockerfile
  - requirements.txt
-  Create a project on Firebase and activate authentication with Google.
-  Cloud Storage Browser page
   - Create bucket
   - Name your bucket : "-----"
   - Location type : region
   - Choose where to store your data = asia-southeast2
   - Leave the default setting
   - Create bucket
-  Model Deployment
    -  [Install GCloud SDK](https://cloud.google.com/sdk/docs/install)
    -  On VSCode Terminal run: ``gcloud init``
    -  Select your account and configure your project (follow the instructions)
    -  Deploy to Cloud Run:
        - ``gcloud builds submit --tag gcr.io/<project_id>/predict_dog_disease``
        - ``gcloud run deploy --image gcr.io/<project_id>/predict_dog_disease --platform managed``
4. Mobile Development:
- 
# Technology Used:
- Tensorflow
- Google Drive
- Google Colab
- VSCode
- Cloud Run
- Cloud Storage
- Firebase for Authentication
- Postman
# Budget:
Google Cloud Subscription $300
# Dataset
- Dog photo
