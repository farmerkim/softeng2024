import tkinter as tk
from tkinter import messagebox

def is_even(n: int):
    return n % 2 == 0

def check_even_odd():
    try:
        n = int(entry.get())
        
        if is_even(n):
            result_label.config(text=f"{n}은 짝수입니다.")
        else:
            result_label.config(text=f"{n}은 홀수입니다.")
    except ValueError:
        messagebox.showerror("입력 오류", "유효한 숫자를 입력하세요.")


def main():
    win = tk.Tk()
    win.title("짝수/홀수 판별기")

    tk.Label(win, text="숫자를 입력하세요:").pack(pady=10)
    global entry
    entry = tk.Entry(win)
    entry.pack(pady=5)

    check_button = tk.Button(win, text="확인", command=check_even_odd)
    check_button.pack(pady=10)

    global result_label
    result_label = tk.Label(win, text="")
    result_label.pack(pady=10)

    win.mainloop()

if __name__ == "__main__":
    main()