# Text-to-SQL Chatbot 💬🧠

This project uses **LangChain** with **Google Gemini (Generative AI)** to convert natural language questions into SQL queries and run them against a SQLite database.

## 🚀 Features
- Gemini API (via `langchain_google_genai`)
- Converts user questions to SQL
- Executes query and returns results
- Sample `schema.sql` and `database.db` included

## 🛠️ Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Set your Google API key
cp .env.example .env
# Add your GOOGLE_API_KEY in the .env file

# Run the chatbot
python app.py
```

## 📁 Project Structure
```
├── app.py             # Main chatbot logic
├── schema.sql         # Sample SQL schema
├── database.db        # Sample database (SQLite)
├── requirements.txt   # Python dependencies
├── .env.example       # API key placeholder
├── .gitignore         # Files to ignore
└── README.md          # Project documentation
```

## 📦 Dependencies

- `langchain`
- `langchain-community`
- `langchain-google-genai`
- `google-generativeai`

## 🧠 Example Prompt

> "Show me all students with marks above 90"

---

🛡️ Made for educational/demo purposes. Customize the DB and prompts for your use case.