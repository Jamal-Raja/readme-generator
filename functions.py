# ============ ALL FUNCTIONS ============
def multiline_input(prompt: str) -> str:
    print(f"{prompt} (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line.strip())
    output = "\n".join(lines)    

    return output