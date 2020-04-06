def is_happy(n: int) -> bool:
        if n == 1:
            return True
        
        m: int = n
        visited: dict = {}
            
        while True:
            if m == 1:
                break
            temp: int = 0
            while True:
                if m == 0:
                    break
                unit: int = m % 10
                temp: int = temp + (unit * unit)
                m: int = m // 10
            if visited.get(temp) == True:
                return False 
            m: int = temp
            visited[m]: bool = True
        return True
