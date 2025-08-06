import openai
from dotenv import find_dotenv, load_dotenv
import time
import logging
from datetime import datetime
import os
import requests
import json

load_dotenv()

news_api_key = os.environ.get("NEWS_API_KEY")

client = openai.OpenAI(api_key=os.environ.get("OPEN_API_KEY"))
model = "gpt-4"

def get_news(topic):
    url = (
        f"https://newsapi.org/v2/everything?q={topic}&apiKey={news_api_key}&pageSize=5"
    )

    try:
        response = requests.get(url)
        if response.status_code == 200:
            news = json.dumps(response.json(), indent=4)
            news_json = json.loads(news)

            data = news_json

            ##  Access all fields, loop through ==
            status = data["status"]
            total_results = data["totalResults"]
            articles = data["articles"]
            final_news = []

            ## Loop through articles
            for article in articles:
                source_name = article["source"]["name"]
                author = article["author"]
                title = article["title"]
                description = article["description"]
                url = article["url"]
                content = article["content"]
                title_description = f"""
                    Title: {title},
                    Author: {author},
                    Source: {source_name},
                    Description: {description}
                    URL: {url}
                """
                final_news.append(title_description)

            return final_news
        else:
            return []




    except requests.exceptions.RequestException as e:
        print("Error occurred durinng API Request", e)

def main():
    news = get_news("bitcoin")
    print(news[0])

class AssistantManager:
    thread_id = None
    assistant_id = None


    def __init__(self, model:str = model):
        self.client = client
        self.model = model
        self.assistant = None
        self.thread = None
        self.run = None
        self.summary = None


        if AssistantManager.assistant_id:
            self.assistant = self.client.beta.assistants.retrieve(
            assistant_id=AssistantManager.assistant_id
        )
        if AssistantManager.thread_id:
            self.thread = self.client.beta.threads.retrieve(
                thread_id=AssistantManager.thread_id
            )

        def create_assistant(self, name, instructions, tools):
            if not self.assistant:
                assistant_obj = self.client.beta.assistants.create(
                    name=name,
                    instructions=instructions,
                    tools=tools,
                    model=self.model
                )
                AssistantManager.assistant_id=assistant_obj.id
                self.assistant = assistant_obj
                print("AssisID:::: {self.assistant.id}")

        
        def create_thread(self):
            if not self.thread:
                thread_obj = self.client.beta.threads.create()
                AssistantManager.thread_id = thread_obj.id
                self.thread = thread_obj
                print("ThreadID::: {self.thread.id}")

        def add_message_to_thread(self, role, content):
            if self.thread:
                self.client.beta.threads.message.create(
                    thread_id=self.thread.id,
                    role=role,
                    content=content
                )

        def run_assistant(self, instructions):
            if self.thread and self.assistant:
                self.run = self.client.beta.threads.runs.create(
                    thread_id=self.thread.id,
                    assistant_id=self.assistant.id,
                    instructions=instructions
                )
        def process_message(self):
            if self.thread:
                messages = self.client.beta.threads.messages.list(
                    thread_id = self.thread.id
                )
                summary = []

                last_message =messages.data[0]
                role =last_message.role
                response = last_message.content[0].text.value
                summary.append(response)

                self.summary = "\n".join(summary)
                print(f"SUMMARY------> {role.capitalize(): ==> {response}}")
        
        def call_required_functions(self, required_actions):
            if not self.run:
                return
            tools_outputs = []

            for action in required_actions["tool_calls"]:
                func_name = action["function"]["name"]
                arguments = json.loads(action["function"]["arguments"])

        def wait_for_completed(self):
            if self.thread and self.run:
                while True:
                    time.sleep(5)
                    run_status = self.client.beta.thread.runs.retrieve(
                        thread_id=self.thread.id,
                        run_id=self.run.id
                    )
                    print(f"RUN STATUS:: {run_status.model_dump_json(indent=4)}")

                    if run_status.status =="completed":
                        self.process_message()
                        break
                    elif run_status.status == "requires_action":
                        print("FUNCTION CALLING NOW...")
                        self.call_required_functions(self, required_actions)

                


if __name__ == "__main__":
    main()
