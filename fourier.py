import math


PI = 3.141592653589793

# example functions
def example1(t):
  return polar(35*math.sin(16*PI*t)+75, 2 * PI * t)

def example2(t):
  return polar(35 if math.sin(16*PI*t)>0.5 else 70, 2 * PI * t)



def polar(r, phi):
  return r * complex(math.cos(phi), math.sin(phi))

def fT(t, coeff):
  y = complex(0, 0)
  for (freq, coef) in coefficients:
    y += coef * polar(1.0, freq * 2 * PI * t)
  return y

def approximateCoefficients(freq_range, func, integration_steps=100):
  cs = []
  half_freq = int(freq_range/2)

  for freq in range(-half_freq , half_freq+1):
    integ = complex(0.0, 0.0)
    deltaT = 1.0 / integration_steps
    for j in range(integration_steps):
      integ += deltaT * func(j * deltaT) * polar(1.0, -freq * 2 * PI * (j * deltaT))
    cs.append((freq, integ))
  return cs

'''def approximateCoefficientsMultiDim(freq_range, func, integration_steps=100):
  dims = len(func(0))
  result = []

  for dim in range(dims-1):
    f = lambda t: complex(func(t)[dim], func(t)[dim+1])
    result.append(approximateCoefficients(freq_range, f, integration_steps=100))
  return result'''




