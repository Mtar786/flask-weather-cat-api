# Weather & Cat Facts App

This project is a fun and simple Flask web application that combines two popular APIs to deliver something a little different: when you enter the name of a city, the app shows you the current weather along with a random cat fact. The application fetches live weather data from [wttr.in](https://wttr.in) and random cat trivia from [Catfact.ninja](https://catfact.ninja).


## Features

- **Current weather:** Users can enter any city name to see the current temperature, weather description, humidity and wind speed.
- **Random cat fact:** Each time a user searches for a city, the app retrieves an interesting fact about cats.
- **Simple UI:** The interface is clean and minimalistic, making it easy to use.

## Project Structure

The repository uses a standard Flask project layout:

```
cool-webapp/
├── app.py               # Main Flask application
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation (this file)
├── .gitignore            # Ignored files and folders
├── templates/
│   ├── index.html        # Home page with search form
│   └── result.html       # Results page displaying weather and cat fact
└── static/
    └── style.css         # Optional CSS styles
```

## Getting Started

Follow these instructions to get a local copy up and running.

### Prerequisites

- Python 3.8 or higher
- An internet connection (the application fetches data from external APIs)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/cool-webapp.git
   cd cool-webapp
   ```

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Once the dependencies are installed, you can start the Flask development server:

```bash
python app.py
```

Open your web browser and navigate to `http://127.0.0.1:5000/` to use the application. Enter the name of a city and click **Get Weather & Cat Fact** to see the results.

### Deployment

This app is suitable for deployment to any platform that supports Python and Flask (e.g., Heroku, AWS Elastic Beanstalk, Azure Web Apps). Most deployment platforms require you to set environment variables and create a `Procfile`—see the platform’s documentation for details.

## How It Works

1. **User input:** On the home page (`index.html`), the user enters a city name and submits the form.
2. **API requests:** The Flask backend receives the input, then makes two HTTP requests:
   - It calls the `wttr.in` API to fetch current weather data in JSON format. This service does not require an API key for basic usage.
   - It calls the `catfact.ninja` API to fetch a random cat fact.
3. **Response rendering:** The app extracts relevant information from both API responses and renders it on the `result.html` page.

## Customisation

- **Change layout or styling:** Edit the files under the `templates` and `static` directories to customise the appearance.
- **Add more data:** You could extend the app to fetch additional details like forecasts, sunrise/sunset times, or facts from other APIs.
- **Error handling:** Currently the app includes basic error handling for failed API calls. You may want to enhance this for production usage.

## Contributing

Contributions are welcome! If you find a bug or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
