def validate_number(num_str: str, min_num: int|float, max_num: int|float) -> bool:
    try:
        valid_number = int(num_str)
        
        if min_num < valid_number < max_num:
            return True
    except:
        pass
    return False


def validate_length(string: str, length: int) -> bool:
    return len(string) >= length