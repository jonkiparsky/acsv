# Annotated CSV handler
# Read csvs with annotation "preamble"
# Basic idea: metadata should live with data, but be distinct from it.
# Annotations allow the user to specify arbitrary facts about their CSV
# data, which is made available to the consuming program (which may use it
# or ignore it).
# Semantics are the business of the user, this reader makes no attempt to
# impose semantics. This means that consuming programs will have to devise
# and communicate their own semantic expectations.
# It's also okay to have no semantics at all, for example if you just want
# to document column names and such, you can do that. (But acsv will attempt
# to provide help worth using)

# First pass: use JSON for annotations.
# Arbitrarily use the string "#~#~" to denote start and end of annotation
# section.
import csv
import json


PREAMBLE_DELIMITER = "#~#~"

class DictReader():
    # Name intentionally duplicates csv.DictReader
    #
    def __init__(self, input_stream):
        # input_stream should be an iterator delivering a sequence of strings,
        # either a File object or a list of strings will work
        self.input_stream = input_stream
        i = iter(self.input_stream)
        # assume that a preamble exists for now
        # ideally, should tolerate absence of preamble and just read with
        # csv.DictReader

        self.preamble = ""
        while (line := next(i).strip()) != PREAMBLE_DELIMITER:
            pass  # consume lines until we get to the start of preamble

        while (line := next(i).strip()) != PREAMBLE_DELIMITER:
            self.preamble += line
        self.annotations = json.loads(self.preamble)
        self.fieldnames = [col['fieldname'] for col in self.annotations['columns']]
        self.reader = csv.DictReader(self.input_stream, fieldnames=self.fieldnames)

    def __iter__(self):
        return self.reader
