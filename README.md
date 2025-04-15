# Collaborative-Code-Debugger-using-Gen-AI

This tool is a Real-Time Collaborative Code Editor that aims to facilitate remote developer collaboration. The platform should allow multiple users to edit the same code file simultaneously, with changes reflected in real-time. Additionally, the platform also integrates an AI model to analyze the code and provide debugging suggestions (e.g., syntax errors, potential bugs, performance improvements).

# Core Features

**1. Real-Time Collaboration:**
Allow multiple users to edit the same code file simultaneously.
Sync changes in real-time using WebSockets or a similar technology.
Show live cursors and highlights for each user.

**2. AI-Assisted Debugging:**
Integrated an AI model -DeepSeek to analyze the code.
Provide real-time suggestions for syntax errors, potential bugs, and performance improvements.
Allow users to accept or reject AI suggestions.

**3. User Management:**
Allow users to create accounts, log in, and join code editing sessions.
Implement role-based access control (e.g., owner, collaborator).

**4. Data Modeling:**
Designed a database schema to store users, code files, and editing sessions.

**5. API Design:**
Built RESTful APIs using FastAPI for user management, code file management, and AI debugging.
Implemented request/response validation using Pydantic models.

**6. Real-Time Communication:**
Implemented real-time collaboration using WebSockets to handle conflicts when multiple users edit the same part of the code simultaneously.

**7. AI Integration:**
Integrated  an AI model to analyze code and provide debugging suggestions.
