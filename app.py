from flask import Flask, request, render_template
from llama3_agent import get_tarot_reading

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_reading', methods=['POST'])
def get_reading():
    try:
        question = request.form['question']
        if not question:
            return render_template('result.html', reading="Please enter a valid question.", summary="Error", cards=[])

        reading, summary, selected_cards = get_tarot_reading(question)
        cards = selected_cards.to_dict('records')

        # Log the selected cards
        for card in cards:
            app.logger.debug(f"Card drawn: {card['name']}, Meaning: {card['fortune_telling'][0]}, Image: {card['img_file']}")

        return render_template('result.html', reading=reading, summary=summary, cards=cards)
    except Exception as e:
        app.logger.error(f"Error: {e}")
        return render_template('result.html', reading="There was an error processing your request.", summary="Error", cards=[])

if __name__ == '__main__':
    app.run(debug=True, port=50001)
