# Webscraper
WebScrap is a lightweight Python script designed for testing and interacting with API endpoints.
It prompts the user for a target URL, sends an HTTP GET request using the requests library, and displays the response.
If the endpoint returns JSON data, the script automatically formats and prints it.
Otherwise, it shows a plain text preview of the response.

Features:

Targets user-provided API endpoints

Automatically detects and displays JSON responses

Falls back to plain text output if JSON is unavailable

Simple, clean, and beginner-friendly structure

Requirements:

Python 3

requests


Usage:

python3 webscrap.py

Then provide an API URL such as:

ENTER YOUR SITE: https://api.example.com/users
