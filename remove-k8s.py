import os
import os.path

from glob import glob

files = glob("argo/models/*.py")

# remove kubernetes models
for filepath in files:
    modelname = os.path.basename(filepath)
    if modelname[:10] == "io_k8s_api":
        print("removing %s" % filepath)
        os.remove(filepath)

_frag = "from argo.models.io_k8s_api_core_v1"

with open("argo/models/__init__.py", "r") as stream:
    contents = []
    while True:
        chunk = stream.readline()
        if not chunk:
            break
        if chunk[:len(_frag)] != _frag:
            contents.append(chunk)
        else:
            print("removing line: %s" % chunk)

with open("argo/models/__init__.py", "w") as stream:
    stream.write("".join(contents))

