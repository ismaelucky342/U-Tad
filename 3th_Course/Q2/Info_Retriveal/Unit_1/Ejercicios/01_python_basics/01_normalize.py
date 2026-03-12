PUNCT = '.,;:!?()[]{}"\''


def normalize(text: str) -> str:
    """Normaliza texto.

    TODO:
    - Minúsculas
    - Sustituir puntuación por espacio
    - Colapsar espacios múltiples
    - Strip
    """
    # TODO: implement
    raise NotImplementedError


def tokenize(text: str) -> list[str]:
    """Tokeniza texto usando normalize.

    TODO:
    - Llamar a normalize
    - Split por espacios
    - Filtrar tokens vacíos
    """
    # TODO: implement
    raise NotImplementedError


def term_frequencies(tokens: list[str]) -> dict[str, int]:
    """Cuenta frecuencias por token."""
    # TODO: implement
    raise NotImplementedError


if __name__ == "__main__":
    sample = "Hola,  Mundo!!  Hola..."
    print("Original:", sample)
    # TODO: cuando implementes, descomenta
    # print("Normalized:", normalize(sample))
    # print("Tokens:", tokenize(sample))
    # print("TF:", term_frequencies(tokenize(sample)))
