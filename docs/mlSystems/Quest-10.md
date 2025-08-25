<h1 align='center'> Model Deployment and Monitoring </h1>

1. **What is model deployment, and why is it challenging?**

<details>
<summary>Answer</summary>

1. A process of packaging trained model and integrate it into the production system using REST API, where model can serve prediction on new unseen data to the user. Hence It bridges the gap between developement and serving to the end users(real world usecase). 

2. Deployment into the production system become challenging due to the following 
   - Enviroment Mismatch from Developement to Deployment
   - Model Serialization : Choosing the right format (e.g., Joblib, Pickle, ONNX, TorchScript) that is portable and secure.
   - Infrastructure Readiness : We have to setup servers, containers or use cloud services to serve prediction at scale
   - Latency and Throughput Issues :  Ensuring low prediction time, especially for real-time applications.
   - Monitoriing and Observability : Detecting model or data drift or outage quickly
   - Data and Model Version Control : Managing multiple version of model and dataset and track each version of model live.
</details>

2. **Can you describe how many different ways to deploy a machine learning model ?**

<details>
<summary> Answer </summary>

There are multiple ways to deploy a machine learning model, each suited to different use cases, latency requirements, infrastructure, and scalability needs. Thus, comprehensive list of main deployment strategies are as follows
1. Batch Inference : We perform predict on large batches of data at scheduled intervals (e.g., nightly reports or churn scoring).It only usefull when we don't need  real-time response. Tools : Apache Spark, Apache Airflow, Azure Data Factory etc.
2. Online(Real-time) Inference : Our model serve instant predictions through APIs for use cases needing low latency (e.g., recommendation systems, real-time fraud detection). It uses frameworks like Flask, FastAPI, TensorFlow Serving, TorchServe etc to build API.
3. Edge Deployment : We deploy our models to the edge devices like mobile, IoT, embedded systems etc for localized or offline inference. It uses frameworks like TensorFlow Lite, ONNX, Apple Core ML etc
4. Streaming Deployment : Continuously ingest and infer data streams in near real-time (e.g., sensor data, financial market feeds). Tools: Kafka + Faust, Spark Streaming, Apache Flink.
5. Containerized Deployment : Package models and dependencies into containers like Docker for environment consistency and portability. Orchestrate with Kubernetes, AWS ECS for scaling and management.
6. Model-as-a-Service (MaaS) : Use managed cloud platforms that provide hosting, scaling, and monitoring out of the box. Platforms: AWS SageMaker, Azure Machine Learning, Google Vertex AI, Databricks Model Serving.
</details>


3. **What is a REST API, and how do you use it to deploy models?**
<details>
<summary> Answer </summary>
</details>

4. **Can you explain CI/CD Pipeline into the MLOps ?**
<details>
<summary> Answer </summary>
</details>

5. **How do you monitor the performance of a deployed model?**
<details>
<summary> Answer </summary>
</details>

6. **What are some common tools for model monitoring and logging?**
<details>
<summary> Answer </summary>
</details>


7. **Describe a scenario where you had to roll back a deployed model.**
<details>
<summary> Answer </summary>
</details>

8. **How do you handle model drift in production?**

9. **What is canary deployment and why is it usefull ?**

10. **Explain the concept of A/B testing in the context of model deployment.**

11. **11. What are the key considerations for scaling a machine learning model?**

12. **How do you ensure the security of your deployed models?**


## template : 
<details>
<summary> Answer </summary>
</details>

## References and Reading Materials
[1]. https://skphd.medium.com/model-deployment-and-monitoring-interview-questions-and-answers-68cd7f48c29b \
[2]. https://www.datacamp.com/blog/mlops-interview-questions \
[3]. https://www.micro1.ai/interview-prep/mlops-engineer-interview-questions \