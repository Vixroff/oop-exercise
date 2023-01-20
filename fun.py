class B:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


if __name__ == "__main__":
    x = B("YO", "YOYO")
    print(x.name)
    print(x.surname)