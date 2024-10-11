"""
Main entry point for the FastAPI application.
"""

from fastapi import FastAPI
from app.routers import items, clock_in
from app.lib.db import connect_db

# Initialize FastAPI app
app = FastAPI()

# Connect to MongoDB
connect_db()

# Include routers for Items and Clock-In Records
app.include_router(items.router)
app.include_router(clock_in.router)

# Health check endpoint
@app.get("/")
async def root():
    """
    Health check endpoint to confirm the application is running.
    """
    return {"message": "FastAPI Assignment is running"}
