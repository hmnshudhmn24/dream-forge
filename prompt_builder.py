from utils import load_config
import textwrap

def build_world_prompt(user_prompt: str, extra_notes: str = "") -> str:
    cfg = load_config()
    template = cfg.get('templates', {}).get('world_overview', '').strip()
    parts = ["User seed:", user_prompt.strip()]
    if extra_notes:
        parts += ["Extra notes:", extra_notes.strip()]
    parts += ["Instructions:", template]
    return "\n\n".join(parts)
