from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import service
import uvicorn

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/pages")
def pages():
    return service.get_pages()

@app.get("/pages/{page_name}")
def list(page_name: str):
    return service.get_news(page_name)

# Run the API using Uvicorn (optional)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)