# 🤖 AI Applications Collection

A collection of powerful AI-powered applications built with Python, Streamlit, and OpenAI GPT models. This repository contains two main applications: a ChatGPT clone with interactive chat interface and a sentiment analysis tool.

## 📋 Table of Contents

- [Features](#features)
- [Applications](#applications)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Screenshots](#screenshots)
- [API Setup](#api-setup)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### ChatGPT Clone
- 🎯 **Custom System Prompts**: Define AI behavior and personality
- 💬 **Interactive Chat Interface**: Real-time conversation with AI
- 🎨 **Beautiful UI**: Modern, responsive Streamlit interface
- ⚙️ **Model Selection**: Choose from GPT-3.5, GPT-4, and other variants
- 📊 **Chat Statistics**: Track conversation metrics
- 📥 **Export Functionality**: Download chat history
- 🚀 **Quick Actions**: One-click conversation enhancers

### Sentiment Analysis App
- 🧠 **Zero-Shot Classification**: Analyze sentiment without training data
- 📈 **Multiple Models**: Support for various GPT models
- 📊 **Real-time Analysis**: Instant sentiment classification
- 📋 **History Tracking**: View previous analyses
- ⚙️ **Customizable Parameters**: Adjust temperature and token limits
- 📈 **Performance Metrics**: Track analysis statistics

## 🚀 Applications

### 1. ChatGPT Clone (`chat-gpt-clone/`)

A fully-featured ChatGPT clone with a beautiful web interface.

**Files:**
- `streamlit_app.py` - Main Streamlit web application
- `app.py` - Command-line version
- `requirements.txt` - Python dependencies

**Key Features:**
- Interactive chat with AI
- Custom system prompt configuration
- Model selection (GPT-3.5, GPT-4, etc.)
- Chat history and export
- Quick action buttons
- Responsive design

### 2. Sentiment Analysis App (`sentiment-analysis-app/`)

Advanced sentiment analysis tool using OpenAI's GPT models for zero-shot classification.

**Files:**
- `app.py` - Main Streamlit application
- `requirements.txt` - Python dependencies
- `README.md` - Detailed documentation

**Key Features:**
- Zero-shot sentiment classification
- Multiple emotion categories
- Model comparison tools
- Analysis history
- Export functionality

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- OpenAI API key
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/prompt_application.git
   cd prompt_application
   ```

2. **Install dependencies for ChatGPT Clone:**
   ```bash
   cd chat-gpt-clone
   pip install -r requirements.txt
   ```

3. **Install dependencies for Sentiment Analysis:**
   ```bash
   cd ../sentiment-analysis-app
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Running the ChatGPT Clone

1. **Navigate to the chat-gpt-clone directory:**
   ```bash
   cd chat-gpt-clone
   ```

2. **Run the Streamlit app:**
   ```bash
   streamlit run streamlit_app.py
   ```

3. **Access the application:**
   - Open your browser to `http://localhost:8501`
   - Configure your system prompt
   - Start chatting with the AI!

### Running the Sentiment Analysis App

1. **Navigate to the sentiment-analysis-app directory:**
   ```bash
   cd sentiment-analysis-app
   ```

2. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

3. **Access the application:**
   - Open your browser to `http://localhost:8501`
   - Enter text for sentiment analysis
   - View results and history

### Command Line Usage (ChatGPT Clone)

For a command-line interface:

```bash
cd chat-gpt-clone
python app.py
```

## ⚙️ Configuration

### API Key Setup

1. **Get your OpenAI API key:**
   - Visit [OpenAI Platform](https://platform.openai.com/)
   - Create an account and generate an API key

2. **Set the API key:**
   
   **Option 1: Environment Variable (Recommended)**
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```
   
   **Option 2: Direct in Code**
   - Edit the respective `app.py` or `streamlit_app.py` files
   - Replace the API key placeholder with your actual key

### Model Configuration

Both applications support various OpenAI models:

- **GPT-3.5 Turbo**: Fast and cost-effective
- **GPT-3.5 Turbo 16K**: Extended context
- **GPT-4**: Most capable model
- **GPT-4 Turbo**: Latest GPT-4 version
- **GPT-4o**: Multimodal capabilities
- **GPT-4o Mini**: Faster GPT-4 variant

## 📸 Screenshots

### ChatGPT Clone Interface
- Modern chat interface with message bubbles
- System prompt configuration panel
- Model selection sidebar
- Quick action buttons

### Sentiment Analysis Interface
- Clean input form
- Real-time analysis results
- Model comparison tools
- Analysis history

## 🔧 API Setup

### OpenAI API Key

1. **Sign up for OpenAI:**
   - Go to [OpenAI Platform](https://platform.openai.com/)
   - Create an account

2. **Generate API Key:**
   - Navigate to API Keys section
   - Create a new secret key
   - Copy the key for use in applications

3. **Set Usage Limits:**
   - Configure spending limits
   - Monitor usage in the dashboard

### Rate Limits

- **GPT-3.5**: 3,500 requests/minute
- **GPT-4**: 500 requests/minute
- **Token Limits**: Vary by model

## 🛠️ Development

### Project Structure

```
prompt_application/
├── chat-gpt-clone/
│   ├── streamlit_app.py      # Main web application
│   ├── app.py               # Command-line version
│   └── requirements.txt     # Dependencies
├── sentiment-analysis-app/
│   ├── app.py              # Main application
│   ├── requirements.txt    # Dependencies
│   └── README.md          # App-specific docs
└── README.md              # This file
```

### Adding New Features

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Test thoroughly**
5. **Submit a pull request**

## 📊 Performance Tips

### For ChatGPT Clone
- Use GPT-3.5-turbo for faster responses
- Adjust temperature for creativity vs consistency
- Set appropriate max tokens for response length

### For Sentiment Analysis
- Use lower temperature (0.0) for consistent results
- Limit max tokens for classification tasks
- Consider model costs for large-scale analysis

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error:**
   - Ensure your OpenAI API key is valid
   - Check if you have sufficient credits

2. **Import Errors:**
   - Install all required dependencies
   - Check Python version compatibility

3. **Streamlit Issues:**
   - Clear browser cache
   - Restart the Streamlit server

### Getting Help

- Check the [Issues](https://github.com/yourusername/prompt_application/issues) page
- Review OpenAI API documentation
- Check Streamlit documentation

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [OpenAI](https://openai.com/) for providing the GPT models
- [Streamlit](https://streamlit.io/) for the web framework
- The open-source community for inspiration and tools

## 📞 Contact

- **Project Link:** [https://github.com/yourusername/prompt_application](https://github.com/yourusername/prompt_application)
- **Issues:** [GitHub Issues](https://github.com/yourusername/prompt_application/issues)

---

⭐ **Star this repository if you found it helpful!**

## 🔄 Updates

### Version 1.0.0
- Initial release with ChatGPT clone
- Sentiment analysis application
- Beautiful Streamlit interfaces
- Custom system prompt functionality

---

**Made with ❤️ using Python, Streamlit, and OpenAI**
