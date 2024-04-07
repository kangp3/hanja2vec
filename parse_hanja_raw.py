#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import json

def is_hanmun(c):
    try:
        return 0x4E00 <= ord(c) <= 0x9FFF
    except:
        return False

hanmun_to_hangeul = {}
with open('hanja_raw.txt') as f:
    for line in f:
        if len(line) < 3:
            continue
        toks = line.strip().split(chr(183))
        for hanmun_hangeul in toks:
            (hanmun, hangeul_raw) = hanmun_hangeul.strip().split(maxsplit=1)
            definition, hangeul = hangeul_raw[1:-1].rsplit(maxsplit=1)
            hanmun_to_hangeul[hanmun] = {"hangeul": hangeul, "definition": definition}

print(hanmun_to_hangeul)
with open('hanja.json', 'w') as f:
    json.dump(hanmun_to_hangeul, f, indent=2)
