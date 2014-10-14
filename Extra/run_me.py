import Testing
import BinaryCSP

lines = Testing.get_lines("cspAdjacency.csp")
csp = Testing.csp_parse(lines)
result = BinaryCSP.solve(csp)
print "CSP modeling seating of guests in a row with constraints on specific seating"
print "and adjacency to other guests. Results take the form of GUEST : SEAT"
print result
