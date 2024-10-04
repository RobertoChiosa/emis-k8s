#  Copyright © Roberto Chiosa 2024.
#  Email: roberto.chiosa@polito.it
#  Last edited: 4/10/2024

# Third party imports
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

# Project imports
from src.api.db import models
from src.api.db.database import engine
from src.api.metadata import *
from src.api.routers import data, metadata, report

# create the database tables
models.Base.metadata.create_all(bind=engine)

# create app instance
app = FastAPI(
    title=title,
    description=description,
    version=version,
    terms_of_service=terms_of_service,
    contact=contact,
    license_info=license_info,
    openapi_tags=openapi_tags,
)

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to the specific origins you want to allow
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(report.router)
app.include_router(metadata.router)
app.include_router(data.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
