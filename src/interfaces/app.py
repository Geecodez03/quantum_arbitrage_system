from fastapi import FastAPI
from src.core.execution.router import OrderRouter
from src.infrastructure.token_manager import TokenManager
from typing import Any

app = FastAPI()
router = OrderRouter()
token_service = TokenManager()


@app.get("/health")
async def health_check():
    return {"status": "OK"}


@app.post("/execute")
async def execute_trade(symbol: str, amount: float) -> dict[str, Any]:
    return {
        "action": "buy",
        "symbol": symbol,
        "amount": amount,
    }  # Explicitly typed as dict[str, Any]
    # Add your execution logic here
    return {"action": "buy", "symbol": symbol, "amount": amount}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
