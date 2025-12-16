import importlib.util
import os

def load_and_run(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return

    spec = importlib.util.spec_from_file_location("eat_pixel", file_path)
    external = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(external)

if __name__ == "__main__":
    load_and_run("eat_pixel.pyw")
