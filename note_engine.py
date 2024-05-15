import os
from llama_index.core.tools import FunctionTool


def save_notes(note):
    note_file = os.path.join("data", "notes.txt")
    
    os.makedirs(note_file, exist_ok=True)
    with open(note_file, "a") as f:
        f.write(note + "\n")
        
    return f"note saved in {note_file}"

note_engine = FunctionTool.from_defaults(save_notes,
    name="save_note",
    description="this tool can save a text based note to a file to the user",
)
