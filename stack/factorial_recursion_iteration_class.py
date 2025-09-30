def factorial_iter(n):
    # 반복문 기반 n!
    result = 1
    for k in range(2, n+1):
        result *= k
    return result

def factorial_rec(n):
    # 재귀적으로 문제 해결 n! -> 재귀함수 정의

    # 1. base case (재귀호출 종료 조건)
    if n == 1:
        return 1
    
    # 2. 재귀 분할 호출
    return n * factorial_rec(n-1)


if __name__ == "__main__":
    n = int (input("\n정수를 입력하세요: ").strip())
    print(f"반복문 기반: {factorial_iter(n)}")
    try:
        print(f"재귀 기반: {factorial_rec(n)}")
    except RecursionError:
        print("입력값이 너무 커서 재귀 계산은 불가능합니다.")

    # main()
