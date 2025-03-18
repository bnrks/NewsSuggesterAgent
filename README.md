
# News Suggester Agent
This project is an AI Agent that makes news recommendations according to the criteria set by the user and summarizes the news it recommends.




## Authors

- [@bnrks](https://www.github.com/bnrks)


This is a news aggregation and summarization project using **OpenAI** and **NewsAPI**. The project includes both a React-based frontend and a Python-based backend. The backend leverages **GPT-4o-mini** via the `smolagent` library to process and summarize news articles fetched from NewsAPI.

---

## 🚀 Features
- **React.js Frontend:** User-friendly interface for setting query parameters.  
- **Python Backend:** Handles API calls and response processing using `smolagent` and GPT-4o-mini.  
- **News Summarization:** Summarizes fetched news articles into a clean, readable format.  
- **Dynamic Filtering:** Customize search parameters for better targeting of news content.  

---






## Run Locally

Clone the project

```bash
  git clone https://github.com/bnrks/NewsSuggesterAgent.git
```
### To run frontend

Go to the project directory 

```bash
  cd frontend/newsagentreact 
```

Install dependencies

```bash
  npm install requirements.txt
```

Start the server

```bash
  npm run dev
```

### To run backend

Go to the project directory 

```bash
  cd backend
```

Install dependencies

```bash
  npm install requirements.txt
```

Start the server

```bash
  python main.py
```


## 🔍 How It Works

- The user inputs search parameters via the web interface.
- The frontend sends a POST request to the /get-news endpoint with the parameters.

- The backend's codeagent (from the smolagent library) fetches news articles from NewsAPI.

- The codeagent processes and summarizes the news using GPT-4o-mini.
- The summarized articles are sent back to the frontend and displayed in the UI.


## Screenshots



![App Screenshot](https://s5.ezgif.com/tmp/ezgif-534e39ac081869.gif)
