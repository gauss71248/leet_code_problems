class Solution:
    def isValid(self, s: str) -> bool:
        state = {
            "(": 0,
            "[": 0,
            "{": 0
        }
        transition_values = {
            "(": 1,
            ")": -1,
            "[": 1,
            "]": -1,
            "{": 1,
            "}": -1
        }
        transition_map = {
            "(": "(",
            ")": "(",
            "[": "[",
            "]": "[",
            "{": "{",
            "}": "{"
        }
        def is_valid_state() -> bool:
            result = True
            for val in state.values():
                result = result & (val>=0)
            return result
        
        def process_one(lit: str) -> Dict[str, int]:
            to_check = transition_map[lit]
            value_to_add = transition_values[lit]
            cur_state_value = state[to_check]
            new_state_value = cur_state_value + value_to_add
            state[to_check] = new_state_value
        
        for x in s:
            process_one(x)
            if not is_valid_state():
                return False
            
        return True
