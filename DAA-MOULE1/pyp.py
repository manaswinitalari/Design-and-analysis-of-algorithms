def read_and_print_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            s = f.read()
        print(s)
    except FileNotFoundError:
        print("Error: file not found")
    except PermissionError:
        print("Error: permission denied")
    except Exception as e:
        print("Unexpected error:", e)
