
import openai

# Set your API key here
openai.api_key = "YOUR_API_KEY"

# Sample architectural prompt
prompt = "Generate a design concept for a futuristic green building in an urban environment using AI."

# Call OpenAI API
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a creative AI architect assistant."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.8,
    max_tokens=300
)

# Print the generated concept
print(response['choices'][0]['message']['content'])
