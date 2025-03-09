import librosa
import numpy as np
import torch
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
from sentence_transformers import SentenceTransformer, util

# Load pre-trained models
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")
sentence_model = SentenceTransformer("all-MiniLM-L6-v2")


def transcribe_audio(audio_path):
    """Convert audio to text using Wav2Vec2"""
    audio, sr = librosa.load(audio_path, sr=16000)
    input_values = processor(audio, return_tensors="pt", sampling_rate=sr).input_values

    with torch.no_grad():
        logits = model(input_values).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)[0]

    return transcription


def process_audio_and_compare(original_audio_path, user_audio_path):
    """Transcribe and compare audio similarity"""
    original_text = transcribe_audio(original_audio_path)
    user_text = transcribe_audio(user_audio_path)

    # Compute similarity score
    embedding1 = sentence_model.encode(original_text, convert_to_tensor=True)
    embedding2 = sentence_model.encode(user_text, convert_to_tensor=True)
    similarity_score = util.pytorch_cos_sim(embedding1, embedding2).item() * 100

    return round(similarity_score, 2)
