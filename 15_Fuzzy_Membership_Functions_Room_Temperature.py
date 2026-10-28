import numpy as np
import matplotlib.pyplot as plt

def triangular(x, a, b, c):
    # Triangular membership function
    return np.maximum(0, np.minimum((x-a)/(b-a+1e-12), (c-x)/(c-b+1e-12)))

def trapezoidal(x, a, b, c, d):
    # Trapezoidal membership function
    left = np.where(x <= b, 1.0, np.where(x < c, 1.0, (d-x)/(d-c+1e-12)))
    left_ramp = np.where(x <= a, 0.0, np.where(x < b, (x-a)/(b-a+1e-12), 1.0))
    return np.maximum(0, np.minimum(left_ramp, left))

def gaussian(x, mean, sigma):
    return np.exp(-0.5 * ((x-mean)/sigma)**2)

value = float(input("Enter temperature in Celsius (0-40): "))
if not 0 <= value <= 40:
    raise ValueError("Value is outside the allowed range 0 to 40.")

x = np.linspace(0, 40, 501)
# For the low-end trapezoid, membership is 1 through the flat region, then falls.
def low_trapezoid(x, plateau_end, fall_end):
    return np.where(x <= plateau_end, 1.0,
                    np.where(x < fall_end, (fall_end-x)/(fall_end-plateau_end), 0.0))

mu1 = low_trapezoid(x, 12, 20)
mu2 = triangular(x, 16, 22, 28)
mu3 = gaussian(x, 32, 4)

m1 = float(low_trapezoid(np.array([value]), 12, 20)[0])
m2 = float(triangular(np.array([value]), 16, 22, 28)[0])
m3 = float(gaussian(np.array([value]), 32, 4)[0])
print("Input value:", value)
print("Cold membership:", round(m1, 3))
print("Comfortable membership:", round(m2, 3))
print("Hot membership:", round(m3, 3))

plt.plot(x, mu1, label="Cold (trapezoidal)")
plt.plot(x, mu2, label="Comfortable (triangular)")
plt.plot(x, mu3, label="Hot (Gaussian)")
plt.title("Cold / Comfortable / Hot Membership Functions")
plt.xlabel("Temperature (°C)")
plt.ylabel("Membership degree")
plt.ylim(0, 1.05)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("room_temperature_membership.png")
print("Plot saved as room_temperature_membership.png")
plt.show()

# SAMPLE INPUT:
# Enter temperature in Celsius (0-40): 22
# SAMPLE OUTPUT:
# The three membership degrees are printed above; the plot is saved to room_temperature_membership.png.
