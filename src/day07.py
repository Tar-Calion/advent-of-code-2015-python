from enum import Enum


circuit = {}
results = {}

class SourceType(Enum):
    WIRE = 1
    VALUE = 2
    AND_GATE = 3
    OR_GATE = 4
    LSHIFT_GATE = 5
    RSHIFT_GATE = 6
    NOT_GATE = 7

def get_source_type(source):
    if source.isdigit():
        return SourceType.VALUE
    elif source.isalpha():
        return SourceType.WIRE
    
    if "AND" in source:
        return SourceType.AND_GATE
    elif "OR" in source:
        return SourceType.OR_GATE
    elif "LSHIFT" in source:
        return SourceType.LSHIFT_GATE
    elif "RSHIFT" in source:
        return SourceType.RSHIFT_GATE
    elif "NOT" in source:
        return SourceType.NOT_GATE
    else:
        raise ValueError(f"Unknown source type: {source}")

def get_signal(wire):
    if wire in results:
        return results[wire]
    
    if wire.isdigit():
        result = int(wire) & 0xFFFF
        return result

    
    print(f"Getting signal for {wire}")
    source = circuit[wire]
    print(f"Source: {source}")
    source_type = get_source_type(source)
    print(f"Source type: {source_type}")

    result = None

    if source_type == SourceType.VALUE:
        result = int(source) & 0xFFFF
    elif source_type == SourceType.WIRE:
        result = get_signal(source)
    elif source_type == SourceType.AND_GATE:
        left, right = source.split(" AND ")
        result = (get_signal(left) & get_signal(right)) & 0xFFFF
    elif source_type == SourceType.OR_GATE:
        left, right = source.split(" OR ")
        result = (get_signal(left) | get_signal(right)) & 0xFFFF
    elif source_type == SourceType.LSHIFT_GATE:
        input, shift_amount = source.split(" LSHIFT ")
        result = (get_signal(input) << int(shift_amount)) & 0xFFFF
    elif source_type == SourceType.RSHIFT_GATE:
        input, shift_amount = source.split(" RSHIFT ")
        result = (get_signal(input) >> int(shift_amount)) & 0xFFFF
    elif source_type == SourceType.NOT_GATE:
        input = source[4:]
        result = (~get_signal(input)) & 0xFFFF
    else:
        raise ValueError(f"Unknown source type: {source}")
        
    results[wire] = result
    return result


def import_circuit(file_path):
    with open(file_path, "r") as file:
        for line in file:
            source, target = line.strip().split(" -> ")
            circuit[target] = source

def first_part():
    import_circuit("data/day07/input.txt")
    print(get_signal("a"))

def second_part():
    import_circuit("data/day07/input.txt")
    wire_a = get_signal("a")
    print(f"Wire a: {wire_a}")
    results.clear()
    results["b"] = wire_a
    print(get_signal("a"))

second_part()

