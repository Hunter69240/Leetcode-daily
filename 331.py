def a():
    preorder = "7,2,#,2,#,#,#,6,#"
    preorder = preorder.split(",")

    slot = 1   # Initially one slot for root

    for node in preorder:

        # Every node consumes one slot
        slot -= 1

        # If no slot available → invalid serialization
        if slot < 0:
            return False

        # If node is not null (#), it creates 2 new slots
        if node != "#":
            slot += 2

    # All slots must be exactly used
    return slot == 0


print(a())