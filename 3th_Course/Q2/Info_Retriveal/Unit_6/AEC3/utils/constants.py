"""Constantes y patrones regex compilados."""

import re

# --- Patrones de texto ---
RE_URL = re.compile(r'https?://\S+|www\.\S+', re.IGNORECASE)
RE_MENTION = re.compile(r'@\w+')
RE_HASHTAG = re.compile(r'#(\w+)')
RE_SPECIAL = re.compile(r'[^\w\s#]', re.UNICODE)
RE_SPACES = re.compile(r'\s+')
MENTION_EXTRACT = re.compile(r'@(\w+)')  # Para extraer solo el nombre sin @

# --- Configuración por defecto ---
DEFAULT_CHUNKSIZE = 100_000
DEFAULT_NUM_TOPICS = 5
DEFAULT_PASSES = 10
DEFAULT_MAX_TOKENS = 512
DEFAULT_TEMPERATURE = 0.7

# --- Directorios ---
DATASETS_DIR = "datasets"
OUTPUTS_DIR = "outputs"

# --- Modelos LLM por defecto ---
DEFAULT_LLM_MODEL = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"  # Ligero, runs on CPU/low VRAM
# Alternativas: "google/gemma-2-2b-it", "meta-llama/Llama-2-7b-chat-hf"
