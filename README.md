# 🧠 Text-to-SQL Chatbot 💬 ➡️ 🗃️

Turn natural language into SQL queries using LLMs (Google Gemini or OpenAI).  
Ideal for databases where users don't know SQL but need insights fast!

---

## 🚀 Features

- 🗣️ Ask database questions in plain English
- 🤖 Converts text → SQL using LLM
- 🧪 Runs the query and shows actual results
- 🛡️ Works with Google Gemini or OpenAI API
- 🛠️ Easy to configure using `.env` file

---

## 📦 Requirements

- Python 3.9+
- A `.env` file with your API key:
  ```
  GOOGLE_API_KEY=your_google_api_key
  ```
- Google Gemini access (Free, from: https://makersuite.google.com/app/apikey)

---

## 🛠️ Setup Instructions

1. **Clone this repository**
   ```bash
   git clone https://github.com/Thinkvas/text-sql-chatbot.git
   cd text-sql-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your API key**
   - Create a `.env` file using `.env.example` as template
   - Paste your Gemini or OpenAI key

4. **Run the chatbot**
   ```bash
   python app.py
   ```

---

## 🧪 Example

**Input:**  
```
Show me the total number of users who signed up in July.
```

**Generated SQL:**  
```sql
SELECT COUNT(*) FROM users WHERE signup_date BETWEEN '2024-07-01' AND '2024-07-31';
```

**Result:**  
```
Total Users: 253
```

---

## 🧠 Built With

- [LangChain](https://www.langchain.com/)
- [Google Generative AI](https://makersuite.google.com/app)
- [SQLite](https://www.sqlite.org/)
- [Python](https://www.python.org/)

---

## 🤝 Contributing

Pull requests are welcome! If you’d like to contribute, feel free to fork and improve.

---

## 📄 License

MIT License — free for personal and commercial use.

---

## ✨ Author

Made by **[@Thinkvas](https://github.com/Thinkvas)** 🚀