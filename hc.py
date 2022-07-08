if __name__ == '__main__':
    n_s = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        n_s[name] = score
        #nested list
#print(n_s.keys())
#print(n_s.values())
keys = list(n_s.keys())
vals = list(n_s.values())
sec_low = sorted(vals)[1]
#print(sec_low)
for key in keys:
    if n_s[key] == sec_low:
        print(key)
    else:
        pass
#print(keys[vals.index(sec_low)])