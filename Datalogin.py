import csv


def datalogin():
    with open("nokeep data.csv", "a+", newline="", encoding="utf8") as f:
        writef = csv.writer(f)
        writef.writerow (["User", "Password"])
        writef.writerow(list(save()))

datalogin()
