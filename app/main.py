from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Zeabur + FastAPI!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

# Optional: Read port from env (for dev, Zeabur will override it)
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8080))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)
