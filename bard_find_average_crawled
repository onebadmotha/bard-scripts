import pandas as pd

def calculate_average_pages_looked_at_daily(discovered_not_crawled_list):
  """Calculates the average pages looked at daily.

  Args:
    discovered_not_crawled_list: A list of the number of pages discovered but not crawled on each day.

  Returns:
    The average pages looked at daily.
  """

  # Create a Pandas DataFrame.
  df = pd.DataFrame(discovered_not_crawled_list, columns=["discovered_not_crawled"])

  # Calculate the difference between each row and the previous row.
  df["difference"] = df["discovered_not_crawled"].diff()

  # Calculate the average of the differences.
  average_difference = df["difference"].mean()

  return average_difference

# Get the list of discovered but not crawled pages.
discovered_not_crawled_list = [2272202, 2226330, 2226330, 2226330, 2256168, 2256168, 2256168, 2256168, 2272142, 2272142, 2272142, 2323001, 2323001, 2323001, 2323001, 2323844, 2323844, 2323844, 2325409, 2325409, 2325409, 2325409, 2325409, 2325409, 2325632, 1992772, 1992772, 1992772, 1992772, 2237507, 2237507, 2237507, 2082840, 2082840, 2082840, 2082840, 1988109, 1988109, 1988109, 1988109, 1988109, 1988109, 1988109, 1988109, 1988109, 1988109, 2339545, 2339545, 2339545, 2339545, 2336691, 2336691, 2336691, 2249975, 2249975, 2249975, 2249975, 2316931, 2316931, 2316931, 2230135, 2230135, 2230135, 2230135, 2075910, 2075910, 2075910, 1857888, 1857888, 1857888, 1857888, 2121706, 2121706, 2121706, 2314036, 2314036, 2314036, 2314036, 2283446, 2283446, 2283446, 2254992, 2254992, 2254992, 22549
