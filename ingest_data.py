from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create the FastAPI app instance with metadata
app = FastAPI(
    title="Data Ingestion API",
    description="An API to ingest and validate data for a machine learning model. Ensures feature_1 is non-negative and feature_2 does not exceed 280 characters.",
    version="1.0.0"
)

class Data(BaseModel):
    feature_1: float
    feature_2: str

@app.post("/ingest_data")
async def ingest_data(data: Data):
    if data.feature_1 < 0:
        raise HTTPException(status_code=400, 
        detail="feature_1 must be non-negative")

    if len(data.feature_2) > 280:
        raise HTTPException(status_code=400, 
        detail="feature_2 must be 280 characters or less")
    
    return {"message": "Data ingested successfully", "data": data}
