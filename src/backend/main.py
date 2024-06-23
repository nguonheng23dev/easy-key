import os
from datetime import datetime, timedelta, timezone

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware 
from models import AccessTokenResponseModel
from token_cache import TokenCache
from utils.url_creation import make_url_query_string

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

load_dotenv()
token_cache = TokenCache()

# Environmental variables
CLIENT_ID: str = os.getenv('CLIENT_ID')
CLIENT_SECRET: str = os.getenv('CLIENT_SECRET')

# Endpoints
SPOTIFY_TOKEN_URL:  str = 'https://accounts.spotify.com/api/token'
SPOTIFY_SEARCH_URL: str = 'https://api.spotify.com/v1/search'


@app.get("/")
async def root():
    return {"message": "Hello there!"}

async def fetch_new_token() -> AccessTokenResponseModel:
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(SPOTIFY_TOKEN_URL, headers=headers, data=data)
    
    if response.status_code == 200:
        token_data = response.json()
        expiration_time = datetime.now(timezone.utc) + timedelta(seconds=token_data['expires_in'])
        token_cache.access_token = token_data['access_token']
        token_cache.expiration_time = expiration_time
        return AccessTokenResponseModel(**token_data)
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)

@app.get('/get-token', response_model=AccessTokenResponseModel)
async def get_access_token():

    if token_cache.expiration_time is None or token_cache.expiration_time <= datetime.now(timezone.utc):
        return await fetch_new_token()

    return AccessTokenResponseModel(
        access_token=token_cache.access_token,
        token_type='Bearer',
        expires_in=int((token_cache.expiration_time - datetime.now(timezone.utc)).total_seconds())
    )


@app.get("/search")
async def search(query: str):

    if token_cache.expiration_time is None or token_cache.expiration_time <= datetime.now(timezone.utc):
        await fetch_new_token()

    headers = {
        'Authorization': 'Bearer ' + token_cache.access_token
    }

    search_query = make_url_query_string(query)

    async with httpx.AsyncClient() as client:
        response = await client.get(SPOTIFY_SEARCH_URL + search_query, headers=headers)

        if response.status_code == 200:
            search_results = response.json()
            return search_results
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
