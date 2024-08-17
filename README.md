From a conversation. "I want a better CSV that knows what my columns mean".

ACSV is "Annotated CSV" format. Annotations are provided in a "preamble". As far
as possible, annotation semantics are left up to the consuming code. The only exception
to this (in this POC version) is that there must be a list of "columns", and the metadata
for each column must include a "fieldname" property. This is passed to csv.DictReader,
and will presumably be made optional in some way.


Annotations come in two flavors:
Global annotations apply to the document as a whole, and might include title, description,
that sort of jazz.

Column annotations are listed in order. Column annotations currently must include
a "fieldname" for each column - this is passed to csv.DictReader.


Usage:

>>> from acsv import DictReader
>>> f = open("test.acsv")
>>> dr = DictReader(f)
>>> dr.annotations
{'global': {'title': 'Test CSV', 'description': 'An annotated CSV document for testing ACSV code'}, 'columns': [{'fieldname': 'Time', 'units': 'seconds', 'type': 'int'}, {'fieldname': 'Distance', 'units': 'meters', 'type': 'float'}]}
>>> [row for row in dr]
[{'0': '1'}, {'0': '2'}, {'0': '3.1'}, {'0': '3.9'}, {'0': '4.8'}]



Status:
This first pass is purely a POC, using JSON for the preamble.
Next step is to develop a better format for the preamble and implement that.
