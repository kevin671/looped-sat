def parse_dimacs(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    i = 0
    while lines[i].strip().split(" ")[0] == "c":
        i += 1
    header = lines[i].strip().split(" ")
    assert header[0] == "p"
    n_vars = int(header[2])
    iclauses = [
        [int(s) for s in line.strip().split(" ")[:-1]] for line in lines[i + 1 :]
    ]
    return n_vars, iclauses
