import sys
import math
import random
import time

print(sys.builtin_module_names)
"""
Output:
('_ast', '_codecs', '_collections', '_functools', '_imp', '_io', '_locale', '_operator', '_signal', 
'_sre', '_stat', '_string', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', 'array', 'atexit', 
'binascii', 'builtins', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'math', 'mmap', 'nt', 
'operator', 'posix', 'pwd', 'sys', 'time', 'xxsubtype')


The most used modules are:
math -> Provides mathematical functions like sqrt, sin, cos, etc.
random -> Used to generate random numbers.
time -> Provides time-related functions.
os -> Provides a way of using operating system dependent functionality like reading or writing to the file system.
sys -> Provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.

"""

# sys Math module

# --- Operaciones matemáticas básicas ---
print("Square root of 16 is:", math.sqrt(16))   # Raíz cuadrada
print("Value of pi is:", math.pi)   # Valor de pi
print("Value of e is:", math.e)   # Valor de e
print("2 raised to the power of 3 is:", math.pow(2, 3)) # Potencia
print("Factorial of 5 is:", math.factorial(5))  # Factorial
print("Greatest common divisor of 48 and 18 is:", math.gcd(48, 18)) # Máximo común divisor
print("Least common multiple of 4 and 5 is:", math.lcm(4, 5))   # Mínimo común múltiplo
print("Absolute value of -7.5 is:", math.fabs(-7.5))    # Valor absoluto
print("Ceiling of 4.3 is:", math.ceil(4.3))   # Techo
print("Floor of 4.7 is:", math.floor(4.7))   # Piso
print("Remainder of 10 divided by 3 is:", math.fmod(10, 3))   # Resto
print("Exponential of 2 is:", math.exp(2))   # Exponencial

# --- Funciones trigonométricas ---
print("Sine of 90 degrees is:", math.sin(math.radians(90))) # Seno
print("Cosine of 0 degrees is:", math.cos(math.radians(0))) # Coseno
print("Radians of 180 degrees is:", math.radians(180)) # Radianes
print("Degrees of pi radians is:", math.degrees(math.pi)) # Grados
print("Arc sine of 1 is:", math.asin(1)) # Arco seno
print("Arc cosine of 0 is:", math.acos(0)) # Arco coseno
print("Arc tangent of 1 is:", math.atan(1)) # Arco tangente
print("Arc tangent of 1 with two arguments (y=1, x=1) is:", math.atan2(1, 1))   # Arco tangente con dos argumentos

# --- Funciones hiperbólicas ---
print("Sine hyperbolic of 1 is:", math.sinh(1)) # Seno hiperbólico
print("Cosine hyperbolic of 1 is:", math.cosh(1))   # Coseno hiperbólico
print("Tangent hyperbolic of 1 is:", math.tanh(1))  # Tangente hiperbólica

# --- Logaritmos ---
print("Logarithm of 1000 with base 10 is:", math.log10(1000))   # Logaritmo base 10
print("Logarithm of 32 with base 2 is:", math.log2(32))  # Logaritmo base 2
print("Logarithm of 100 with base e is:", math.log(100))    # Logaritmo natural
print("Logarithm of 27 with base 3 is:", math.log(27, 3))   # Logaritmo con base personalizada

# --- Funciones especiales ---
print("Gamma function of 5 is:", math.gamma(5)) # Función gamma
print("Log gamma function of 5 is:", math.lgamma(5))    # Logaritmo de la función gamma
print("Hypotenuse of a right triangle with sides 3 and 4 is:", math.hypot(3, 4))    # Hipotenusa

# --- Comprobaciones y valores especiales ---
print("Is 16 finite?:", math.isfinite(16))  # Comprobación de finitud
print("Is infinity finite?:", math.isfinite(math.inf))  # Comprobación de finitud
print("Is NaN a number?:", math.isnan(math.nan))    # Comprobación de NaN
print("Is 10 infinite?:", math.isinf(10))   # Comprobación de infinito
print("Is infinity infinite?:", math.isinf(math.inf))   # Comprobación de infinito
print("Is -infinity infinite?:", math.isinf(-math.inf))  # Comprobación de infinito
print("Is 10 a number?:", math.isclose(10, 10.0000001)) # Comprobación de cercanía
print("Is 10 close to 20?:", math.isclose(10, 20))  # Comprobación de cercanía
print("Is 0.1 + 0.2 close to 0.3?:", math.isclose(0.1 + 0.2, 0.3))  # Comprobación de cercanía
print("Is 0.1 + 0.2 exactly equal to 0.3?:", (0.1 + 0.2) == 0.3)    # Comprobación de igualdad exacta
print("Machine epsilon (smallest difference recognizable by the system):", math.ulp(1.0))   # Epsilon de máquina

# --- Constantes matemáticas ---
print("Value of infinity is:", math.inf)    # Infinito
print("Value of NaN (Not a Number) is:", math.nan)  # NaN
print("Value of tau (2 * pi) is:", math.tau)  # Tau
print("Value of the golden ratio is:", (1 + math.sqrt(5)) / 2)  # Razón áurea 

#-------------------------------------------------------------------------------------------------------------------
# Random module
print("Random float between 0 and 1:", random.random()) # Random float between 0 and 1
print("Random integer between 1 and 10:", random.randint(1, 10)) # Random integer between 1 and 10 (inclusive)
print("Random choice from a list:", random.choice(['apple', 'banana', 'cherry'])) # Random choice from a list
print("Random sample of 3 elements from a list:", random.sample(range(100), 3)) # Random sample of 3 elements from a range of 0 to 99

#-------------------------------------------------------------------------------------------------------------------
#time module
print("Current time in seconds since the epoch:", time.time()) # tiempo en segundos desde epoch (epoch está definido como 00:00:00 UTC del 1 de enero de 1970)
print("Current local time:", time.localtime()) # tiempo local
print("Current UTC time:", time.gmtime()) # tiempo en UTC

# ---- sleep function ----
print("Sleeping for 2 seconds...")
time.sleep(2)
print("Awoke after 2 seconds!")

# ----------- Conversiones de tiempo -----------
# strftime: formatea un objeto struct_time (como el devuelto por localtime() o gmtime()) en una cadena legible.
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("Formatted local time:", formatted_time)

# strptime: analiza una cadena que representa una fecha y hora y la convierte en un objeto struct_time.
time_string = "2023-10-05 14:30:00"
parsed_time = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
print("Parsed time:", parsed_time)

# ctime: convierte un tiempo en segundos desde epoch a una cadena legible.
print("Current time (ctime):", time.ctime(time.time()))

# asctime: convierte un objeto struct_time a una cadena legible.
print("Current local time (asctime):", time.asctime(time.localtime()))

# perf_counter: devuelve el valor del contador de rendimiento más preciso disponible en el sistema.
start = time.perf_counter()

# loops with sleep to simulate a time-consuming task
for i in range(5):
    time.sleep(0.5)  # sleep for 0.5 seconds
end = time.perf_counter()
print(f"Elapsed time for the loop: {end - start} seconds")

while True:
    with open("stop.txt", "r") as file:
        content = file.read()
        time.sleep(10)  # Check every 10 seconds
    # Si modificamos el contenido dentro de stop.txt en los 10 segundos, se reflejará aquí
    # Si modificamos el contenido de stop.txt a "STOP", el bucle se detendrá
    if content.strip() == "STOP":
        print("Stopping the loop as 'STOP' was found in stop.txt")
        break