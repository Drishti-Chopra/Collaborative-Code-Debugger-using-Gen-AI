from fastapi import FastAPI
from api import users, debug, codes
from websocket import router as websocket_router
import nest_asyncio
nest_asyncio.apply()

from database import engine
import models as models

# Ensure all tables are created
models.Base.metadata.create_all(bind=engine)


# Initialize FastAPI app
app = FastAPI(title="Real-Time Collaborative Code Editor with AI Debugging")

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(debug.router, prefix="/debug", tags=["Debugging"]) 
app.include_router(codes.router, prefix="/codes", tags=["Code Files"]) 
app.include_router(websocket_router, prefix="/ws", tags=["WebSocket"])

@app.get("/")
async def root():
    return {"message": "Hello World"}