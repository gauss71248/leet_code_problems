class Solution:
    def romanToInt(self, s: str) -> int:
        def convert_literals(c: str) -> int:
            match c:
                case "IV":
                    return 4
                case "IX": 
                    return 9
                case "XL":
                    return 40
                case "XC":
                    return 90
                case "CD":
                    return 400
                case "CM":
                    return 900
                case "I":
                    return 1
                case "X":
                    return 10
                case "V":
                    return 5
                case "L":
                    return 50
                case "C":
                    return 100
                case "D":
                    return 500
                case "M":
                    return 1000
                case _:
                    return 0
        def check_special_case(to_check:str)-> bool:
            if len(to_check)<=1:
                return False
            lit = to_check[:2]
            if lit in ["IV","IX","XL","XC","CD","CM"]:
                return True
            else:
                return False
            
        def process_literals(work_str: str):
            if len(work_str)==0:
                return 0
            if check_special_case(work_str):
                lit = work_str[:2]
                new_work_str = work_str[2:]
            else:
                lit = work_str[:1]
                new_work_str = work_str[1:]
            return convert_literals(lit) + process_literals(new_work_str)
        return process_literals(s)
