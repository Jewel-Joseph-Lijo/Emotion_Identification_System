# Human Emotion Detection from Text

A personal machine learning project that detects **human emotions from text** using Natural Language Processing (NLP). The system classifies user-entered sentences into one of six emotions and provides predictions through a simple **Tkinter-based desktop interface**.

<img width="741" height="639" alt="Screenshot 2026-01-27 230711" src="https://github.com/user-attachments/assets/82ecbe3d-7007-4fad-a971-69ff16759a05" />

<img width="741" height="637" alt="Screenshot 2026-01-27 231004" src="https://github.com/user-attachments/assets/754b2f0f-6fd2-4cd1-9b0d-06cdd7e72b7f" />

---

## 📌 Project Overview

Human emotions are often expressed through written text such as messages, comments, or short statements. This project focuses on identifying the **underlying emotion** in a given sentence using machine learning techniques.

The model is trained on a labeled text dataset and predicts one of the following emotions:

* **Joy**
* **Sad**
* **Fear**
* **Anger**
* **Surprise**
* **Love**

---

## How to Run the Project

1. Make sure you have **Python 3.14** installed.
2. Install required libraries.
3. Run the Emotion_Identification.py file.

---

## 🧠 Machine Learning Approach

### Text Preprocessing

* Converting text to lowercase
* Removing English stop words
* Converting text into numerical features using **TF-IDF Vectorization**
* Using unigrams and bigrams to capture contextual meaning

### Algorithm Used

* **Logistic Regression**

Logistic Regression was selected due to its strong performance on high-dimensional sparse text data and its ability to learn meaningful feature weights.

---

## 📊 Model Performance

* **Accuracy:** ~91%

Some overlap between emotions such as **Joy, Love, and Surprise** is expected due to the natural ambiguity of human language.

---

## 🖥️ User Interface

The project includes a **Tkinter-based graphical user interface (GUI)** with:

* A text input box for entering a sentence
* A button to trigger emotion prediction
* An output field displaying the predicted emotion

This interface makes the system easy to test and demonstrate.

---

## 🛠️ Technologies Used

* **Python**
* **Tkinter** (GUI)
* **Pandas** (data handling)
* **Scikit-learn** (machine learning & NLP)
* **TF-IDF Vectorizer**

---

## 📜 Dataset Information

* **Dataset Name: Sentiment and Emotion Analysis Dataset** Emotion Detection from Text
* Dataset sourced from **Kaggle**
* Contains labeled text samples across six emotion categories (Joy, Sad, Fear, Anger, Surprise, Love)
* Licensed under the **Apache License 2.0**
* The dataset is permitted for use, modification, and redistribution with attribution

---

## ⚠️ Limitations

* Emotion detection from text is inherently ambiguous
* Some emotions share similar vocabulary, leading to occasional overlap
* Context beyond text (tone, facial expression, intent) is not available

---

## 🚀 Future Enhancements

* Display prediction confidence scores
* Show top two predicted emotions
* Improve GUI design and usability
* Deploy the model as a web-based application
* Explore advanced NLP models for improved semantic understanding

---

## 📌 Conclusion

This project demonstrates how machine learning and natural language processing can be used to detect emotions from text with high accuracy. The combination of TF-IDF and Logistic Regression provides an efficient and reliable solution, making this a strong personal project and a foundation for future enhancements.
