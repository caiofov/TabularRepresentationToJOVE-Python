from typing import Optional


class Converter:
    """Converts a tabular representation of an automata into a text accepted by JOVE library
    Example:
        Input:
                a | b
            1 | 2 | 1
        Output:
            1: a -> 2
            1: b -> 1
    """

    def __init__(
        self,
        initial_state=str,
        end_states=list[str],
        symbols: dict[str, str] = {},
    ) -> None:
        self.initial_state = initial_state
        self.end_states = end_states
        self.symbols = symbols
        self.output = ""

    def convert(self, output_file: Optional[str] = None) -> str:
        pass

    def _parse_state(self, state: str) -> str:
        pass
