class MealyState:
    def __init__(self, name):
        self.name = name
    
    def transition(self, input_char):
        raise NotImplementedError("Subclasses must implement transition method")
    
    def __str__(self):
        return self.name


class StateA(MealyState):
    """State A: Initial state"""
    def __init__(self):
        super().__init__("A")
    
    def transition(self, input_char):
        if input_char == '0':
            return StateB(), 'b'  
        else: 
            return StateA(), 'b'  


class StateB(MealyState):
    """State B: After seeing '0'"""
    def __init__(self):
        super().__init__("B")
    
    def transition(self, input_char):
        if input_char == '0':
            return StateB(), 'b'  
        else:  
            return StateC(), 'a' 


class StateC(MealyState):
    """State C: After detecting '01'"""
    def __init__(self):
        super().__init__("C")
    
    def transition(self, input_char):
        if input_char == '0':
            return StateB(), 'b' 
        else:  
            return StateA(), 'b' 


class MealyMachine:
    def __init__(self):
        self.current_state = StateA()
        self.transition_table = {
            'A': {'0': ('B', 'b'), '1': ('A', 'b')},
            'B': {'0': ('B', 'b'), '1': ('C', 'a')},
            'C': {'0': ('B', 'b'), '1': ('A', 'b')}
        }
    
    def show_transition_table(self):
        print("=" * 70)
        print("MEALY MACHINE TRANSITION TABLE (From Diagram)")
        print("=" * 70)
        print(f"{'State':<10}{'Input':<10}{'Next State':<15}{'Output':<10}{'Note'}")
        print("-" * 70)
        for state, transitions in self.transition_table.items():
            for inp, (next_state, out) in transitions.items():
                note = "← outputs 'a'" if out == 'a' else ""
                print(f"{state:<10}{inp:<10}{next_state:<15}{out:<10}{note}")
        print("=" * 70)
    
    def process_input(self, input_string):
        if not all(char in ['0', '1'] for char in input_string):
            raise ValueError("Input string must contain only '0's and '1's")
        
        output_sequence = []
        state_path = [str(self.current_state)]
        
        print(f"\nInitial state: {self.current_state}")
        print(f"Input string: {input_string}")
        print("-" * 70)
        print(f"{'Step':<6}{'Input':<8}{'Transition':<15}{'Output':<10}{'Note'}")
        print("-" * 70)
        
        for i, char in enumerate(input_string):
            previous_state = str(self.current_state)
            self.current_state, output = self.current_state.transition(char)
            output_sequence.append(output)
            state_path.append(str(self.current_state))
            
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
