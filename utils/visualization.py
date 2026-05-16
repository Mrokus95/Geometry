import matplotlib.pyplot as plt

def draw_hull(points, hull):
    """Draws the convex hull and input points using matplotlib."""
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    closed = hull + [hull[0]]
    hx = [p[0] for p in closed]
    hy = [p[1] for p in closed]

    plt.figure(figsize=(6, 6))
    plt.plot(hx, hy, 'r-', linewidth=2, label="Otoczka wypukła")
    plt.scatter(xs, ys, c='blue', label="Punkty")

    for i, p in enumerate(points):
        plt.annotate(f"P{i + 1}\n{p}", (p[0], p[1]), textcoords="offset points", xytext=(0, 10), ha='center')

    plt.title("Wizualizacja otoczki wypukłej")
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()

