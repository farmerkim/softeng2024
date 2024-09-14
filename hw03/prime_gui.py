import tkinter as tk
from tkinter import messagebox

def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def yes_no_prime():
    try:
        n = int(entry.get())
        
        if is_prime(n):
            result_label.config(text=f"{n}은 소수입니다.")
        else:
            result_label.config(text=f"{n}은 소수가 아닙니다.")
    except ValueError:
        
        messagebox.showerror("입력 오류", "유효한 숫자를 입력하세요.")

def main():
    win = tk.Tk()
    win.title("소수 판별기")

    tk.Label(win, text="숫자를 입력하세요:").pack(pady=10)
    global entry
    entry = tk.Entry(win)
    entry.pack(pady=5)

    check_button = tk.Button(win, text="확인", command=yes_no_prime)
    check_button.pack(pady=10)

    global result_label
    result_label = tk.Label(win, text="")
    result_label.pack(pady=10)

    win.mainloop()

if __name__ == "__main__":
    main()