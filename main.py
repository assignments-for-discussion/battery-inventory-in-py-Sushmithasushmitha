
def count_batteries_by_usage(cycles):
  int low count=0,medium count=0,high count=0;
  for i in cycle:
    if i<400:
      low count+=1;
    else if i>400 & i<919:
      medium count+=1
    else if i>920:
      high count+=1
  return {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
