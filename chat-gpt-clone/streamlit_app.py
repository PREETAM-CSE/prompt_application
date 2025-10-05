import streamlit as st
from openai import OpenAI
import os
import time
from datetime import datetime

# Initialize OpenAI client
def get_client():
    return OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

# Function to get AI response
def get_ai_response(messages, model="gpt-3.5-turbo", temperature=0.7, max_tokens=1000):
    client = get_client()
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Custom CSS for beautiful styling
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

.chat-container {
    background-color: #f8fafc;
    padding: 2rem;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
    margin-bottom: 2rem;
    box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
    min-height: 400px;
    max-height: 600px;
    overflow-y: auto;
}

.message-user {
    background-color: #3b82f6;
    color: white;
    padding: 1rem;
    border-radius: 12px 12px 4px 12px;
    margin: 1rem 0;
    margin-left: 20%;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.message-assistant {
    background-color: #f1f5f9;
    color: #1e293b;
    padding: 1rem;
    border-radius: 12px 12px 12px 4px;
    margin: 1rem 0;
    margin-right: 20%;
    border-left: 4px solid #3b82f6;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.message-system {
    background-color: #fef3c7;
    color: #92400e;
    padding: 0.75rem;
    border-radius: 8px;
    margin: 0.5rem 0;
    text-align: center;
    font-style: italic;
    border: 1px solid #fbbf24;
}

.input-container {
    background-color: white;
    padding: 1.5rem;
    border-radius: 12px;
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

.metric-card {
    background-color: white;
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
}

.status-indicator {
    display: inline-block;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    margin-right: 8px;
}

.status-online {
    background-color: #10b981;
}

.status-offline {
    background-color: #ef4444;
}

.timestamp {
    font-size: 0.75rem;
    color: #6b7280;
    margin-top: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'system_prompt' not in st.session_state:
    st.session_state.system_prompt = "You are a helpful AI assistant. Answer questions clearly and concisely."
if 'chat_count' not in st.session_state:
    st.session_state.chat_count = 0

# Set API key - Replace with your actual API key
# os.environ['OPENAI_API_KEY'] = 'your-openai-api-key-here'
# Or set it as an environment variable: export OPENAI_API_KEY="your-key-here"

# Main header
st.markdown('<h1 class="main-header">🤖 ChatGPT Clone</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Intelligent AI Assistant with Custom System Prompts</p>', unsafe_allow_html=True)

# Sidebar for configuration
with st.sidebar:
    st.markdown("### ⚙️ Configuration")
    st.markdown("---")
    
    # Model selection
    model_options = {
        "gpt-3.5-turbo": "Fast and cost-effective",
        "gpt-3.5-turbo-16k": "Extended context (16k tokens)",
        "gpt-4": "Most capable model",
        "gpt-4-turbo": "Latest GPT-4",
        "gpt-4o": "Multimodal model",
        "gpt-4o-mini": "Faster GPT-4 variant"
    }
    
    model_choice = st.selectbox(
        "Select OpenAI Model:",
        list(model_options.keys()),
        index=0,
        help="Choose the OpenAI model for chat"
    )
    
    st.caption(f"💡 {model_options[model_choice]}")
    
    # Temperature setting
    temperature = st.slider(
        "Temperature:",
        min_value=0.0,
        max_value=2.0,
        value=0.7,
        step=0.1,
        help="Controls randomness. Lower = more focused, Higher = more creative"
    )
    
    # Max tokens
    max_tokens = st.slider(
        "Max Tokens:",
        min_value=100,
        max_value=4000,
        value=1000,
        step=100,
        help="Maximum length of response"
    )
    
    st.markdown("---")
    st.markdown("### 🎯 System Prompt")
    
    # System prompt input
    new_system_prompt = st.text_area(
        "Custom System Prompt:",
        value=st.session_state.system_prompt,
        height=100,
        help="Define how the AI should behave and respond"
    )
    
    if st.button("🔄 Update System Prompt"):
        st.session_state.system_prompt = new_system_prompt
        st.success("System prompt updated!")
        st.rerun()
    
    st.markdown("---")
    st.markdown("### 📊 Chat Statistics")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Messages", len(st.session_state.messages))
    with col2:
        st.metric("Model", model_choice)
    
    # API status
    try:
        client = get_client()
        st.success("🟢 API Connected")
    except:
        st.error("🔴 API Error")
    
    st.markdown("---")
    st.markdown("### 🛠️ Actions")
    
    # Clear chat button
    if st.button("🗑️ Clear Chat", help="Clear all messages"):
        st.session_state.messages = []
        st.session_state.chat_count = 0
        st.success("Chat cleared!")
        st.rerun()
    
    # Export chat button
    if st.button("📥 Export Chat"):
        if st.session_state.messages:
            chat_text = "\n\n".join([f"{msg['role'].title()}: {msg['content']}" for msg in st.session_state.messages])
            st.download_button(
                label="Download Chat",
                data=chat_text,
                file_name=f"chat_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )
        else:
            st.warning("No messages to export")

# System Prompt Section
st.markdown("### 🎯 System Prompt Configuration")
with st.expander("🔧 Customize AI Behavior", expanded=False):
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # System prompt input with placeholder
        system_prompt_input = st.text_area(
            "System Prompt:",
            value=st.session_state.system_prompt,
            height=120,
            placeholder="Enter your custom system prompt here...\n\nExamples:\n- 'You are a helpful coding assistant'\n- 'You are a creative writing expert'\n- 'You are a professional business consultant'\n- 'Answer all questions in a friendly, conversational tone'",
            help="Define how the AI should behave and respond. This sets the personality and behavior of your AI assistant."
        )
    
    with col2:
        st.markdown("**💡 Quick Templates:**")
        
        if st.button("🤖 Coding Assistant"):
            st.session_state.system_prompt = "You are a helpful coding assistant. Provide clear, well-commented code examples and explain programming concepts thoroughly."
            st.rerun()
        
        if st.button("✍️ Creative Writer"):
            st.session_state.system_prompt = "You are a creative writing expert. Help with storytelling, character development, and creative expression."
            st.rerun()
        
        if st.button("💼 Business Consultant"):
            st.session_state.system_prompt = "You are a professional business consultant. Provide strategic advice and practical business solutions."
            st.rerun()
        
        if st.button("🎓 Tutor"):
            st.session_state.system_prompt = "You are a patient and knowledgeable tutor. Explain concepts clearly and adapt to different learning styles."
            st.rerun()
        
        if st.button("🔄 Reset"):
            st.session_state.system_prompt = "You are a helpful AI assistant. Answer questions clearly and concisely."
            st.rerun()
    
    # Update button
    if st.button("🔄 Update System Prompt", type="primary"):
        st.session_state.system_prompt = system_prompt_input
        st.success("✅ System prompt updated successfully!")
        st.rerun()
    
    # Display current system prompt
    st.markdown("**Current System Prompt:**")
    st.info(f"💬 {st.session_state.system_prompt}")

st.markdown("---")

# Main chat interface
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Show system prompt status
if st.session_state.system_prompt != "You are a helpful AI assistant. Answer questions clearly and concisely.":
    st.markdown(f'''
    <div class="message-system">
        <strong>🎯 Active System Prompt:</strong> {st.session_state.system_prompt}
    </div>
    ''', unsafe_allow_html=True)

# Display chat messages
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f'''
        <div class="message-user">
            <strong>You:</strong><br>
            {message["content"]}
            <div class="timestamp">{message.get("timestamp", "")}</div>
        </div>
        ''', unsafe_allow_html=True)
    elif message["role"] == "assistant":
        st.markdown(f'''
        <div class="message-assistant">
            <strong>🤖 Assistant:</strong><br>
            {message["content"]}
            <div class="timestamp">{message.get("timestamp", "")}</div>
        </div>
        ''', unsafe_allow_html=True)
    elif message["role"] == "system":
        st.markdown(f'''
        <div class="message-system">
            <strong>System:</strong> {message["content"]}
        </div>
        ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Floating System Prompt Panel
if st.session_state.get('show_system_prompt', False):
    st.markdown("### 🎯 Quick System Prompt Editor")
    with st.container():
        col_quick1, col_quick2 = st.columns([4, 1])
        
        with col_quick1:
            quick_prompt = st.text_area(
                "Quick Edit System Prompt:",
                value=st.session_state.system_prompt,
                height=80,
                key="quick_prompt_editor",
                placeholder="Enter your system prompt here..."
            )
        
        with col_quick2:
            if st.button("✅ Apply", type="primary"):
                st.session_state.system_prompt = quick_prompt
                st.session_state.show_system_prompt = False
                st.success("System prompt updated!")
                st.rerun()
            
            if st.button("❌ Close"):
                st.session_state.show_system_prompt = False
                st.rerun()
    
    st.markdown("---")

# Chat input
st.markdown('<div class="input-container">', unsafe_allow_html=True)

# Quick system prompt access
col_input1, col_input2, col_input3 = st.columns([6, 1, 1])

with col_input1:
    # Text input for user message
    user_input = st.text_input(
        "Type your message:",
        placeholder="Ask me anything...",
        key="user_input"
    )

with col_input2:
    # Quick system prompt button
    if st.button("🎯", help="Quick System Prompt Access"):
        st.session_state.show_system_prompt = not st.session_state.get('show_system_prompt', False)
        st.rerun()

with col_input3:
    # Clear chat button
    if st.button("🗑️", help="Clear Chat"):
        st.session_state.messages = []
        st.session_state.chat_count = 0
        st.success("Chat cleared!")
        st.rerun()

# Send button
col1, col2, col3 = st.columns([1, 1, 8])
with col1:
    send_button = st.button("📤 Send", type="primary")
with col2:
    clear_button = st.button("🗑️ Clear")

st.markdown('</div>', unsafe_allow_html=True)

# Handle send button
if send_button and user_input:
    # Add user message
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.messages.append({
        "role": "user", 
        "content": user_input,
        "timestamp": timestamp
    })
    
    # Prepare messages for API call
    api_messages = [{"role": "system", "content": st.session_state.system_prompt}]
    api_messages.extend([{"role": msg["role"], "content": msg["content"]} for msg in st.session_state.messages])
    
    # Get AI response
    with st.spinner("🤖 AI is thinking..."):
        ai_response = get_ai_response(api_messages, model_choice, temperature, max_tokens)
    
    # Add assistant message
    st.session_state.messages.append({
        "role": "assistant", 
        "content": ai_response,
        "timestamp": timestamp
    })
    
    st.session_state.chat_count += 1
    st.rerun()

# Handle clear button
if clear_button:
    st.session_state.messages = []
    st.session_state.chat_count = 0
    st.rerun()

# Quick actions
st.markdown("### 🚀 Quick Actions")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("💡 Explain"):
        if st.session_state.messages:
            st.session_state.messages.append({
                "role": "user", 
                "content": "Please explain this in simple terms",
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })
            st.rerun()

with col2:
    if st.button("📝 Summarize"):
        if st.session_state.messages:
            st.session_state.messages.append({
                "role": "user", 
                "content": "Please summarize our conversation",
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })
            st.rerun()

with col3:
    if st.button("🔍 More Details"):
        if st.session_state.messages:
            st.session_state.messages.append({
                "role": "user", 
                "content": "Please provide more details about this topic",
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })
            st.rerun()

with col4:
    if st.button("❓ Ask Question"):
        if st.session_state.messages:
            st.session_state.messages.append({
                "role": "user", 
                "content": "What questions should I ask about this topic?",
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #6b7280; padding: 2rem;'>
    <p>🤖 Powered by OpenAI GPT | Built with Streamlit</p>
    <p>💡 Tip: Use the sidebar to customize your AI assistant's behavior</p>
</div>
""", unsafe_allow_html=True)
