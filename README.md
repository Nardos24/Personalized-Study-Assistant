# 📚 Personalized Study Assistant

### **An AI-powered web application for interactive learning**

## 🚀 **Project Overview**
The **Personalized Study Assistant** is a single-page web application that utilizes **Generative AI** to help users learn various topics in a structured and efficient manner. By leveraging OpenRouter’s API, the app generates AI-powered summaries based on user input and supplements the response with additional content from **Wikipedia** when necessary. The tool is designed to assist students, researchers, and curious learners in quickly understanding new concepts with minimal effort.

---

## 📌 **Features**
✅ AI-powered topic summarization using OpenRouter's API.  
✅ Adjustable **level of detail** (Short, Medium, In-depth).  
✅ **Bullet Points or Paragraph format** selection.  
✅ **Wikipedia Integration** for additional learning resources.  
✅ **Interactive UI** with a clean, responsive design built with Streamlit.  

---

## 🎯 **Idea Behind the App**
The purpose of this project is to **enhance learning efficiency** by allowing users to quickly grasp complex topics using AI-generated summaries. The integration of Wikipedia ensures that responses remain **factually accurate and comprehensive**. Instead of spending time sifting through search results, users receive **precise, context-aware summaries** in seconds, making the learning process faster and more effective.

This project is ideal for:
- **Students** looking for quick explanations before exams.
- **Researchers** who need an overview before deep-diving into papers.
- **Casual learners** curious about various topics.

---

## 🧠 **How Prompt Engineering Techniques Were Applied**
To enhance the **quality and relevance** of AI-generated summaries, multiple prompt engineering techniques were employed:

### **1️⃣ Contextual Prompting**
- We provide the AI with **specific task instructions** to ensure responses align with user expectations.
- Example:
  ```
  Summarize '{topic}' in '{detail_level}' detail. Format: '{output_format}'.
  ```
- This helps the AI understand the context and **generate structured, concise, and informative outputs**.

### **2️⃣ Few-Shot Prompting**
- AI is conditioned using **example responses** to ensure consistency in structure and tone.
- This minimizes **hallucinations** and keeps responses **aligned with user intent**.

### **3️⃣ Iterative Prompting**
- If the AI's response is **too short**, Wikipedia is used to **supplement the answer**.
- This ensures users always get **detailed and accurate information**.

### **4️⃣ Role-Based Prompting**
- The AI is prompted to **act as an intelligent study assistant**, ensuring responses are:
  - **Concise but informative**
  - **Factually accurate**
  - **Educational in nature**
- This enhances usability for students and researchers.

---

## 🛠 **AI Model & Parameter Adjustments**
To fine-tune AI behavior, several parameters were adjusted:

| **Parameter**  | **Value** | **Purpose** |
|---------------|----------|-------------|
| **Model** | `gpt-3.5-turbo` | Optimized for fast, cost-efficient responses. |
| **Temperature** | `0.5` | Controls creativity: Low values ensure factual accuracy, while high values encourage more creative responses. |
| **Max Tokens** | Dynamic | Prevents overly lengthy responses while ensuring completeness. |
| **Top-p** | Default | Adjusts diversity: Lower values create more deterministic outputs, while higher values generate diverse responses. |

✅ **Why Temperature = 0.5?**
- A **lower temperature** ensures **fact-based and structured summaries**, preventing unnecessary creativity.
- If users prefer **more creative outputs**, increasing the temperature **adds variety to the responses**.

---

## ⚙ **Tech Stack & Setup**
### **📦 Requirements**
- Python 3.8+
- Streamlit
- Requests
- Wikipedia API
- Python-dotenv

### **📂 Installation Steps**
1️⃣ **Clone the Repository**
```sh
git clone https://github.com/Nardos24/Personalized-Study-Assistant.git
cd personalized-study-assistant
```

2️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

3️⃣ **Set Up Environment Variables**
Create a `.env` file and add your **OpenRouter API Key**:
```sh
echo "OPENROUTER_API_KEY=your_actual_api_key_here" > .env
```

4️⃣ **Configure Wikipedia Access**
Wikipedia requires a **User-Agent** for API access. Open `utils/wikipedia_utils.py` and replace the **email placeholder** with your actual email:
```python
wiki_wiki = wikipediaapi.Wikipedia(
    user_agent="PersonalizedStudyAssistant/1.0 (contact: your-email@example.com)",
    language="en"
)
```
✅ **Replace** `your-email@example.com` with your real email to comply with Wikipedia’s access policy.

5️⃣ **Run the Application**
```sh
streamlit run app.py
```

