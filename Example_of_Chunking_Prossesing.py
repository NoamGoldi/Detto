### open the csv file "Deeto/References For Search.xlsx" and read the data to a pandas dataframe
%pip install openpyxl
import pandas as pd
# Install pandas
!{sys.executable} -m pip install pandas
import cv2
# Install numpy
!{sys.executable} -m pip install numpy

!{sys.executable} -m pip install openai
# Install openai
import openai
# Install openpyxl for reading Excel files
!{sys.executable} -m pip install openpyxl
# Set your OpenAI API key directly (not recommended for production, use environment variable instead)
openai.api_key = "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"  # Replace with your actual OpenAI API key

import os
# Optionally, you can use the environment variable if you want:
# openai.api_key = os.getenv('OPENAI_API_KEY')
# if not openai.api_key:
#     raise ValueError("Please set your OpenAI API key in the environment variable 'OPENAI_API_KEY' or replace")

# Read the Excel file
df = pd.read_excel(r"Deeto/References For Search.xlsx")
# Convert the dataframe to a dictionary
data_dict = df.to_dict(orient='records')
# Save the dictionary to a file
import json
with open('data_dict.json', 'w') as f:
    json.dump(data_dict, f, indent=4)
# Load the dictionary from the file
with open('data_dict.json', 'r') as f:
    loaded_data_dict = json.load(f)

# Each dictionary contains the keys 'type' (string type), 'topic' (string type), and 'content' (json string)
# In the 'content' field there is json string keys like 'paragraphs', 'content', 'Question 2', 'Question 0', etc.
# Conunt the number of occurences of each row groupped by value of 'type' and 'topic' fields and each key in the 'content' field
from collections import defaultdict
def count_occurrences(data_dict):
    counts = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    
    for record in data_dict:
        record_type = record['type']
        topic = record['topic']
        content = record['content']
        
        # Parse the content JSON string
        content_dict = json.loads(content)
        
        for key in content_dict.keys():
            counts[record_type][topic][key] += 1
            
    return counts
occurrences = count_occurrences(loaded_data_dict)
# Print the occurrences
for record_type, topics in occurrences.items():
    for topic, keys in topics.items():
        for key, count in keys.items():
            print(f"Type: {record_type}, Topic: {topic}, Key: {key}, Count: {count}")

# we will take all the rows with the 'type' field value 'Review' and their 'content' key json value of 'content' field
def extract_review_contents(data_dict):
    review_contents = []
    
    for record in data_dict:
        if record['type'] == 'Review':
            content = json.loads(record['content'])
            if 'content' in content:
                review_contents.append(content['content'])
    
    return review_contents
review_contents = extract_review_contents(loaded_data_dict)

# Filter out None values from review_contents
filtered_review_contents = [r for r in review_contents if isinstance(r, str) and r.strip()]

# make a summery reviews of all the 'Review' contents just in one single string, use ChatGPT for summarize the reviews
# Prosses the reviews by break the reviews into smaller chunks if they are too long, and summarize them
# keep the summary of each chunk and then summarize the summaries into one final summary, without exceeding the OpenAI API token limit
def summarize_reviews(reviews):
    summaries = []
    chunk_size = 2000  # Adjust this size based on token limits and average review length

    for i in range(0, len(reviews), chunk_size):
        chunk = reviews[i:i + chunk_size]
        prompt = "Please summarize the following reviews:\n\n" + "\n".join(chunk)

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        summaries.append(response.choices[0].message.content)

    final_summary_prompt = "Please summarize the following summaries:\n\n" + "\n".join(summaries)

    final_response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": final_summary_prompt}],
        max_tokens=500
    )

    return final_response.choices[0].message.content
# Summarize the reviews
final_summary = summarize_reviews(filtered_review_contents)
# Print the final summary
print("Final Summary of Reviews:")
print(final_summary)
