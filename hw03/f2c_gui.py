import tkinter as tk
from tkinter import messagebox

def f2c(temp_f: float) -> float:
    return (temp_f - 32) * 5 / 9

def convert():
    try:
        global entry, result_label
        
        temp_f = float(entry.get())
        temp_c = f2c(temp_f)
        
        result_label.config(text=f"{temp_f:.1f}F => {temp_c:.1f}C")
    except ValueError:
        messagebox.showerror("입력 오류", "유효한 숫자를 입력하세요.")

def main():
    global entry, result_label  #entry 와 result_label을 global로 선언하여서 다른 함수에도 가능하게 하였습니다.
    
    win = tk.Tk()
    win.title("화씨에서 섭씨로 변환기")

    tk.Label(win, text="화씨 온도를 입력하세요:").pack(pady=10)
    entry = tk.Entry(win)
    entry.pack(pady=5)

    convert_button = tk.Button(win, text="변환", command=convert)
    convert_button.pack(pady=10)

    result_label = tk.Label(win, text="")
    result_label.pack(pady=10)

    win.mainloop()

if __name__ == "__main__":
    main()