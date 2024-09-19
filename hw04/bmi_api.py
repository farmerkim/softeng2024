from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello():
    html_str = '''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BMI 계산기</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 50px;
        }
        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            margin: 0 auto;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        input, button {
            padding: 10px;
            margin: 10px 0;
            width: 100%;
            box-sizing: border-box;
        }
        p.result {
            text-align: center;
            font-size: 1.2em;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>BMI 계산기</h1>
        <label for="height">키 (cm):</label>
        <input type="number" id="height" placeholder="키를 입력하세요 (cm)">

        <label for="weight">몸무게 (kg):</label>
        <input type="number" id="weight" placeholder="몸무게를 입력하세요 (kg)">

        <button onclick="calculateBMI()">BMI 계산하기</button>

        <p class="result">당신의 BMI는: <span id="bmi-result">0</span></p>
        <p class="result" id="bmi-message"></p>
    </div>

    <script>
        function calculateBMI() {
            var height = document.getElementById("height").value / 100; // cm를 m로 변환
            var weight = document.getElementById("weight").value;

            if (height > 0 && weight > 0) {
                var bmi = (weight / (height * height)).toFixed(2);
            
                document.getElementById("bmi-result").textContent = bmi;

                var message = "";
                if (bmi < 18.5) {
                    message = "저체중입니다.";
                } else if (bmi >= 18.5 && bmi < 24.9) {
                    message = "정상 체중입니다.";
                } else if (bmi >= 25 && bmi < 29.9) {
                    message = "과체중입니다.";
                } else {
                    message = "비만입니다.";
                }

                document.getElementById("bmi-message").textContent = message;
            } else {
                document.getElementById("bmi-message").textContent = "유효한 값을 입력하세요.";
            }
        }
    </script>
</body>
</html>
    '''
    return html_str

if __name__ == "__main__":
    app.run(debug=True)