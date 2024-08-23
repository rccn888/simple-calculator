from pystyle import Colors, Colorate

text1 = """  _|_|_|    _|_|_|            _|                      _|              _|                         
_|        _|          _|_|_|  _|    _|_|_|  _|    _|  _|    _|_|_|  _|_|_|_|    _|_|    _|  _|_| 
  _|_|    _|        _|    _|  _|  _|        _|    _|  _|  _|    _|    _|      _|    _|  _|_|     
      _|  _|        _|    _|  _|  _|        _|    _|  _|  _|    _|    _|      _|    _|  _|       
_|_|_|      _|_|_|    _|_|_|  _|    _|_|_|    _|_|_|  _|    _|_|_|      _|_|    _|_|    _|       """
print(Colorate.Horizontal(Colors.blue_to_white, text1, 1))
print(Colorate.Horizontal(Colors.blue_to_white, "\n[?] Author: raccoon888\n", 1))
num1 = input(Colorate.Horizontal(Colors.blue_to_white, "[+] Введите первое число: "))
num1 = float(num1)
num2 = input(Colorate.Horizontal(Colors.blue_to_white, "[+] Введите второе число: "))
num2 = float(num2)
maths = input(Colorate.Horizontal(Colors.blue_to_white, "[+] Выберите действие: (+, -, /, *) "))
if maths == "+":
    result = num1 + num2
    print(Colorate.Horizontal(Colors.blue_to_white, "[!] Ответ: "), result)
elif maths == "-":
    result = num1 - num2
    print(Colorate.Horizontal(Colors.blue_to_white, "[!] Ответ: "), result)
elif maths == "*":
    result = num1 * num2
    print(Colorate.Horizontal(Colors.blue_to_white, "[!] Ответ: "), result)
elif maths == "/":
    result = num1 / num2
    print(Colorate.Horizontal(Colors.blue_to_white, "[!] Ответ: "), result)