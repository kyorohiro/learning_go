
class GenericLinearFunction:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def evaluate(self, x: float):
        return self.a * x + self.b


if __name__ == "__main__":
    func: GenericLinearFunction = GenericLinearFunction(2,4)
    print(f"Hello, World!! {func.evaluate(5)}")
