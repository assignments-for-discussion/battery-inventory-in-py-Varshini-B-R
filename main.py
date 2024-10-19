def count_batteries_by_health(present_capacities):
    rated_capacity = 120
    health_counts = {
        "healthy": 0,
        "exchange": 0,
        "failed": 0
    }

    for current_capacity in present_capacities:
        SoH = (current_capacity / rated_capacity) * 100
        print("SoH of", current_capacity, ":", SoH)

        if SoH > 80:
            health_counts["healthy"] += 1
        elif 62 < SoH <= 80:
            health_counts["exchange"] += 1
        else:
            health_counts["failed"] += 1

    print("Counts:")
    print("Healthy:", health_counts["healthy"])
    print("Exchange:", health_counts["exchange"])
    print("Failed:", health_counts["failed"])


    return health_counts


def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")
    present_capacities = [113, 116, 80, 95, 92, 70]
    counts = count_batteries_by_health(present_capacities)
    print()
    assert(counts["healthy"] == 2)
    assert(counts["exchange"] == 3)
    assert(counts["failed"] == 1)

    # Test case (all healthy)
    present_capacities_1 = [121, 125, 115, 130]
    counts_1 = count_batteries_by_health(present_capacities_1)
    print()
    assert(counts_1["healthy"] == 4)
    assert(counts_1["exchange"] == 0)
    assert(counts_1["failed"] == 0)

    # Test case (mixed capacities)
    present_capacities_2 = [100, 60, 75, 90]
    counts_2 = count_batteries_by_health(present_capacities_2)
    print()
    assert(counts_2["healthy"] == 1)
    assert(counts_2["exchange"] == 2)
    assert(counts_2["failed"] == 1)

    # Test case (all failed)
    present_capacities_3 = [60, 50, 30, 20]
    counts_3 = count_batteries_by_health(present_capacities_3)
    print()
    assert(counts_3["healthy"] == 0)
    assert(counts_3["exchange"] == 0)
    assert(counts_3["failed"] == 4)
    print("\nDone counting :)")


if __name__ == '__main__':
    test_bucketing_by_health()
