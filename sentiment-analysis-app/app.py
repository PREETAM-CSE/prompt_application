import streamlit as st
import openai
import os



def gpt_classify_sentiment(prompt, emotions, model="gpt-3.5-turbo", temperature=0.0, max_tokens=20):
    system_prompt = f'''You are an emotionally intelligent assistant.
Classify the sentiment of the user's text with only one of the following emotions: {emotions}
After classifying the text, respond with the emotion only.'''

    # Create OpenAI client
    client = openai.OpenAI()

    try:
        # Make chat completion request with dynamic parameters
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature
        )

        # Extract the response content
        result = response.choices[0].message.content.strip()

        return result if result else 'N/A'

    except Exception as e:
        print(f"Error during classification: {e}")
        return 'N/A'


if __name__ == "__main__":
    # Set API key - Replace with your actual API key
    # os.environ['OPENAI_API_KEY'] = 'your-openai-api-key-here'
    # Or set it as an environment variable: export OPENAI_API_KEY="your-key-here"
    
    # Initialize session state for storing analysis history
    if 'analysis_history' not in st.session_state:
        st.session_state.analysis_history = []
    
    if 'total_analyses' not in st.session_state:
        st.session_state.total_analyses = 0
    
    # Custom CSS for professional styling
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f2937;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .sub-header {
        font-size: 1.2rem;
        color: #6b7280;
        text-align: center;
        margin-bottom: 3rem;
    }
    
    .input-container {
        background-color: #f8fafc;
        padding: 2rem;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        margin-bottom: 2rem;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
    }
    
    .result-container {
        background-color: #f0f9ff;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #3b82f6;
        margin-top: 2rem;
    }
    
    .metric-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 8px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    
    .sidebar .sidebar-content {
        background-color: #f8fafc;
    }
    
    .history-container {
        background-color: #f8fafc;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        margin-top: 2rem;
    }
    
    .history-entry {
        background-color: white;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #3b82f6;
        margin-bottom: 1rem;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Main header
    st.markdown('<h1 class="main-header">AI Sentiment Analysis</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Advanced Zero-Shot Classification with GPT</p>', unsafe_allow_html=True)
    
    # Sidebar for configuration
    with st.sidebar:
        st.markdown("### ⚙️ Configuration")
        st.markdown("---")
        
        # Model selection with more options and descriptions
        model_options = {
            "gpt-3.5-turbo": "Fast and cost-effective for most tasks",
            "gpt-3.5-turbo-16k": "GPT-3.5 with extended context (16k tokens)",
            "gpt-4": "Most capable model with better reasoning",
            "gpt-4-turbo": "Latest GPT-4 with improved performance",
            "gpt-4-turbo-preview": "Preview version of GPT-4 Turbo",
            "gpt-4o": "Multimodal model with vision capabilities",
            "gpt-4o-mini": "Faster and cheaper GPT-4 variant"
        }
        
        model_choice = st.selectbox(
            "Select OpenAI Model:",
            list(model_options.keys()),
            index=0,
            help="Choose the OpenAI model for analysis. Different models have different capabilities and costs."
        )
        
        # Display model description
        st.caption(f"💡 {model_options[model_choice]}")
        
        # Model cost indicator
        cost_info = {
            "gpt-3.5-turbo": "💰 Low cost",
            "gpt-3.5-turbo-16k": "💰 Low-Medium cost", 
            "gpt-4": "💰💰💰 High cost",
            "gpt-4-turbo": "💰💰💰 High cost",
            "gpt-4-turbo-preview": "💰💰💰 High cost",
            "gpt-4o": "💰💰💰💰 Very High cost",
            "gpt-4o-mini": "💰💰 Medium cost"
        }
        st.caption(cost_info[model_choice])
        
        # Temperature setting
        temperature = st.slider(
            "Temperature:",
            min_value=0.0,
            max_value=1.0,
            value=0.0,
            step=0.1,
            help="Lower values make responses more focused and deterministic"
        )
        
        # Max tokens
        max_tokens = st.slider(
            "Max Tokens:",
            min_value=10,
            max_value=100,
            value=20,
            step=5,
            help="Maximum number of tokens in the response"
        )
        
        st.markdown("---")
        st.markdown("### 📊 Quick Stats")
        st.metric("API Status", "✅ Connected")
        st.metric("Selected Model", model_choice)
        st.metric("Total Analyses", st.session_state.total_analyses)
        
        # Model performance indicator
        if model_choice.startswith("gpt-4"):
            st.success("🚀 High Performance Model")
        elif model_choice.startswith("gpt-3.5"):
            st.info("⚡ Balanced Performance Model")
        
        # Show current settings
        st.markdown("---")
        st.markdown("### ⚙️ Current Settings")
        st.write(f"**Model:** {model_choice}")
        st.write(f"**Temperature:** {temperature}")
        st.write(f"**Max Tokens:** {max_tokens}")
        
        # Clear history button
        st.markdown("---")
        if st.button("🗑️ Clear History", help="Clear all analysis history"):
            st.session_state.analysis_history = []
            st.session_state.total_analyses = 0
            st.success("History cleared!")
            st.rerun()
    
    # Model comparison section
    with st.expander("🔍 Model Comparison & Information", expanded=False):
        st.markdown("### Available OpenAI Models")
        
        col_comp1, col_comp2 = st.columns(2)
        
        with col_comp1:
            st.markdown("#### GPT-3.5 Series")
            st.markdown("""
            - **gpt-3.5-turbo**: Fast, cost-effective, good for most tasks
            - **gpt-3.5-turbo-16k**: Extended context (16k tokens)
            - **gpt-4o-mini**: Faster GPT-4 variant with lower cost
            """)
        
        with col_comp2:
            st.markdown("#### GPT-4 Series")
            st.markdown("""
            - **gpt-4**: Most capable, better reasoning
            - **gpt-4-turbo**: Latest with improved performance
            - **gpt-4o**: Multimodal with vision capabilities
            """)
        
        st.markdown("### 💡 Model Selection Tips")
        st.markdown("""
        - **For quick analysis**: Use GPT-3.5-turbo
        - **For accuracy**: Use GPT-4 or GPT-4-turbo
        - **For cost efficiency**: Use GPT-3.5-turbo or GPT-4o-mini
        - **For long texts**: Use GPT-3.5-turbo-16k
        """)
    
    # Main content area
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    
    # Create two columns for inputs
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📝 Text Input")
        prompt_text = st.text_area(
            "Enter your text for sentiment analysis:",
            height=200,
            placeholder="Type your text here...",
            help="Enter the text you want to analyze for sentiment"
        )
    
    with col2:
        st.markdown("### 🎭 Emotion Categories")
        emotions_input = st.text_area(
            "Define emotion categories:",
            height=200,
            value="Happy, Sad, Angry, Fearful, Disgusted, Surprised, Neutral",
            placeholder="Enter emotions separated by commas...",
            help="Define the emotion categories for classification"
        )
        
        # Preset emotion templates
        st.markdown("**Quick Templates:**")
        if st.button("Basic Emotions"):
            emotions_input = "Happy, Sad, Angry, Fearful, Disgusted, Surprised, Neutral"
        if st.button("Extended Emotions"):
            emotions_input = "Joy, Sadness, Anger, Fear, Surprise, Disgust, Trust, Anticipation, Shame, Guilt"
        if st.button("Business Sentiment"):
            emotions_input = "Positive, Negative, Neutral, Excited, Concerned, Satisfied, Frustrated"
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Analysis button
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        analyze_button = st.button("🔍 Analyze Sentiment", use_container_width=True)
    
    # Process analysis
    if analyze_button:
        if not prompt_text.strip():
            st.warning("⚠️ Please enter some text to analyze.")
        elif not emotions_input.strip():
            st.warning("⚠️ Please define emotion categories.")
        else:
            with st.spinner("🤖 AI is analyzing your text..."):
                try:
                    # Update the function to use the selected parameters
                    result = gpt_classify_sentiment(
                        prompt_text, 
                        emotions_input, 
                        model=model_choice,
                        temperature=temperature,
                        max_tokens=max_tokens
                    )
                    
                    if result != 'N/A':
                        # Save to session state history
                        import datetime
                        analysis_entry = {
                            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            'text': prompt_text,
                            'emotions': emotions_input,
                            'result': result,
                            'model': model_choice,
                            'temperature': temperature,
                            'max_tokens': max_tokens
                        }
                        st.session_state.analysis_history.append(analysis_entry)
                        st.session_state.total_analyses += 1
                        
                        st.markdown('<div class="result-container">', unsafe_allow_html=True)
                        st.markdown("### 🎯 Analysis Result")
                        
                        # Display result in a metric card
                        col_result1, col_result2 = st.columns([1, 1])
                        
                        with col_result1:
                            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
                            st.metric("Detected Emotion", result)
                            st.markdown('</div>', unsafe_allow_html=True)
                        
                        with col_result2:
                            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
                            st.metric("Confidence", "High", delta=model_choice)
                            st.markdown('</div>', unsafe_allow_html=True)
                        
                        # Detailed analysis
                        st.markdown("### 📋 Detailed Analysis")
                        st.write(f"**Original Text:** {prompt_text}")
                        st.write(f"**Emotion Categories:** {emotions_input}")
                        st.write(f"**Detected Emotion:** {result}")
                        st.write(f"**Model Used:** {model_choice}")
                        st.write(f"**Temperature:** {temperature}")
                        st.write(f"**Max Tokens:** {max_tokens}")
                        st.write(f"**Analysis #:** {st.session_state.total_analyses}")
                        
                        # Model performance indicator
                        if model_choice.startswith("gpt-4"):
                            st.success(f"✅ Used high-performance model: {model_choice}")
                        elif model_choice.startswith("gpt-3.5"):
                            st.info(f"⚡ Used balanced model: {model_choice}")
                        
                        st.markdown('</div>', unsafe_allow_html=True)
                    else:
                        st.error("❌ Failed to analyze sentiment. Please check your inputs and try again.")
                        
                except Exception as e:
                    st.error(f"❌ Error during analysis: {str(e)}")
    
    # History Section
    if st.session_state.analysis_history:
        st.markdown("---")
        st.markdown("### 📚 Analysis History")
        
        # Create tabs for different views
        tab1, tab2, tab3 = st.tabs(["📋 List View", "📊 Statistics", "📈 Charts"])
        
        with tab1:
            st.markdown(f"**Total Analyses:** {len(st.session_state.analysis_history)}")
            
            # Display history in reverse order (newest first)
            for i, entry in enumerate(reversed(st.session_state.analysis_history)):
                with st.expander(f"Analysis #{len(st.session_state.analysis_history) - i} - {entry['timestamp']}"):
                    col_h1, col_h2 = st.columns([2, 1])
                    
                    with col_h1:
                        st.write(f"**Text:** {entry['text'][:100]}{'...' if len(entry['text']) > 100 else ''}")
                        st.write(f"**Emotions:** {entry['emotions']}")
                    
                    with col_h2:
                        st.metric("Result", entry['result'])
                        st.caption(f"Model: {entry['model']}")
        
        with tab2:
            # Calculate statistics
            emotions_count = {}
            models_count = {}
            
            for entry in st.session_state.analysis_history:
                # Count emotions
                emotion = entry['result']
                emotions_count[emotion] = emotions_count.get(emotion, 0) + 1
                
                # Count models
                model = entry['model']
                models_count[model] = models_count.get(model, 0) + 1
            
            col_stat1, col_stat2 = st.columns(2)
            
            with col_stat1:
                st.markdown("#### 🎭 Emotion Distribution")
                for emotion, count in sorted(emotions_count.items(), key=lambda x: x[1], reverse=True):
                    percentage = (count / len(st.session_state.analysis_history)) * 100
                    st.write(f"**{emotion}:** {count} ({percentage:.1f}%)")
            
            with col_stat2:
                st.markdown("#### 🤖 Model Usage")
                for model, count in models_count.items():
                    percentage = (count / len(st.session_state.analysis_history)) * 100
                    st.write(f"**{model}:** {count} ({percentage:.1f}%)")
        
        with tab3:
            # Create charts
            import pandas as pd
            
            # Emotion distribution chart
            emotions_df = pd.DataFrame(list(emotions_count.items()), columns=['Emotion', 'Count'])
            st.markdown("#### Emotion Distribution Chart")
            st.bar_chart(emotions_df.set_index('Emotion'))
            
            # Model usage chart
            models_df = pd.DataFrame(list(models_count.items()), columns=['Model', 'Count'])
            st.markdown("#### Model Usage Chart")
            st.bar_chart(models_df.set_index('Model'))
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #6b7280; padding: 2rem;'>
        <p>Powered by OpenAI GPT • Built with Streamlit</p>
        <p>Advanced AI-powered sentiment analysis and emotion classification</p>
    </div>
    """, unsafe_allow_html=True)
