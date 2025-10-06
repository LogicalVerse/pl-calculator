import json
import math

def json_calculator(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            data = json.loads(line)

            operation = data.get("operation")

            if operation == "add":
                result = sum(data["numbers"])
            elif operation == "mul":
                result = 1
                for num in data["numbers"]:
                    result *= num
            elif operation == "sqrt":
                result = math.sqrt(data["number"])
            else:
                result = "Invalid operation"

            print(json.dumps({"result": result}))

if __name__ == "__main__":
    json_calculator("examples.jsonl")
