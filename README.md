# LangChain Output Parser 🦜🔗

A practical implementation of LangChain's Output Parsers using different approaches including Pydantic, JSON, Structured, and String output parsers.

---

## 📁 Project Structure

Langchain_Output_parser/
├── json_outputparser.py
├── pydantic_outputparser.py
├── stroutput_parser.py
├── stroutputparser_chain.py
└── structured_outputparser.py

---

## 🧠 Files Overview

| File | Description |
|---|---|
| `json_outputparser.py` | Parse LLM output into JSON format |
| `pydantic_outputparser.py` | Parse output using Pydantic validation |
| `stroutput_parser.py` | Basic String output parser |
| `stroutputparser_chain.py` | String output parser with LangChain chain |
| `structured_outputparser.py` | Parse output into structured format |

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/waseemmalik82/Langchain_Output_parser.git
cd Langchain_Output_parser
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup API Keys
Create a `.env` file in root folder:

OPENAI_API_KEY=your_openai_key

---

## 🚀 Usage

```bash
# JSON Output Parser
python json_outputparser.py

# Pydantic Output Parser
python pydantic_outputparser.py

# String Output Parser
python stroutput_parser.py

# String Output Parser with Chain
python stroutputparser_chain.py

# Structured Output Parser
python structured_outputparser.py
```

---

## 🔑 Required API Keys

| Provider | Get API Key |
|---|---|
| OpenAI | [platform.openai.com](https://platform.openai.com) |

---

## 🛡️ Important

- Never share your `.env` file
- `.env` is added to `.gitignore` for security
- Keep your API keys private at all times

---

## 👨‍💻 Author

**Waseem Malik**
GitHub: [@waseemmalik82](https://github.com/waseemmalik82)


