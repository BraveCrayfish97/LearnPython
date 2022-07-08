lst = []

s = input()
n = int(input())

lst_s = list(s)

def merge_the_tools(string, k):
    parts = len(string)/k
    for i in range(1, int(parts) + 1):
        st = set()
        for index in range(k*(i-1), k*i):
            
            st.add(lst_s[index])
            print(lst_s[index])
        print(st)
        lst.append(st)
        print("_____")
    print(lst)

merge_the_tools(s, n)