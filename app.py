# Import dependencies
import streamlit as st
import asyncio
import websockets
import json
import requests
from streamlit_ace import st_ace

# Server details
FASTAPI_URL = "http://127.0.0.1:8000"
WS_URL = "ws://localhost:8000/ws/collaborate" 

# Initialize session state
if "code" not in st.session_state:
    st.session_state["code"] = ""
if "ws" not in st.session_state:
    st.session_state["ws"] = None  

# WebSocket communication (Persistent Connection)
async def connect_ws():
    """Create a persistent WebSocket connection."""
    if st.session_state["ws"] is None or st.session_state["ws"].closed:
        st.session_state["ws"] = await websockets.connect(WS_URL)

async def send_code_update(code):
    """Send updated code to WebSocket server."""
    await connect_ws() 
    update = json.dumps({"code": code})
    await st.session_state["ws"].send(update)

# Streamlit UI
st.title("Real-Time Collaborative Code Editor with AI Debugging")

# Code editor (without on_change)
new_code = st_ace(
    value=st.session_state["code"],  # Load session state
    language="python",
    theme="monokai",
    keybinding="vscode",
    font_size=14
)

# Detect code changes manually
if new_code != st.session_state["code"]:
    st.session_state["code"] = new_code
    asyncio.create_task(send_code_update(new_code))

# AI Debugging
if st.button("Analyze Code"):
    response = requests.post(f"{FASTAPI_URL}/debug/", json={"code": st.session_state["code"]}) 
    if response.status_code == 200:
        st.subheader("AI Suggestions")
        st.write(response.json().get("suggestions", "No suggestions available."))
    else:
        st.error(f"Error analyzing code: {response.text}") 
