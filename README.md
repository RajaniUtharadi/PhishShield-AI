# 🛡️ PhishShield AI

An AI-powered phishing URL detection system built using Python, Streamlit, and Machine Learning.

PhishShield AI analyzes suspicious URL characteristics such as:

* URL length
* Special symbols
* IP address usage
* Suspicious keywords
* HTTPS usage

and predicts whether the URL is:

* ✅ Safe
* ⚠️ Suspicious
* 🔴 Dangerous

---

# 🚀 Features

* Premium cybersecurity UI
* Real-time URL analysis
* Machine Learning based prediction
* Threat score detection
* Suspicious keyword analysis
* IP address detection
* Beginner-friendly project
* Fast lightweight deployment

---

# 🧠 Tech Stack

* Python
* Streamlit
* Scikit-learn
* Joblib
* Random Forest Classifier

---

# 📂 Project Structure

```bash
phishshield-ai/
│
├── app.py
├── feature.py
├── train_model.py
├── model.pkl
├── requirements.txt
└── README.md
```

---

# ⚙️ Complete Installation Process

## 1️⃣ Install Python

Download and install Python from:

[Python Official Website](https://www.python.org/downloads/?utm_source=chatgpt.com)

IMPORTANT:
During installation enable:

```bash
✅ Add Python to PATH
```

---

## 2️⃣ Verify Python Installation

Open terminal / PowerShell:

```bash
python --version
```

Expected output:

```bash
Python 3.x.x
```

---

## 3️⃣ Clone Repository

```bash
git clone https://github.com/your-username/phishshield-ai.git
```

---

## 4️⃣ Navigate to Project Folder

```bash
cd phishshield-ai
```

---

## 5️⃣ Install Required Libraries

```bash
pip install streamlit pandas scikit-learn joblib
```

OR

```bash
pip install -r requirements.txt
```

---

# 📦 requirements.txt

Create a file named:

```bash
requirements.txt
```

Add:

```txt
streamlit
pandas
scikit-learn
joblib
```

---

# 🧠 Train Machine Learning Model

Run:

```bash
python train_model.py
```

This generates:

```bash
model.pkl
```

---

# ▶️ Run the Application

```bash
python -m streamlit run app.py
```

---

# 🧪 Test URLs

## ✅ Safe URLs

```bash
https://google.com
https://github.com
https://microsoft.com
https://openai.com
```

---

## ⚠️ Suspicious URLs

```bash
http://paypal-login-security-alert.com
http://verify-bank-account.xyz
http://secure-login-update.ru
```

---

# 🧠 Machine Learning Workflow

1. URL entered by user
2. Features extracted from URL
3. Features passed into Random Forest model
4. Model predicts phishing probability
5. Threat score displayed visually

---

# 🔍 Features Extracted

* URL Length
* Number of dots
* Hyphen count
* @ symbol detection
* HTTPS presence
* IP address detection
* Suspicious keyword analysis

---

# ✅ Conclusion

PhishShield AI is a simple Machine Learning based cybersecurity project that helps detect suspicious and phishing URLs using URL feature analysis. The project combines AI, cybersecurity, and web development concepts into an interactive real-time detection system. It is useful for learning, portfolio building, and hackathon demonstrations.
