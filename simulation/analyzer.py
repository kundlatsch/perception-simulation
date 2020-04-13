from statistics import mean


def get_mean():
    results = open("results.txt", "r")

    content = results.read().split(";")

    vtimes = []
    perceptions_processed = []
    plans_created = []

    for c in content:
        try:
            (vtime, perceptions, plans) = c.split(",")
            vtimes.append(int(vtime))
            perceptions_processed.append(int(perceptions))
            plans_created.append(int(plans))
        except ValueError:
            pass

    print(f"VTIMES: {mean(vtimes)}")
    print(f"PERCEPTIONS PROCESSED: {mean(perceptions_processed)}")
    print(f"PLANS CREATED: {mean(plans_created)}")
