from typing import Dict, List


def get_book_text(f_path: str) -> str:
    with open(f_path, "r") as f:
        return f.read()


def count_chars(content: str) -> Dict[str, int]:
    char_counts = {}

    for c in content:
        lower_c = c.lower()
        char_counts[lower_c] = char_counts.get(lower_c, 0) + 1

    return char_counts


def sort_on_char_count(char_count: Dict) -> int:
    return char_count["num"]


def chars_dict_to_sorted_list(chars: Dict[str, int], reverse=True) -> List[Dict]:
    counts = [{"name": key, "num": val} for key, val in chars.items()]
    counts.sort(reverse=reverse, key=sort_on_char_count)

    return counts
