from fastapi import FastAPI
import uvicorn
from src.routers import router as tasks_router

app = FastAPI()
app.include_router(tasks_router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8080, reload=True)