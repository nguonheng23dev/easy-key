from typing import List


def make_url_query_string(query: str, 
                          search_types: List[str] = ['track'], 
                          limit: int = 10, 
                          offset: int = 0) -> str:
    query = query.strip().replace(' ', '+')
    types = search_types[0].strip()

    return f'?q={query}&type={types}&limit={limit}&offset={offset}'