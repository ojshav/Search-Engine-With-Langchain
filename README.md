# Search Engine With Langchain

🔍 A powerful search engine application built using Streamlit and Langchain, integrating various tools like Wikipedia, Arxiv, and DuckDuckGo for comprehensive search capabilities.

## Features

- **Wikipedia Search**: Retrieve concise information from Wikipedia.
- **Arxiv Search**: Access academic papers and research articles.
- **DuckDuckGo Search**: Perform web searches using DuckDuckGo.
- **Interactive Chat Interface**: Engage with the search engine through a chat interface.

## Prerequisites

- Python 3.7 or higher
- [Streamlit](https://streamlit.io/)
- [Langchain](https://github.com/langchain/langchain)
- [Groq API Key](https://groq.com/)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the root directory and add your Groq API key:

   ```plaintext
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

1. **Run the application:**

   ```bash
   streamlit run Tools_agents/app.py
   ```

2. **Access the application:**

   Open your web browser and go to `http://localhost:8501`.

3. **Interact with the search engine:**

   - Enter your Groq API key in the sidebar.
   - Use the chat interface to ask questions and receive responses from the integrated tools.

## Troubleshooting

- Ensure all dependencies are installed correctly.
- Verify that your Groq API key is valid and correctly set in the `.env` file.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Langchain](https://github.com/langchain/langchain) for providing the tools and utilities.
- [Streamlit](https://streamlit.io/) for the interactive web application framework.

![image](https://github.com/user-attachments/assets/d3e8477b-5186-4de2-8023-c8bbbce509ec)

