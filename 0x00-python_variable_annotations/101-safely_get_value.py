from typing import TypeVar, Dict, Any

KT = TypeVar('KT')  # TypeVar for the key type
VT = TypeVar('VT')  # TypeVar for the value type

def safely_get_value(dct: Dict[KT, VT], key: KT, default: VT = None) -> VT:
    if key in dct:
        return dct[key]
    else:
        return default
