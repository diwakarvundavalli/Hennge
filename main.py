import sys

def main():
    tokens = sys.stdin.read().strip().split()
    
    def process_cases(idx, remaining, output):
        if remaining == 0:
            sys.stdout.write("\n".join(output))
            return
        
        if idx >= len(tokens):
            sys.stdout.write("\n".join(output + ["-1"] * remaining))
            return
        
        try:
            x = int(tokens[idx])
        except:
            process_cases(idx + 1, remaining - 1, output + ["-1"])
            return
        
        values_start = idx + 1
        values_end = values_start + x
        
        if values_end > len(tokens):
            process_cases(values_end, remaining - 1, output + ["-1"])
            return
        
        values = tokens[values_start:values_end]
        
        if len(values) != x:
            process_cases(values_end, remaining - 1, output + ["-1"])
            return
        
        try:
            nums = list(map(int, values))
        except:
            process_cases(values_end, remaining - 1, output + ["-1"])
            return
        
        result = sum(map(lambda n: n ** 4 if n <= 0 else 0, nums))
        process_cases(values_end, remaining - 1, output + [str(result)])
    
    if not tokens:
        return
    
    try:
        n = int(tokens[0])
    except:
        return
    
    process_cases(1, n, [])

if __name__ == "__main__":
    main()
