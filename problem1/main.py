def compare(a, b):
    pattern=''
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            k=1
            while (i+k <= len(a) and j+k <= len(b) and a[i:i+k]==b[j:j+k]):
                if len(pattern) <= len(a[i:i+k]):
                   pattern = a[i:i+k]
                k=k+1
    return pattern

if __name__ == '__main__':
    print(compare("AKA", "AKASHI")) # AKA
    print(compare("KANGOORO", "KANG")) # KANG
    print(compare("KI", "KIJANG")) # KI
    print(compare("KUPU-KUPU", "KUPU")) # KUPU
    print(compare("ILALANG", "ILA")) # ILA