from pathlib import Path
import yaml

def load_config(path='config.yaml'):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Missing config file: {path}")
    return yaml.safe_load(p.read_text())

def save_text(path, text):
    Path(path).write_text(text, encoding='utf-8')
