import subprocess
import os
import glob


for i in range(5):
    result = subprocess.run(['perf', 'stat', 'python', 'testCloud.py'])
    
    files = glob.glob('images/*')
    for f in files:
        os.remove(f)