# Phishing URL Detection 
![image](https://raw.githubusercontent.com/hgusweldeyowhanes/website-Phishing-detector/main/images/legitmate.PNG)
![image](https://raw.githubusercontent.com/hgusweldeyowhanes/website-Phishing-detector/main/images/phishing.PNG)

## Table of Content
  * [Introduction](#introduction)
  * [Installation](#installation)
  * [Directory Tree](#directory-tree)
  * [Result](#result)
  * [Conclusion](#conclusion)


## Introduction

The Internet has become an indispensable part of our daily lives. However, with its rapid growth, it has also created new opportunities for malicious activities such as phishing. Phishers exploit human trust through social engineering or by creating mockup websites that closely resemble legitimate ones. Their goal is to steal sensitive information such as account IDs, usernames, passwords, and even financial data from individuals and organizations.
One of the most effective approaches to counter this challenge is Machine Learning (ML). Unlike static rule-based systems, ML models can learn from data, identify hidden patterns, and adapt to the ever-changing tactics of phishers. Since most phishing websites share common characteristics, machine learning becomes a powerful tool in distinguishing between legitimate and malicious sites.

This project demonstrates how machine learning techniques can be applied to detect phishing websites with high accuracy.


## Installation
This project is developed using Python 3.9.2.
If you don’t have Python installed, download it from the official website [here](https://www.python.org/downloads/). If you are using an older version of Python, upgrade it to the latest version. You can also upgrade pip to ensure you have the latest package manager

```bash
python -m pip install --upgrade pip
```
clone repository[clone]
git clone https://github.com/hgusweldeyowhanes/website-Phishing-detector.git
cd website-Phishing-detector

create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # On Linux/Mac
.venv\Scripts\activate      # On Windows
```
install dependency
```bash
pip install -r requirements.txt
```

## Directory Tree 
```
├── phishing
│   detector app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── apps.py
│   ├── admins.py
│   ├── ml
│       ├── phishing_rf_model.joblib
│       ├── feature_names.json
│       ├── utils.py
│   static
│   ├── style.css
│   templates
│   ├── index.html
│   Phishing URL Detection.ipynb
│   imaages
│   ├── legitmate.png
│   ├── phishing.png
│   Phishing
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   README.md
│   manage.py
│   phishing.csv
│   requirements.txt


```

## 🛠️ Technologies Used  

![](https://forthebadge.com/images/badges/made-with-python.svg)  

- **Backend Framework:** [<img src="https://static.djangoproject.com/img/logos/django-logo-positive.png" width=150>](https://www.djangoproject.com/)  
- **Machine Learning Algorithm:** 🏆 **Random Forest Classifier** (from [scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html))  

### Core Libraries  
[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/3/31/NumPy_logo_2020.svg" width=200>](https://numpy.org/doc/)  
[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg" width=200>](https://pandas.pydata.org/)  
[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg" width=100>](https://matplotlib.org/)  
[<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/)

## Result

Accuracy of the model used for URL detection
<br>

<br>

||ML Model|	Accuracy|  	f1_score|	Recall|	Precision|
|---|---|---|---|---|---|
1|	Random Forest|	                0.95|	0.958|	0.95|	0.95|


Feature importance for Phishing URL Detection 
<br><br>
![image](https://github.com/hgusweldeyowhanes/website-Phishing-detector/blob/main/images/top_feature.PNG)




## Conclusion
1. Model Development: A Phishing URL Detector was developed using the Random Forest Classifier, capable of analyzing URL features to distinguish between legitimate and phishing websites. 
2. Backend Implementation: The application uses Django for the backend, providing a secure and responsive web interface for users.
3. Accuracy and Performance: The model demonstrates strong predictive performance, effectively identifying phishing attempts even as attackers evolve their techniques. 
4. Scalability and Flexibility: The combination of machine learning and web technologies allows for future expansion, including integration with larger security platforms or real-time monitoring systems.
5.Practical Impact: This project highlights how machine learning can be applied to improve cybersecurity, offering a practical tool to reduce online threats.