# AI Sentiment Analysis App

A powerful Streamlit-based web application for sentiment analysis using OpenAI's GPT models. This app provides advanced zero-shot classification capabilities with customizable emotion categories and multiple model options.

## Features

- 🤖 **Multiple OpenAI Models**: Support for GPT-3.5, GPT-4, and GPT-4o variants
- 🎭 **Customizable Emotions**: Define your own emotion categories for classification
- 📊 **Real-time Analysis**: Instant sentiment analysis with detailed results
- 📈 **Analytics Dashboard**: View analysis history, statistics, and charts
- ⚙️ **Configurable Parameters**: Adjust temperature, max tokens, and model selection
- 💰 **Cost Awareness**: Built-in cost indicators for different models

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd sentiment-analysis-app
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key:
   - Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
   - Replace the API key in `app.py` (line 39) with your own key
   - **Important**: Never commit your API key to version control!

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to the provided local URL (usually `http://localhost:8501`)

3. Enter your text and define emotion categories, then click "Analyze Sentiment"

## Configuration

### Model Selection
- **GPT-3.5-turbo**: Fast and cost-effective for most tasks
- **GPT-4**: Most capable model with better reasoning
- **GPT-4o**: Multimodal model with vision capabilities
- **GPT-4o-mini**: Faster and cheaper GPT-4 variant

### Parameters
- **Temperature**: Controls randomness (0.0 = deterministic, 1.0 = creative)
- **Max Tokens**: Maximum length of the response
- **Emotion Categories**: Customize the classification labels

## Project Structure

```
sentiment-analysis-app/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── .gitignore         # Git ignore file
```

## API Key Security

⚠️ **Important Security Note**: 
- Never commit your OpenAI API key to version control
- Consider using environment variables for production deployments
- Use `.env` files for local development (add to `.gitignore`)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues and questions, please create an issue in the GitHub repository.
