#!/usr/bin/env bash
set -euo pipefail

# Enunciado: definir pares clave-valor y describir Map/Shuffle/Reduce.
# Objetivo: comprender la logica MapReduce sin codigo.

cat <<'EOF'
Datos de ejemplo (CSV)
----------------------
TiendaA,2026-03-10,12
TiendaB,2026-03-10,7
TiendaA,2026-03-11,5
TiendaB,2026-03-11,4

Lo que se espera obtener
------------------------
Map:
  (TiendaA, 12)
  (TiendaB, 7)
  (TiendaA, 5)
  (TiendaB, 4)

Shuffle:
  TiendaA -> [12, 5]
  TiendaB -> [7, 4]

Reduce:
  TiendaA -> 17
  TiendaB -> 11
EOF
