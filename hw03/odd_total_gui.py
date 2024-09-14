import tkinter as tk

def is_even(n: int):
    return n % 2 == 0

def even_sum():
    total = sum(i for i in range(1, 101) if is_even(i))
    result_label.config(text=f"1부터 100까지 짝수의 합은 {total}입니다.")

def main():
    global result_label

    win = tk.Tk()
    win.title("짝수의 합 계산기")

    tk.Label(win, text="1부터 100까지 짝수의 합을 계산합니다").pack(pady=10)

    calculate_button = tk.Button(win, text="계산하기", command=even_sum)
    calculate_button.pack(pady=10)

    result_label = tk.Label(win, text="")
    result_label.pack(pady=10)

    win.mainloop()

if __name__ == "__main__":
    main()