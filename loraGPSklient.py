def main():
    while True:
        with open("/dev/ttyS0","r") as f:
            data = f.read()
            commands = data.split("\n")
            for command in commands:
                args = command.split(",")
                if args[0] == "$GPGGA":
                    print(args)

main()