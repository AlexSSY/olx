from dataclasses import dataclass


@dataclass
class Item:
    name: str
    url: str


@dataclass
class Category:
    name: strE


def get_categories() -> list[Category]:
    pass


def get_items(category: Category) -> list[Item]:
    pass


if __name__ == '__main__':
    pass