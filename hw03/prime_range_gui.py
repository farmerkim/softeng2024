import tkinter as tk

def is_prime(n: int):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def find_primes():
    primes = [i for i in range(2, 51) if is_prime(i)]
    result_label.config(text=f"2부터 50까지의 소수: {', '.join(map(str ,primes))}")


def main():
  
    win = tk.Tk()
    win.title("소수 목록")

    tk.Label(win, text="2부터 50까지의 소수를 찾습니다").pack(pady=10)

    find_button = tk.Button(win, text="소수 찾기", command=find_primes)
    find_button.pack(pady=10)

    global result_label
    result_label = tk.Label(win, text="")
    result_label.pack(pady=10)

    win.mainloop()


if __name__ == "__main__":
    main()