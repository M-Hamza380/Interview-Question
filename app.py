import uvicorn, time
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from src.utils.common import get_setting
from src.routers.router import router as llm_route

start_process = time.process_time()
print(f"Start process time: {start_process} seconds")

app = FastAPI(
    title="Interview Question Creator",
    description="An advanced, production-ready generative AI application that automates the creation of " \
    "tailored interview questions using cutting-edge Retrieval-Augmented Generation (RAG) techniques.",
    version="0.0.2"
)

# Configure CROS
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["POST", "GET"],
    allow_headers = ["*"]
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
app.include_router(llm_route, prefix="/api/v2", tags=["llm route"])

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    try:
        settings = get_setting()
        print(f"Starting the server with Settings: {settings.debug}")

        if settings.debug:
            print("Debug mode is enabled!")
            uvicorn.run("app:app", host="localhost", port=8080, reload=True)
            print(f"Process took {time.process_time() - start_process} seconds")
        else:
            print("Debug mode is disable!")
            uvicorn.run("app:app", host="localhost", port=8080, workers=2)
            print(f"Process took {time.process_time() - start_process} seconds")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    