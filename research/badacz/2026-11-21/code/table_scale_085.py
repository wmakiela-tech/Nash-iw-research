"""PREREG_085 positive injection control: write a copy of a hadron table with all five yield columns multiplied by a factor.
Usage: python3 -I table_scale_085.py <in_table> <factor> <out_table>   (header and mass column copied verbatim)"""
import sys

src, fac, dst = sys.argv[1], float(sys.argv[2]), sys.argv[3]
lines = open(src).read().splitlines()
out = [lines[0]]
for l in lines[1:]:
    f = l.split("\t")
    assert len(f) == 6
    out.append("\t".join([f[0]] + [repr(float(x) * fac) for x in f[1:]]))
open(dst, "x").write("\n".join(out) + "\n")
print("SCALED", len(out) - 1, "rows x", fac)
