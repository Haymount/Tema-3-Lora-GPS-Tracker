def main():
    while True:
        with open("/dev/ttyS0","r") as f:
            data = f.read(500)
            commands = data.split("\n")
            for command in commands:
                args = command.split(",")
                if args[0] == "$GPGGA":
                    print(args)

main()

#https://www.google.com/maps/@57.0207251,9.8850979,18.38z