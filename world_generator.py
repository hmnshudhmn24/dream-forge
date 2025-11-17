import torch
from transformers import pipeline
from prompt_builder import build_world_prompt
from utils import load_config, save_text

def get_pipeline(model_name):
    device = 0 if torch.cuda.is_available() else -1
    # Use text2text for Flan-T5 family
    return pipeline('text2text-generation', model=model_name, device=device, truncation=True)

def generate_world(prompt_seed, out_path=None):
    cfg = load_config()
    model_name = cfg['generation']['model_name']
    max_new_tokens = cfg['generation'].get('max_new_tokens', 512)
    num_beams = cfg['generation'].get('num_beams', 4)
    temperature = cfg['generation'].get('temperature', 0.9)
    top_p = cfg['generation'].get('top_p', 0.95)

    prompt = build_world_prompt(prompt_seed, extra_notes="")
    pipe = get_pipeline(model_name)
    result = pipe(prompt, max_new_tokens=max_new_tokens, num_beams=num_beams, do_sample=True, temperature=temperature, top_p=top_p)
    text = result[0].get('generated_text') if isinstance(result, list) else str(result)
    if out_path:
        save_text(out_path, text)
    return text

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--prompt', required=True)
    p.add_argument('--out', default='dreamforge_output.md')
    args = p.parse_args()
    out = generate_world(args.prompt, out_path=args.out)
    print('Saved to', args.out)
