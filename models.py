from pydantic import BaseModel, Field, HttpUrl
from typing import Union, Optional, List, Literal


class createPaymentReq(BaseModel):
    amount: int
    return_url: Optional[HttpUrl] = Field(None, alias="returnUrl")
    payer_identity: Optional[str] = Field(None, alias="payerIdentity")
    description: Optional[str] = Field(None, alias="payerName")
    client_ref_id: Optional[str] = Field(None, alias="clietnRefId")
    national_code: Optional[str] = Field(None, alias="nationalCode")


class createPaymentResponse(BaseModel):
    payment_code: str
    return_url: HttpUrl
    amount: int


class startPaymentReq(BaseModel):
    code: str


class deletePaymentRequest(startPaymentReq): ...


class verifyPaymentReq(BaseModel):
    payment_ref_id: int = Field(alias="paymentRefId")
    payment_code: str = Field(alias="paymentCode")
    amount: int


class SharedPaymentItem(BaseModel):
    amount: int
    payment_code: str = Field(alias="paymentCode")
    user_identity: str = Field(alias="userIdentity")


class VerifyPaymentResponse(BaseModel):
    amount: int
    card_number: str = Field(alias="cardNumber")
    card_hash_pan: str = Field(alias="cardHashPan")
    client_ref_id: str = Field(alias="clientRefId")
    payment_ref_id: int = Field(alias="paymentRefId")
    code: str
    payed_date: str = Field(alias="payedDate")
    payer_wage: int = Field(alias="payerWage")
    business_wage: int = Field(alias="businessWage")
    gateway_amount: int = Field(alias="gatewayAmount")
    shared_payment_items: List[SharedPaymentItem] = Field(alias="sharedPaymentItems")

    class Config:
        allow_population_by_field_name = True


class reversePaymentReq(BaseModel):
    payment_ref_id: int = Field(alias="paymentRefId")
    payment_code: str = Field(alias="paymentCode")


class ReversePaymentResponse(BaseModel):
    amount: int
    client_ref_id: str = Field(alias="clientRefId")
    payment_ref_id: int = Field(alias="paymentRefId")
    code: str
    payer_wage: int = Field(alias="payerWage")
    gateway_amount: int = Field(alias="gatewayAmount")
    reversed_date: str = Field(alias="reversedDate")
    shared_payment_items: List[SharedPaymentItem] = Field(alias="sharedPaymentItems")

    class Config:
        allow_population_by_field_name = True


# * models for nobitext client


class nobitextBalanceReq(BaseModel):
    currency: Literal["ltc", "btc", "eth", "usdt", "tron"]


class pagination(BaseModel):
    page: Optional[int] = None
    page_size: Optional[int] = Field(None, alias="pageSize")


class nobitextTransactionsReq(pagination):
    wallet_id: int = Field(alias="wallet")


class nobitextDepositsReq(BaseModel): ...


class nobitextDepositsResponse(BaseModel): ...


# * models for arc


class GetAccountBalanceResponse(BaseModel):
    availableBalance: float
    actualBalance: float
