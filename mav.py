import sys
import time
from readfile import readata as rd
from movavg import dynamic_moving_average as ma
from savefile import savedata

def main(gn, window):
    filename, header, bin_count, intensity = rd(gn)
    print(f"\r{' ' * 50}", end='')
    print(f"\rNúmero de dados: {len(bin_count)}", end='', flush=True)

    for ws in window:
        bincount, movavg = ma(intensity, ws)
        savedata(filename, header, bincount, movavg, ws)
        if len(bin_count) == len(movavg):
            print(f"\r{' ' * 50}", end='')
            print(f"\rfim do cálculo para {ws} com {len(movavg)} dados criados!", end='', flush=True)
            time.sleep(0.5)
        else:
            print(f"\r{' ' * 50}", end='')
            print(f"\rATENÇÃO! {ws} não possui mesmo número de dados que {gn}.", end='', flush=True)
            time.sleep(0.5)
    print(f"\r{' ' * 50}", end='')
    print(f"\rfinished!", end='', flush=True)
        
# window = int(input("window size: "))
try:
    window = list(int(sys.argv[2]))
except:
    window = list(range(10, 160, 10))
main(sys.argv[1], window)