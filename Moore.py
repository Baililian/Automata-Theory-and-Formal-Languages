class MooreState:
    def __init__(self, name, output):
        self.name = name
        self.output = output
    
    def transition(self, input_char):
        raise NotImplementedError("Subclasses must implement transition method")
    
    def __str__(self):
        return self.name


class StateA(MooreState):
    """State A: Initial state, outputs 'b'"""
    def __init__(self):
        super().__init__("A", 'b')
    
    def transition(self, input_char):
        if input_char == '0':
            return StateB()  
        else:
            return StateA() 


class StateB(MooreState):
    """State B: After seeing '0', outputs 'b'"""
    def __init__(self):
        super().__init__("B", 'b')
    
    def transition(self, input_char):
        if input_char == '0':
            return StateB() 
        else:
            return StateC()  


class StateC(MooreState):
    """State C: Just detected '01', outputs 'a'"""
    def __init__(self):
        super().__init__("C", 'a')
    
    def transition(self, input_char):
        if input_char == '0':
            return StateB() 
        else:
            return StateD()


class StateD(MooreState):
    """State D: After C saw '1', outputs 'b', ready to detect '0' again"""
    def __init__(self):
        super().__init__("D", 'b')
    
    def transition(self, input_char):
        if input_char == '0':
            return StateB()  
        else:
            return StateD()  


class MooreMachine:
    def __init__(self):
        self.current_state = StateA()
        self.transition_table = {
            'A': {'0': 'B', '1': 'A', 'output': 'b'},
            'B': {'0': 'B', '1': 'C', 'output': 'b'},
            'C': {'0': 'B', '1': 'D', 'output': 'a'},
            'D': {'0': 'B', '1': 'D', 'output': 'b'}
        }
    
    def show_transition_table(self):
        print("=" * 70)
        print("MOORE MACHINE TRANSITION TABLE (4 States)")
        print("Problem: Print 'a' whenever sequence 01 is encountered")
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
        print(f"{'Step':<6}{'Input':<8}{'Transition':<15}{'Output':<10}{'Note'}")
        print("-" * 70)
        
        for i, char in enumerate(input_string):
            previous_state = str(self.current_state)
            self.current_state = self.current_state.transition(char)
            state_path.append(str(self.current_state))
            
            # Moore output comes from the NEW state
            output = self.current_state.output
            output_sequence.append(output)
            
            transition = f"{previous_state}→{self.current_state}"
            note = "'01' detected!" if output == 'a' else ""
            print(f"{i+1:<6}{char:<8}{transition:<15}{output:<10}{note}")
        
        print("-" * 70)
        print(f"State path: {' → '.join(state_path)}")
        result = ''.join(output_sequence)
        print(f"Full Output: {result}")
        print(f"Only 'a's: {result.replace('b', '')}")
        return result
    
    def reset(self):
        self.current_state = StateA()
