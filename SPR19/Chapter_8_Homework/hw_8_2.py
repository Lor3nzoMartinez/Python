

prefixes = "JKLMNOPQ"
suffix = "ack"

for j in range(len(prefixes)):
    if prefixes[j] == "Q" or prefixes[j] == "O":
        print(prefixes[j] + 'u' + suffix)
    else:
        print(prefixes[j] + suffix)

