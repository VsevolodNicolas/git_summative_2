def tower_of_hanoi(n, initial_peg, auxilary_peg, ultimate_peg):

    if n > 0:

        tower_of_hanoi(n - 1, initial_peg, ultimate_peg, auxilary_peg)

        if initial_peg[0]:

            disk = initial_peg[0].pop()

            print("Moving disk " + str(disk) + " from " + initial_peg[1] + " to " + ultimate_peg[1] + '.')

            ultimate_peg[0].append(disk)

        tower_of_hanoi(n - 1, auxilary_peg, initial_peg, ultimate_peg)

n = int(input())

disk_list = []

for i in range(n):

    disk_list.append(n - i)

initial_peg = (disk_list, "initial peg")
ultimate_peg = ([], "ultimate peg")
auxilary_peg = ([], "auxilary peg")

tower_of_hanoi(n, initial_peg, auxilary_peg, ultimate_peg)