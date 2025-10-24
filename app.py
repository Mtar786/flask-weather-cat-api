"""Main entry point for the Weather & Cat Facts application.

This module sets up a small Flask web application that fetches
current weather information for a given city from the wttr.in API
and a random cat fact from the catfact.ninja API. The results
are displayed on a simple web page.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, Optional

import requests
from flask import Flask, render_template, request

# Configure basic logging. In production you might want to configure
# logging handlers differently or integrate with a structured logger.
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


def get_weather(city: str) -> Optional[Dict[str, Any]]:
    """Retrieve current weather data for a given city.

    This function calls the wttr.in API, which returns JSON data when
    the `format=j1` parameter is used. If the request fails or the
    response cannot be parsed, `None` is returned.

    Args:
        city: The name of the city to query.

    Returns:
        A dictionary with weather information, or None if there was
        an error.
    """
    url = f"https://wttr.in/{city}?format=j1"
    try:
        logging.info("Fetching weather for %s", city)
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        current = data.get("current_condition", [{}])[0]
        weather = {
            "temperature_C": current.get("temp_C"),
            "temperature_F": current.get("temp_F"),
            "description": current.get("weatherDesc", [{}])[0].get("value"),
            "humidity": current.get("humidity"),
            "wind_kmph": current.get("windspeedKmph"),
        }
        return weather
    except Exception as exc:  # broad catch is acceptable here for robustness
        logging.exception("Failed to fetch weather: %s", exc)
        return None


def get_cat_fact() -> Optional[str]:
    """Retrieve a random cat fact from the catfact.ninja API.

    Returns:
        A string containing a cat fact, or None if the request failed.
    """
    url = "https://catfact.ninja/fact"
    try:
        logging.info("Fetching a random cat fact")
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data.get("fact")
    except Exception as exc:
        logging.exception("Failed to fetch cat fact: %s", exc)
        return None


@app.route("/", methods=["GET"])
def index() -> str:
    """Render the home page with the search form."""
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result() -> str:
    """Handle form submission and display results.

    Reads the city name from the submitted form, retrieves weather and
    cat fact data, and renders the result page. Basic error handling
    ensures that issues with the external APIs do not crash the app.
    """
    city = (request.form.get("city") or "").strip()
    weather = get_weather(city) if city else None
    cat_fact = get_cat_fact()
    error = None
    if not city:
        error = "Please enter a city name."
    elif weather is None:
        error = "Failed to fetch weather data. Please check the city name or try again later."
    # Note: even if the cat fact fails, we'll still display the page; it can be None
    return render_template(
        "result.html",
        city=city.title() if city else "",
        weather=weather,
        cat_fact=cat_fact,
        error=error,
    )


if __name__ == "__main__":
    # Enable debug mode for development. In production, this should be
    # disabled and the app should be served by a WSGI server like gunicorn.
    app.run(debug=True)