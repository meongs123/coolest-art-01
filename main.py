# The art ships in the repo as art.jpg (round 2: a fisherman reeling in the sun,
# ukiyo-e style); the program only copies it to the output.
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "art.jpg"), os.path.join(OUT, "entry.png"))
