class State:
    def __init__(self, name, output=None):
        self.name = name
        self.output = output
        self.transitions = {}
    
    def add_transition(self, input_symbol, next_state):
        self.transitions[input_symbol] = next_state


class MooreMachine:
    def __init__(self, initial_state):
        self.states = {}
        self.initial_state = initial_state
        self.current_state = initial_state
    
    def add_state(self, state):
        self.states[state.name] = state
    
    def add_transition(self, from_state, input_symbol, to_state):
        self.states[from_state].transitions[input_symbol] = to_state
    
    def process_input(self, input_string):
        self.current_state = self.initial_state
        outputs = [self.states[self.current_state].output]
        
        for symbol in input_string:
            self.current_state = self.states[self.current_state].transitions[symbol]
            outputs.append(self.states[self.current_state].output)
        
        return ''.join(outputs)


def build_moore_machine():
    moore = MooreMachine('A_A')
    
    # Create states
    states = [
        State('A_A', 'A'), State('B_B', 'B'), State('C_A', 'A'),
        State('D_B', 'B'), State('D_C', 'C'), State('C_C', 'C'),
        State('E_C', 'C')  
    ]
    for state in states:
        moore.add_state(state)
    
    # Add transitions 
    transitions = [
        ('A_A', '0', 'A_A'), ('A_A', '1', 'B_B'),
        ('B_B', '0', 'C_A'), ('B_B', '1', 'D_B'),
        ('C_A', '0', 'D_C'), ('C_A', '1', 'B_B'),
        ('D_B', '0', 'B_B'), ('D_B', '1', 'C_C'),
        ('D_C', '0', 'B_B'), ('D_C', '1', 'C_C'),
        ('C_C', '0', 'D_C'), ('C_C', '1', 'B_B'),
        ('E_C', '0', 'D_C'), ('E_C', '1', 'E_C')  
    ]
    for from_s, inp, to_s in transitions:
        moore.add_transition(from_s, inp, to_s)
    
    return moore


if __name__ == "__main__":
    print("="*60)
    print("CS13A - Lab 2: Mealy to Moore Machine Conversion")
    print("="*60)
    
    moore = build_moore_machine()
    test_inputs = ['00110', '11001', '1010110', '101111']
    
    print(f"\n{'Input':<15} {'Output':<15}")
    print("-"*60)
    for inp in test_inputs:
        out = moore.process_input(inp)
        print(f"{inp:<15} {out:<15}")
    print("="*60)
