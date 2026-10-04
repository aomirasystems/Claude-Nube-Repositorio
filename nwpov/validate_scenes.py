import sys, re, importlib.util, os
S_DIR = os.path.dirname(os.path.abspath(__file__))  # usa nwpov_common real si esta en el PYTHONPATH; si no, copia nwpov_common_stub.py como nwpov_common.py
sys.path.insert(0, S_DIR)
KINDS = {"MACRO","HAND","STAND","SIT","CLOSE","WIDE"}
SETS = {"KDAY","KNIGHT","OFFICE","LIVING","STREET","DEALER","CLEAN","DESK"}
path = sys.argv[1]
spec = importlib.util.spec_from_file_location("m", path)
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
S = m.S
words = 0; problems = []
run = 1
for i,(k,s,v,n) in enumerate(S,1):
    if k not in KINDS: problems.append((i,"kind",k))
    if s not in SETS: problems.append((i,"setting",s))
    w = len(n.split()); words += w
    if re.search(r"\d|[$%]|—|–|\.\.\.|…", n): problems.append((i,"narr symbol/digit",n))
    if re.search(r"[A-Za-z]'[a-z]|’", n): problems.append((i,"apostrophe",n))
    if re.search(r"\d", re.sub(r"no digits","",v)): problems.append((i,"digit in visual",v))
    if w < 10 or w > 26: problems.append((i,"words=%d"%w,n))
    if i>1 and S[i-2][0]==k: run += 1
    else: run = 1
    if run > 2: problems.append((i,"3 same kind in a row",k))
print("scenes",len(S),"words",words, "avg %.1f"%(words/len(S)))
for p in problems: print(p)
