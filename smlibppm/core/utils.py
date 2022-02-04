import random as rand


def generate_rand_color() -> list:
    """[generates a random colored pixel]

    Returns:
        list: [a random colored pixel]
    """
    pixel = [
        f"{rand.randint(0,255)} ",
        f"{rand.randint(0,255)} ",
        f" {rand.randint(0,255)} ",
    ]

    return pixel
