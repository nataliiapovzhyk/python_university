anton = {"GoIt", "Chernobyl", "Friends"}
boris = {"Friends", "Office", "Ivan", "Chernobyl"}

def interset(one, two):
    return one.symmetric_difference(two)

print(interset(anton, boris)) 