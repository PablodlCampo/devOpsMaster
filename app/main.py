from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/hello")
def hello():
    return {"response": "Hello, World!"}

class QuestionRequest(BaseModel):
    question: str

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "size_bytes": file.size,
        "content_type": file.content_type
    }

@app.post("/ask")
def ask_question(body: QuestionRequest):
    return {
        "question": body.question,
        "answer": "Esto es una respuesta de prueba. Aquí irá el LLM en la Fase 2."
    }