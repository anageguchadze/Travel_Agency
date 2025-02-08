# Travel_Agency

This project is a **Travel Agency API** built with Django and Django Rest Framework (DRF). It allows users to browse through various travel packages and get recommendations through a simple chatbot interface. The chatbot helps users by answering queries and suggesting travel packages based on keywords.

## Features

- **Travel Package API**: Allows users to view, create, update, and delete travel packages.
- **Chatbot**: A simple chatbot to help users select vacation packages. The chatbot responds to messages based on keywords like "cheapest", "best", etc.
- **Destinations and Packages**: Users can explore various destinations and package details like price, duration, and availability.

## Tech Stack

- **Django**: Web framework for building the API.
- **Django Rest Framework (DRF)**: For creating RESTful APIs.
- **SQLite** (default database) for data storage.
- **nltk** (optional, for future enhancements) to extend chatbot capabilities.

## Installation

### 1. Clone the repository:
git clone https://github.com/anageguchadze/Travel_Agency.git
cd Travel_Agency

2. Set up the virtual environment:
python -m venv venv
source venv/bin/activate   # For Linux/MacOS
venv\Scripts\activate      # For Windows

3. Install dependencies:
pip install -r requirements.txt

4. Apply database migrations:
python manage.py migrate

5. Run the development server:
python manage.py runserver
Visit http://127.0.0.1:8000 in your browser to access the API.

API Endpoints
GET /api/travel-packages/: List all available travel packages.
POST /api/travel-packages/: Create a new travel package (with destination information).
POST /chatbot/: Send a message to the chatbot to get travel package recommendations.
Usage
To interact with the chatbot, send a POST request to /chatbot/ with a JSON message:

json
{
  "message": "Tell me the best vacation packages."
}
Response:

json
{
  "response": "Our best packages include trips to Bali, Paris, and Japan. Which one interests you?"
}
Future Enhancements
Implement a more advanced AI-based chatbot using platforms like Dialogflow or OpenAI for better conversation handling.
Add user authentication and bookings for a complete travel agency experience.
Contributing
Feel free to fork this repository and submit pull requests. All contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.

markdown
---

### Explanation:

- **Description**: Briefly explains the purpose of the project and what it does.
- **Tech Stack**: Lists the technologies used in the project.
- **Installation**: Step-by-step guide to set up the project locally.
- **API Endpoints**: Describes the key API endpoints that users can access.
- **Usage**: Gives an example of how to interact with the chatbot API.
- **Future Enhancements**: Mentions potential improvements for the future.
- **Contributing**: Encourages others to contribute to the project.
- **License**: Provides a standard MIT license or you can customize it based on your preference.

### Next Steps:
1. Customize the repository URL and any other project-specific details.
2. You can add a `requirements.txt` file to list the dependencies for easy installation (e.g., Django, DRF, nltk).

Let me know if you'd like any more details added to the `README.md` or need further assistance with anything!






