def f2c(temp_f: float) -> float:
    return (temp_f -32) * 5 /9

def main():
    temp_f = (float(input(f"화씨 온도를 입력하세요 => ")))
    #temp_c = (temp_f -32) * 5 /9
    temp_c = f2c(temp_f)

    print(f"{temp_f}F => {temp_c:.1f}C")

if __name__ == "__main__":
    main()