import ollama
from cards import draw_cards

client = ollama.Client(host='http://localhost:11434')

def get_tarot_reading(question):
    try:
        selected_cards = draw_cards()
        card_names = ', '.join(selected_cards['name'])
        card_meanings = '\n'.join([f"{row['name']}: {row['fortune_telling'][0]}" for _, row in selected_cards.iterrows()])
        
        prompt = f"Question: {question}\nCards: {card_names}\nInterpret these cards: {card_meanings}."
        response = client.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
        reading = response['message']['content']

        # Generate a summary in 5 words or fewer
        summary_prompt = f"Summarize this tarot reading in 5 words or fewer: {reading}"
        summary_response = client.chat(model='llama3', messages=[{'role': 'user', 'content': summary_prompt}])
        summary = summary_response['message']['content']

        return reading, summary, selected_cards
    except Exception as e:
        print(f"Error: {e}")
        return "There was an error retrieving your tarot reading. Please try again later.", "Error", pd.DataFrame()
