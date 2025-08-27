enter = ["10", "1000", "110", "101", "01", "111"]

def automation1(s):
    state = "a"
    for c in s:
        if state == "a":
            state = "a" if c == "0" else "b"
        elif state == "b":
            state = "1" if c == "0" else "a"
        elif state == "1":
            state = "1" if c == "0" else "1"   
    return state == "1"

print("Automaton:")
for s in enter:
    print(f"{s} = {'ACCEPTED' if automation1(s) else 'REJECTED'}")