import csv

symbols = {"Ã˜": "v"}  # Ã˜ = Ø
initial_state = "1"
end = ["2", "6"]
output = ""


def parse_state(state: str) -> str:
    global symbols, initial_state, end
    state = symbols.get(state, state)
    if state == initial_state:
        state = f"I{state}"
    elif state in end:
        state = f"F{state}"

    return state


def main() -> None:
    with open("input.csv") as f:
        reader = csv.reader(f)
        l = list(reader)
        header = l[0][1:]
        states = l[1:]
        del l

    for state in states:
        st = parse_state(state[0])
        transitions = state[1:]
        for next_st, letter in zip(transitions, header):
            next_st = parse_state(next_st)
            output += f"{st}: {letter} -> {next_st}\n"
    with open("output.txt", "w") as out:
        out.write(output)

    print(output)


if __name__ == "__main__":
    main()
