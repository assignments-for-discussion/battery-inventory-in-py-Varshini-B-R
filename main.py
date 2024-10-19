
def count_batteries_by_health(present_capacities):
  rated_capacity = float(input("Enter the rated capacity: "))
  return {
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }

for current_capacity in present_capacities:
  SOH = (present_capacity / rated_capacity) * 100
  print("SOH of " ,current_capacity, ": " ,SOH)

  if 

def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
