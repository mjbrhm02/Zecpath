# Zecpath AI System
Zecpath AI System is a modular, microservices-oriented AI backend designed to automate the hiring lifecycle.
This project demonstrates the foundational architecture of AI-driven recruitment, including resume parsing, ATS scoring, and decision-making.

## 🎯 Objectives

* Build a scalable AI system architecture
* Implement modular AI services
* Enable automated candidate evaluation
* Maintain clean and testable code structure
---
## 🏗️ Project Structure
``
zecpath-ai/
│
├── data/                  # Sample datasets
├── parsers/               # Resume parsing logic
├── ats_engine/            # ATS scoring engine
├── screening_ai/          # Screening AI module
├── interview_ai/          # Interview AI module
├── scoring/               # Decision engine
├── utils/                 # Logging and helpers
├── tests/                 # Unit tests
│
├── main.py                # Main pipeline execution
├── config.py              # Configuration file
├── requirements.txt       # Dependencies
└── README.md              # Documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/yourusername/zecpath-ai.git
cd zecpath-ai
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```
python main.py
```

### Output:

```
Final Result:
Score: 10
Decision: Hold
```

---

## 🧠 Features Implemented

* Resume parsing (basic logic)
* ATS scoring engine
* Decision engine
* Modular architecture
* Logging system
* Unit testing (pytest)

---

## 🧪 Run Tests

```
pytest
```

---

## 📊 Logging

Logs are stored in:

```
ai_logs.log
```
