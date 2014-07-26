# Copyright (c) 2014 Parker Harris Emerson
# Subject to the MIT License; please see file LICENSE.

# Replaces all instances of a user's name with [REDACTED], or vis a versa.

import sys, fileinput, getopt

def main(argv):

  NAME = "Parker Harris Emerson"
  REDACT = "[REDACTED]"
  redact_file = ""
  redact_option = True

  try:
    opts, args = getopt.getopt(argv,"hnri:",["ifile="])
  except getopt.GetoptError:
    print("name-strip.py -i <input_file>")
    sys.exit(2)
  for opt, arg in opts:
    if opt in ("-h", "--help"):
      print("name-strip.py HELP\n\t-i <input_file>\t selects input file to redact / unredact")
      print("\t-r\treplaces your name with [REDACTED], default option")
      print("\t-n\treplaces [REDACTED] with your name")
      sys.exit()
    elif opt in ("-i", "--ifile"):
      redact_file = arg
    elif opt in ("-r", "--redact"):
      redact_option = True
    elif opt in ("-n", "--name"):
      redact_option = False
  if redact_file == "":
    print("No file entered. Program terminating.")
    sys.exit()

  print("Input file is", redact_file)

  if redact_option:
    for line in fileinput.input(redact_file, inplace=True):
        print(line.replace(NAME, REDACT), end='')
    print("Replacing", NAME, "with", REDACT)
  else:
    for line in fileinput.input(redact_file, inplace=True):
        print(line.replace(REDACT, NAME), end='')
    print("Replacing", REDACT, "with", NAME)

if __name__ == "__main__":
   main(sys.argv[1:])
