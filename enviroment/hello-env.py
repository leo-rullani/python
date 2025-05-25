from dotenv import load_dotenv
import os
from pathlib import Path

# eine Ebene nach oben wechseln
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

print("Hello", os.environ.get("USER_NAME"))