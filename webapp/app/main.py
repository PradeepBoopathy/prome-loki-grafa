from fastapi import FastAPI
from logging import getLogger
import logging
from pathlib import Path

log_dir = Path("/var/log/webapp")
log_dir.mkdir(parents=True, exist_ok=True)
file_handler = logging.FileHandler(log_dir / "webapp.log")
file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
logging.getLogger().addHandler(file_handler)

app = FastAPI(title="Hello‑World service")

@app.get("/")
async def hello_world() -> str:
    logging.info("root endpoint hit")
    return "Hello World!"

@app.get("/ping")
async def ping() -> dict[str, str]:
    logging.info("ping endpoint hit")
    return {"message": "pong"}

@app.get("/greet/{name}")
async def greet(name: str) -> dict[str, str]:
    logging.info("greet endpoint hit", extra={"name": name})
    return {"message": f"Hello {name}!"}