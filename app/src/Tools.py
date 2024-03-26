from fake_useragent import UserAgent


def getShape():
    shape = UserAgent()
    return shape.getRandom["useragent"]

def main():
    return getShape()



if __name__ == "__main__":
    print(main())