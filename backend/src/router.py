from fastapi import APIRouter
from src.http_client import CMCHTTPClient
from src.config import settings

cmc_http_client = CMCHTTPClient(
    base_url='https://pro-api.coinmarketcap.com',
    api_key=settings.API_KEY)


router = APIRouter(prefix='/currencies', tags=['currencies'])


@router.get('/')
async def get_cryptocurrencies():
    all_currencies = await cmc_http_client.get_listings()
    return all_currencies


@router.get('/{currency_id}')
async def get_currency(currency_id: int):
    currency = await cmc_http_client.get_currency(currency_id)
    return currency
