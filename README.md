# AI-Powered News Assistant (WIP)

This project is an AI assistant that fetches news articles based on a topic (via NewsAPI) and can eventually summarize or analyze them using OpenAI's GPT-4 through the (deprecated) **Assistants API**.

The assistant is managed programmatically using an `AssistantManager` class and is being prepared for integration into a GUI using **Streamlit**.

>  **Note**: The OpenAI Assistants API used in this project is **deprecated**. This project is a learning step as it transitions toward the new [OpenAI Responses API](https://platform.openai.com/docs/guides/responses).

---

##  Features (So Far)

- Fetches top 5 news articles related to a given topic using **NewsAPI**
- Formats and prepares the news content for use with an AI assistant
- Sets up:
  - Assistant creation
  - Thread management
  - Message addition
  - Run execution and polling
- Contains a skeleton structure for future:
  - Function calling
  - Assistant responses and summarization
  - Streamlit integration

---

##  Planned Features

- [ ] Streamlit GUI to select topic, view articles, and get summaries
- [ ] Full support for required function calls
- [ ] Integration with OpenAI’s **Responses API**
- [ ] More robust error handling and retries
- [ ] News source filters, language options, and date ranges

---

##  Project Structure

```
news_assistant/
├── assistant.py          # Assistant logic and manager class
├── .env                  # Contains API keys (not tracked by Git)
├── requirements.txt
```

---

##  Requirements

- Python 3.8+
- OpenAI API key (for Assistants API)
- NewsAPI key (https://newsapi.org/)
- Required Python packages:
  - `openai`
  - `requests`
  - `python-dotenv`

---

##  Environment Variables (`.env`)

Create a `.env` file in the root directory with the following:

```
OPEN_API_KEY=your_openai_api_key
NEWS_API_KEY=your_newsapi_key
```

---

##  Running the Script

```bash
python assistant.py
```

By default, the script runs `main()` which:
- Fetches the top 5 recent articles on **bitcoin**
- Prints the first formatted news result

You can later change this topic inside `main()` or make it user-defined via the Streamlit UI.

---

##  Example Output

```
[
    "Title: Bitcoin jumps above $30,000... Author: John Doe... Source: CNN... Description: The crypto market is rallying... URL: https://...",
    ...
]
```

---

##  Notes

- The `AssistantManager` class handles all communication with the OpenAI Assistants API.
- Some functions like `call_required_functions()` and Streamlit UI are yet to be fully implemented.
- Outputs are currently printed to the terminal for inspection.

---

##  Development Status

This project is **work-in-progress** and is being built modularly. Expect placeholder methods, incomplete functionality, and hardcoded topic defaults for now.

---

##  License

This project is for educational and learning purposes. You may reuse or extend it freely.

---

**Created by [Sidney Baraka](https://github.com/mathncode-sid)**
