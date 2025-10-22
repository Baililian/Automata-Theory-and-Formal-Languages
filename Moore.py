class MooreState:
    def __init__(self, name, output):
        self.name = name
        self.output = output
    
    def transition(self, input_char):
        raise NotImplementedError("Subclasses must implement transition method")
    
    def __str__(self):
        return self.name


class StateA(MooreState):
    """State A: outputs 'b'"""
    def __init__(self):
        super().__init__("A", 'b')
    
    def transition(self, input_char):
        if input_char == '0':
            return StateB()
        else:
            return StateA()


class StateB(MooreState):
    """State B: outputs 'b'"""
    def __init__(self):
        super().__init__("B", 'b')
    
    def transition(self, input_char):
        if input_char == '0':
            return StateB()
        else:
            return StateC()


class StateC(MooreState):
    """State C: outputs 'a' (detected '01')"""
    def __init__(self):
        super().__init__("C", 'a')
    
    def transition(self, input_char):
        # Both inputs go back to A
        return StateA()


class MooreMachine:
    def __init__(self):
        self.current_state = StateA()
        self.transition_table = {
            'A': {'0': 'B', '1': 'A', 'output': 'b'},
            'B': {'0': 'B', '1': 'C', 'output': 'b'},
            'C': {'0': 'A', '1': 'A', 'output': 'a'}
        }
    
    def show_transition_table(self):
        print("=" * 70)
        print("MOORE MACHINE TRANSITION TABLE")
        print("=" * 70)
        print(f"{'State':<10}{'Output':<10}{'Input':<10}{'Next State':<15}")
        print("-" * 70)
        for state, transitions in self.transition_table.items():
            output = transitions['output']
            for inp in ['0', '1']:
                next_state = transitions[inp]
                print(f"{state:<10}{output:<10}{inp:<10}{next_state:<15}")
        print("=" * 70)
    
    def process_input(self, input_string):
        if not all(char in ['0', '1'] for char in input_string):
            raise ValueError("Input string must contain only '0's and '1's")
        
        output_sequence = []
        state_path = [str(self.current_state)]
        
        print(f"\nInitial state: {self.current_state} (output: {self.current_state.output})")
        print(f"Input string: {input_string}")
        print("-" * 70)
        print(f"{'Step':<6}{'Input':<8}{'State':<12}{'Output':<10}{'Next State':<12}")
        print("-" * 70)
        
        for i, char in enumerate(input_string):
            current_state_name = str(self.current_state)
            current_output = self.current_state.output
            
            # Output from CURRENT state
            output_sequence.append(current_output)
            
            self.current_state = self.current_state.transition(char)
            state_path.append(str(self.current_state))
            
            print(f"{i+1:<6}{char:<8}{current_state_name:<12}{current_output:<10}{self.current_state}")
        
        # Final state output
        final_output = self.current_state.output
        output_sequence.append(final_output)
        print(f"{'FINAL':<6}{'-':<8}{self.current_state:<12}{final_output:<10}{'-'}")
        
        print("-" * 70)
        print(f"State path: {' → '.join(state_path)}")
        result = ''.join(output_sequence)
        print(f"Full Output: {result}")
        print(f"Only 'a's: {result.replace('b', '')}")
        return result
    
    def reset(self):
        self.current_state = StateA()
