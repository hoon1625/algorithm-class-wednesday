# factorial_app.py
import time

def factorial_iter(n: int) -> int:
    if n < 0:
        raise ValueError("음수 입력 불가")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_rec(n: int) -> int:
    if n < 0:
        raise ValueError("음수 입력 불가")
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n - 1)

def run_with_time(func, n: int):
    start = time.perf_counter()
    result = func(n)
    elapsed = time.perf_counter() - start
    return result, elapsed

TEST_CASES = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]

def run_menu():
    while True:
        print("\n================ Factorial Tester ================")
        print("1) 반복법으로 n! 계산")
        print("2) 재귀로 n! 계산")
        print("3) 두 방식 모두 계산 후 결과/시간 비교")
        print("4) 준비된 테스트 데이터 일괄 실행")
        print("q) 종료")
        print("--------------------------------------------------")
        choice = input("선택: ").strip()

        if choice == "q":
            print("프로그램을 종료합니다.")
            break

        elif choice in ["1", "2", "3"]:
            n_str = input("정수 n 입력: ").strip()
            if not n_str.isdigit():
                print("[오류] 정수를 입력해야 합니다.")
                continue
            n = int(n_str)

            try:
                if choice == "1":
                    res, t = run_with_time(factorial_iter, n)
                    print(f"n={n} | iter={t:.6f}s\n{res}")

                elif choice == "2":
                    res, t = run_with_time(factorial_rec, n)
                    print(f"n={n} | rec={t:.6f}s\n{res}")

                elif choice == "3":
                    res1, t1 = run_with_time(factorial_iter, n)
                    res2, t2 = run_with_time(factorial_rec, n)
                    same = res1 == res2
                    print(f"n={n} | same={same} | iter={t1:.6f}s, rec={t2:.6f}s")
                    print(res1 if same else f"iter={res1}, rec={res2}")

            except ValueError as e:
                print("[오류]", e)
            except RecursionError:
                print("[오류] 재귀 호출 한도를 초과했습니다.")

        elif choice == "4":
            print("\n[테스트 데이터 실행]")
            for n in TEST_CASES:
                try:
                    res1, t1 = run_with_time(factorial_iter, n)
                    res2, t2 = run_with_time(factorial_rec, n)
                    same = res1 == res2
                    print(f"\nn= {n} | same={same} | iter={t1:.6f}s, rec={t2:.6f}s")
                    print(f"{n}! = {res1}")
                except RecursionError:
                    print(f"\nn= {n} | 재귀 호출 한도 초과!")
        else:
            print("[오류] 잘못된 메뉴 선택")

if __name__ == "__main__":
    run_menu()
