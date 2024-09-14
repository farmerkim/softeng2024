import tkinter as tk
from tkinter import messagebox

def factorial(n: int):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def calculate_factorial():
    try:
        number = int(entry.get())
        result = factorial(number)
        result_label.config(text=f"{number}의 팩토리얼 값은 {result}")
    except ValueError:
        messagebox.showerror("입력 오류", f"유효한 양의 정수를 입력하세요.")

def main():
    global entry, result_label

    win = tk.Tk()
    win.title("팩토리얼 계산기")

    tk.Label(win, text="팩토리얼을 구할 숫자를 입력하세요:").pack(pady=10)
    entry = tk.Entry(win)
    entry.pack(pady=5)

    calculate_button = tk.Button(win, text="계산하기", command=calculate_factorial)
    calculate_button.pack(pady=10)

    result_label = tk.Label(win, text="")
    result_label.pack(pady=10)

    win.mainloop()

if __name__ == "__main__":
    main()