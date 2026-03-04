from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from risk_engine import calculate_trust_score

from models.face_model import face_match_score
from models.deepfake_model import deepfake_score
from models.liveness_model import liveness_score
from models.ocr_engine import document_auth_score

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/verify")
async def verify_identity(
    selfie: UploadFile = File(...),
    id_card: UploadFile = File(...)
):
    face_score = face_match_score()
    deepfake = deepfake_score()
    live_score = liveness_score()
    doc_score = document_auth_score()

    trust_score, flags = calculate_trust_score(
        face_score, deepfake, live_score, doc_score
    )

    return {
        "trust_score": trust_score,
        "flags": flags,
        "face_score": face_score,
        "deepfake_probability": deepfake,
        "liveness_score": live_score,
        "document_score": doc_score
    }
