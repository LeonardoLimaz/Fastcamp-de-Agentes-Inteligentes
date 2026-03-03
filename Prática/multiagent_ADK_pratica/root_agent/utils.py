import json
from typing import Any, Dict

def ensure_dict(value: Any) -> Dict[str, Any]:
    """
    Converte o que vier do state em dict JSON-safe:
    - dict -> dict
    - str (JSON) -> dict
    - bytes -> decode utf-8 e json.loads
    """
    if value is None:
        return {}

    if isinstance(value, dict):
        return value

    if isinstance(value, bytes):
        value = value.decode("utf-8", errors="ignore")

    if isinstance(value, str):
        s = value.strip()
        # se vier texto com JSON, tenta carregar
        try:
            return json.loads(s)
        except Exception:
            return {"_raw": s}

    # fallback: força string
    return {"_raw": str(value)}