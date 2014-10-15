import Testing
import BinaryCSP

lines = Testing.get_lines("cspAdjacency.csp")
csp = Testing.csp_parse(lines)
result = BinaryCSP.solve(csp)
print "CSP modeling seating of guests in a row with constraints on specific seating and adjacency to other guests"
print "Constraints are:"
for constraint in csp.binaryConstraints:
    if constraint.__class__ is BinaryCSP.AdjacentConstraint:
        print " ", constraint.var1, "must be next to", constraint.var2
    elif constraint.__class__ is BinaryCSP.NotAdjacentConstraint:
        print " ", constraint.var1, "cannot be next to", constraint.var2
for constraint in csp.unaryConstraints:
    if constraint.__class__ is BinaryCSP.GoodValueConstraint:
        print " ", constraint.var, "must be at seat", constraint.goodValue
    elif constraint.__class__ is BinaryCSP.BadValueConstraint:
        print " ", constraint.var, "cannot be at seat", constraint.badValue
print
print "CSP Solution"

firstLine = "Seat:"
secondLine = "Guest:"

seats = {}
for guest in result:
    seats[result[guest]] = guest

for seat in sorted(seats.keys()):
    firstLine += "\t" + seat
    secondLine += "\t" + seats[seat]
print firstLine
print secondLine
