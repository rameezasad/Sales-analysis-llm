import pandas as pd
import openai

def load_sales_data(file_path: str):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.json'):
        return pd.read_json(file_path)
    else:
        raise ValueError("Unsupported file format. Use CSV or JSON.")

def get_gpt_insights(sales_data: str, prompt: str):
    openai.api_key = 'org-b6FvqaKT1qG7iz3v2vACEqAb'
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt + sales_data,
        max_tokens=150
    )
    return response.choices[0].text.strip()
