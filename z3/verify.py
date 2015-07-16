#!/usr/bin/python

import sys

import z3

from mcf2smtlib import uvars, string_from_z3_model, smtlib2_string_from_file

if __name__ == '__main__':
    solver = z3.Solver()
    solver.add(z3.parse_smt2_string(smtlib2_string_from_file(sys.argv[1], sys.argv[3] if len(sys.argv) > 3 else "1")))
    old_vars = uvars
    solver.add(z3.Not(z3.parse_smt2_string(smtlib2_string_from_file(sys.argv[2], sys.argv[4] if len(sys.argv) > 4 else "1"))))
    uvars = uvars | old_vars

    if solver.check() == z3.unsat:
        print "UNSAT"
    else:
        print(string_from_z3_model(solver.model()))
