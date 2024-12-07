import math


def minEatingSpeed(piles, H):
    
    def helper(piles, mid):
        count = 0
        for pile in piles:
            div = pile // mid
            rem = pile % mid
            if rem != 0:
                count += 1
            count += div
        return count
    
    left = 1
    right = max(piles)

    while left < right:
        mid = (left + right) // 2
        if helper(piles, mid) <= H:
            right = mid
        else:
            left = mid + 1

    return right

def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    h = int(input())
    ans = minEatingSpeed(arr, h)
    print(ans)

if __name__ == "__main__":
    main()
