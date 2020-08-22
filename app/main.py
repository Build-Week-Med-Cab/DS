"""FastAPI app definition."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api import labels, recommends

app = FastAPI(
    title='DS Med Cabinet 3',
    description='API page for DS',
    version='0.1.2',
    docs_url='/',
)

app.include_router(labels.router)
app.include_router(recommends.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)
