## SMS Spam detection application
This NLP model developed for this application was based on Kaggle dataset
https://www.kaggle.com/uciml/sms-spam-collection-dataset. The API service is developed using 
Django REST framework hosted in docker containerized platform.

### Text Preprocessing
Text preprocessing is an approach for cleaning and preparing text data for use in a specific context.
This is very essential as text data can have different formats, dialects and they could be
other stuff that could add noise to the data.

NLTK libraries is used for
+ Regex - remove unnecessary charaters and formatting in text
+ Tokenization - convert a sentence to smaller chunks
+ Normalization - stemming the words (capture the root word)

### Machine Learning models
+ Naive-Bayes
+ Decision tree classifier
+ Balanced bagging classifier

F1-score evaluated on all three model's performance on test data and for the provides
dataset 'DecisionTreeClassifier' has better metrics
```
Decision Tree Accuracy: 97.36842105263158

Precision-Recall-F1_Score:
              precision    recall  f1-score   support

           0       0.98      0.99      0.98       728
           1       0.91      0.88      0.90       108

    accuracy                           0.97       836
   macro avg       0.95      0.93      0.94       836
weighted avg       0.97      0.97      0.97       836
```

### Kubernetes - Deploy the containerized application
#### Creating K8s Pod and Services
+ Pod : k8s-pod.yaml
+ Service
  + NodePort: k8s-svc-np.yaml
  + LoadBalancer: k8s-svc-lb.yaml

#### Port Info
```shell
NodePort: 31111
ContainerListeningPort: 8000
ClusterPort: 80
```

#### Accessing API
Kubernetes Clusters with one node must use services of type NodePort
* Single Node Cluster _(NodePort)_ `http://<nodePublicIP>:31111/checkSpam/`
* Multiple Node Cluster _(LoadBalancer)_ `http://<loadBalancerPublicIP>/checkSpam/`
