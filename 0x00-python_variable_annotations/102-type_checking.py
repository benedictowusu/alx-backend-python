from typing import Tuple, Any

def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple[Any, ...]:
    zoomed_in: Tuple[Any, ...] = tuple(
        item for item in lst
        for _ in range(factor)
    )
    return zoomed_in


array = (12, 72, 91)  # Use tuple instead of list for array

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Use integer instead of float for the factor
