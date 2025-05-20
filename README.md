# 🇰🇿 AI Constitution Assistant

An AI-powered assistant that helps users explore and understand the **Constitution of the Republic of Kazakhstan**. Built using **Streamlit**, **Large Language Models (LLMs)**, and **Vector Search**, this project allows users to ask natural language questions and receive relevant answers based on constitutional documents.

---

## 📌 Features

- 🔎 Semantic search of constitutional articles using vector embeddings  
- 🤖 Natural language question answering with LLMs  
- 🧠 Embedding-based retrieval for relevant sections of the Constitution  
- 🌐 User-friendly interface built with Streamlit  
- 💾 Local or remote vector store support (e.g., FAISS or ChromaDB)

---

## 🛠️ Technologies Used

- Python 3.10+
- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [ChromaDB](https://www.trychroma.com/) or FAISS
- [OpenAI API](https://platform.openai.com/)
- Constitution of Kazakhstan dataset (in `/data/` folder)


## 📥 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/aselyagrammy/ai-constitution-assistant.git
cd ai-constitution-assistant
````

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Environment Variables

Create a `.env` file in the root of the project and include your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
```

Or export it directly in the terminal:

```bash
export OPENAI_API_KEY=your_api_key_here
```

### 5. Run the App

```bash
streamlit run app.py
```

Then open your browser and go to: [http://localhost:8501](http://localhost:8501)

---

## 📂 Project Structure

```
ai-constitution-assistant/
│
├── data/                   # Contains the Constitution text files
├── app.py                  # Main Streamlit application
├── vector_store/           # Embedding and vector DB logic
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not committed)
└── README.md               # Project documentation
```

---

## 📚 Example Use Cases

* "What are the rights of citizens in the Republic of Kazakhstan?"
* "Can the President dissolve the Parliament?"
* "How is the judicial power structured?"

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for improvements or new features.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🧠 Credits

Developed by [Aselya](https://github.com/aselyagrammy) as part of the **Blockchain Technologies 2** course project.
