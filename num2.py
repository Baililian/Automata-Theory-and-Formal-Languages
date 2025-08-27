enter = ["ab", "ba", "bba", "a", "babb", "bbb"]

def automation2(s):
    state = "q0"
    for c in s:
        if state == "q0":
            state = "q1" if c == "a" else "q2"
        elif state == "q1":
            state = "q0" if c == "a" else "q3"
        elif state == "q2":
            state = "q3" if c == "a" else "q0"
        elif state == "q3":
            state = "q2" if c == "a" else "q1"
    return state == "q3"

print("\nAutomaton:")
for s in enter:
    print(f"{s} = {'ACCEPTED' if automation2(s) else 'REJECTED'}")