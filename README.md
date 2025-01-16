
# Brochurify

Welcome to Brochurify! This project leverages cutting-edge Large Language Models (LLMs) to deliver efficient webpage summarization and brochure generation.

## Table of Contents

1. [About the Project](#about-the-project)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Contributing](#contributing)
7. [License](#license)

---

## About the Project

An innovative project that simplifies website data extraction and summarization.

Key Technologies:
- FastAPI for backend APIs
- WebSockets for real-time communication
- LLMs for summarization and brochure generation

---

## Features

- **Webpage Summarization:** Provide a URL and get a concise summary.
- **Brochure Creation:** Generate a visually appealing, structured brochure from a website.
- **Real-time Processing:** Instant feedback using WebSockets.

---

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/itsnotvahid/Brochurify.git
   cd Brochurify
   ```

2. **Create a Virtual Environment:**

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   ```

3. **Install Dependencies:**

   Ensure you have `pip` installed. Then, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` File:**

   The application requires certain environment variables. Create a `.env` file in the root directory with the following content:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   # Add any other environment variables as needed
   ```

   Replace `your_openai_api_key_here` with your actual OpenAI API key. Ensure this file is included in your `.gitignore` to prevent it from being tracked by version control.

---

## Usage

To run the application:

1. **Start the FastAPI Server:**

   ```bash
   uvicorn main:app --reload
   ```

2. **Access the Application:**

   Open your browser and navigate to `http://localhost:8000` to interact with the application.

---

## Project Structure

- `main.py`: The entry point of the application.
- `api/`: Contains the API endpoints.
- `services/`: Includes the core logic for summarization and brochure generation.
- `static/`: Holds static files like CSS and JavaScript.
- `templates/`: Contains HTML templates for rendering web pages.
- `exceptions.py`: Custom exception handling.

---

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

---

## License

This project is licensed under the MIT License.