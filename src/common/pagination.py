from typing import Generic, List, TypeVar
from pydantic import BaseModel
from math import ceil

T = TypeVar("T")


class PaginatedResponse(Generic[T], BaseModel):
    items: List[T]
    total_items: int
    total_pages: int
    current_page: int
    items_per_page: int


def paginate(queryset, page: int, page_size: int):
    total_items = queryset.count()
    total_pages = ceil(total_items / page_size)

    items = queryset.offset((page - 1) * page_size).limit(page_size).all()

    return PaginatedResponse(
        items=items,
        total_items=total_items,
        total_pages=total_pages,
        current_page=page,
        items_per_page=page_size,
    )
