def write_to_file(name:str, content:str):
    file = open(name, "a")
    file.write(content)
    file.close()
