# Calculate the cost of painting the following building's walls(both interior and exterior).
# You need to accept the area(one wall) and cost of both interior and exterior wall.
a=int(input("Enter area of a wall(sq.m.):"))
I=int(input("Enter cost of painting interior wall(Rs.):"))
E=int(input("Enter cost of painting exterior wall(Rs.):"))
side_of_wall=a**0.5
interior_area=a*8
exterior_area=a*7
Totalcost_interior=interior_area*I
Totalcost_exterior=exterior_area*I
total_cost=Totalcost_interior+Totalcost_exterior
print(f"Cost of painting interior wall is{Totalcost_interior}")
print(f"Cost of painting exterior wall is{Totalcost_exterior}")
print(f"Total cost of painting is {total_cost}")