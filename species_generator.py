import torch
from transformers import pipeline
from utils import load_config

def generate_species(seed_prompt):
    cfg = load_config()
    model_name = cfg['generation']['model_name']
    device = 0 if torch.cuda.is_available() else -1
    pipe = pipeline('text2text-generation', model=model_name, device=device)
    prompt = f"Invent 4-6 major species for a world described as:\n{seed_prompt}\n\nProvide short bios and ecological roles."
    out = pipe(prompt, max_new_tokens=300, do_sample=True, temperature=cfg['generation']['temperature'])
    return out[0].get('generated_text') if isinstance(out, list) else str(out)
