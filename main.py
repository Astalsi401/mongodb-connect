from db_connect import Mongodb


def main():
    db = Mongodb('floormap')
    # do something
    db.close()


if __name__ == '__main__':
    main()
