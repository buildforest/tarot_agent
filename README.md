# Tarot Reading App

You can ask any questions to the mage and type in the question. The mage will draw 3 cards for you and read the meaning.

## Features
Ask a question and get a tarot reading.
Displays three drawn tarot cards with images and brief descriptions.
Generates a short summary of the tarot reading.
Beautiful landing page and result page with custom styling.

## Data
The tarot card data used in this app is sourced from Kaggle: Tarot JSON Dataset(https://www.kaggle.com/datasets/lsind18/tarot-json).

## File Structure
app.py: Main Flask application file.
llama3_agent.py: Contains the logic to interact with the Llama3 model and generate tarot readings.
cards.py: Handles the tarot card data and drawing logic.
templates/: Contains HTML templates for the landing page and result page.
static/: Contains static files such as CSS and images.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
Tarot card data is sourced from Kaggle.
Background images and styling inspired by various web resources.