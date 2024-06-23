import ollama

client = ollama.Client(host='http://localhost:11434')
question = "hi"
response = client.chat(model='llama3', messages=[
    {
        'role': 'user', 
        'content': question
    }])
print(response['message']['content'])