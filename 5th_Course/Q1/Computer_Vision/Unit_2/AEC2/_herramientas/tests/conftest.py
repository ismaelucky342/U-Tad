"""Configuración de pytest para importar el banco de pruebas."""

from __future__ import annotations

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
CODIGO = RAIZ / "U2_Practica_Hernandez_Ismael" / "codigo"
if str(CODIGO) not in sys.path:
    sys.path.insert(0, str(CODIGO))
