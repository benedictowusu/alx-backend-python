from typing import Any, List, Union

def safe_first_element(lst: List[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
