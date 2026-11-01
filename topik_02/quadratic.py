import math

from topik_01.main import discriminant


def find_roots(a, b, c):
    if a == 0:
        return None

    d = discriminant(a, b, c)

    if d > 0:
        root_d = math.sqrt(d)
        return (-b - root_d) / (2 * a), (-b + root_d) / (2 * a)
    elif d == 0:
        return (-b / (2 * a),)
    else:
        return ()


def main():
    a = float(input())
    b = float(input())
    c = float(input())
    roots = find_roots(a, b, c)

    if roots is None:
        print("a не може дорівнювати нулю")
    elif len(roots) == 0:
        print("Коренів немає")
    else:
        for index, root in enumerate(roots, 1):
            print(f"x{index} = {root}")


if __name__ == "__main__":
    main()
