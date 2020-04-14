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
            perceptions_processed.append(float(perceptions))
            plans_created.append(int(plans))
        except ValueError:
            pass

    print(f"VTIME: {mean(vtimes)}")
    
    pp_mean = mean(perceptions_processed)
    pp_string = "{:.2f}".format(pp_mean)
    print(f"PERCEPTIONS PROCESSED: {pp_string}")

    print(f"PLANS CREATED: {mean(plans_created)}")
