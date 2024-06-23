from pydantic import BaseModel # type: ignore


class AccessTokenResponseModel(BaseModel):
    access_token: str = None
    token_type: str = None
    expires_in: int = None
