## Solution Validator

This is an initial implementation of a **solution logic validator** using OWL and SHACL. It defines the ontology, validation constraints, and a set of test cases.

The five rules enforced in SHACL are specified in the THE RULES.txt file.

### Running the Test Battery

To run all test cases at once, use:

```bash
python .\test.py
```

This runs all `.ttl` test files in the `tests` directory and reports whether each test conforms to the defined SHACL constraints. For failed tests, the corresponding validation message is also displayed.

### Running a Specific Test

To run an individual test directly with `pySHACL`, use:

```bash
python -m pyshacl -s SHACL.ttl -e ontology_OWL.ttl -f human .\tests\Baseline_test.ttl
```

For example, the command above runs `Baseline_test.ttl` against the SHACL constraints defined in `SHACL.ttl`, using `ontology_OWL.ttl` for entailment.

Other test files can be run by replacing Baseline_test.ttl with the desired test file name.
