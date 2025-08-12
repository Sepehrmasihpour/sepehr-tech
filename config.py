from dotenv import load_dotenv
from pydantic import BaseSettings, Field

# 1) Populate os.environ from .env
load_dotenv()


class Settings(BaseSettings):
    payping_base_url: str = Field(..., env="PAYPING_BASE_URL")
    payping_access_token: str = Field(..., env="PAYPING_ACCESS_TOKEN")
    payping_callback_url: str = Field(..., env="PAYPING_CALLBACK_URL")

    arc_base_url: str = Field(..., env="ARC_BASE_URL")
    arc_client_id: str = Field(..., env="ARC_CLIENT_ID")
    arc_client_secret: str = Field(..., env="ARC_CLIENT_SECRET")
    bank_acount_number = int = Field(..., env="BANK_ACOUNT_NUMBER")

    nobitex_auth_token: str = Field(..., env="NOBITEX_AUTH_TOKEN")
    nobitex_base_url: str = Field(..., env="NOBITEX_BASE_URL")
    nobitex_sheba: str = Field(..., env="NOBITEX_SHEBA")

    rpc_url: str = Field(..., env="RPC_URL")
    hot_wallet_address: str = Field(..., env="HOT_WALLET_ADDRESS")
    hot_wallet_private_key: str = Field(..., env="HOT_WALLET_PRIVATE_KEY")

    app_base_url: str = Field(..., env="APP_BASE_URL")


settings = Settings()
