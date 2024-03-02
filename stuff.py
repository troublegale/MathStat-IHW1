from math import sqrt


def read_data(file):
    a = []
    for line in file:
        row = [float(f) for f in line.split()]
        a += row
    return sorted(a)


def separate_into_intervals(a, k, l):
    m = [[] for _ in range(k)]
    for i in range(k):
        cur_len = 0
        for j in range(i):
            cur_len += len(m[j])
        thresh = a[cur_len] + l
        for j in range(cur_len, len(a)):
            if a[j] > thresh:
                break
            m[i].append(a[j])
    return m


def interval(a):
    return str(a[0]) + ' - ' + str(a[len(a) - 1]) if len(a) > 1 else str(a[0]) + '\t\t'


def avg(a):
    return (a[0] + a[len(a) - 1]) / 2 if len(a) > 1 else a[0]


def avgs(m):
    return [avg(a) for a in m]


def frequency(a, k):
    return float(len(a)) / k


def frequencies(m, k):
    return [frequency(a, k) for a in m]


def heights(p, l):
    return [i / l for i in p]


def print_info(m, x, p, h):
    print("x_l - x_r\t", "x*\t", "m*", "p*\t", "h", sep="\t\t")
    for i in range(len(m)):
        print(interval(m[i]), format(x[i], '.3f'), len(m[i]), format(p[i], '.2f'), format(h[i], '.3f'), sep="\t\t")


def math_exp(x, p):
    return sum(x[i] * p[i] for i in range(len(x)))


def dispersion(x, p, m):
    return sum((x[i] ** 2) * p[i] for i in range(len(x))) - (m ** 2)


def math_exp_borders(m, d, k):
    t = 1.8331  # Квантиль распределения Стьюдента при b = 0.95 и n-1 = 9
    math_exp_left = m - t * sqrt(d / k)
    math_exp_right = m + t * sqrt(d / k)
    return math_exp_left, math_exp_right


def dispersion_borders(d, k):
    h1 = 2.70039   # Квантиль Хи-квадрат при (1+b)/2 = 0.975 и n-1 = 9
    h2 = 19.02277  # Квантиль Хи-квадрат при (1-b)/2 = 0.025 и n-1 = 9
    disp_right = (k - 1) * d / h2
    disp_left = (k - 1) * d / h1
    return disp_right, disp_left
