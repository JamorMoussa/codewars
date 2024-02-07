###############################################################################
# problem: sum-of-array-singles                                             #
# link: https://www.codewars.com/kata/59f11118a5e129e591000134/train/python   #
###############################################################################


# my solution : 

def repeats(arr):
    occ = {key: 0 for key in set(arr)}
    
    for key in arr:
        occ[key] += 1

    return sum(filter(lambda key: occ[key] == 1, occ.keys()))

# very clever one :)     
repeats=lambda a: 2*sum(set(a))-sum(a)


if __name__ == "__main__":

    print(repeats([4,5,7,5,4,8])) # should give 15