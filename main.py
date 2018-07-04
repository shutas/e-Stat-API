"""Call e-Stat's API to Retrieve Japan Trade Data."""
# Written by Shuta Suzuki (shutas@umich.edu)

import pandas

# Retrieve the First Row
contents = pandas.read_csv("https://www.e-stat.go.jp/stat-search/file-" +
                           "download?statInfId=000031731993&fileKind=1",
                           header=None,
                           nrows=2)

# Print Column Header and First Row
print contents

# Checking Correct Data is Retrieved
try:
    print "Retrieving specific content...",

    if contents[0][0] != "Exp or Imp":
        raise Exception

    print "SUCCESS!"

except:
    print "FAIL!"