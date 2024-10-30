import os
import struct

from src.btree import BTree


def test(order, generated, debug=False):
    if debug:
        print("Input", generated)

    t = BTree(order)
    for i, v in enumerate(generated):
        if debug:
            print("nth", i + 1)
        t = t.insert(
            {
                "key": v,
                "value": v,
            }
        )
        if debug:
            print(sorted(generated[: i + 1]), [x["key"] for x in t.list()])
        assert sorted(generated[: i + 1]) == [x["key"] for x in t.list()]
        if debug:
            t.print()

    if debug:
        print("Output")
    if debug:
        t.print()

    klist = [x["key"] for x in t.list()]
    if debug:
        print(klist)

    s = sorted(generated)
    for i in range(len(s)):
        assert s[i] == klist[i], f"wanted {s[i]}, got {klist[i]}"
    assert len(klist) == len(s), f"wanted: {len(s)}, got len(l)"

    assert sorted(generated) == [x["key"] for x in t.list()]


# First insert backwards
generated = []
for i in list(reversed(range(10))):
    r = i
    generated.append(r)

test(3, generated)

# Then insert going forward.
generated = []
for i in list(range(10)):
    r = i
    generated.append(r)

test(3, generated)

# Then insert randomly.
generated = []
for _ in list(range(10)):
    r = struct.unpack("H", os.urandom(2))[0]
    generated.append(r)

test(3, generated)

generated = []
for _ in list(range(20)):
    r = struct.unpack("H", os.urandom(2))[0]
    generated.append(r)

test(8, generated)

# Now let's try some big ones.
# for tree_size in [3, 100, 4096]:
#     generated = []
#     for _ in list(range(10000)):
#         r = struct.unpack("H", os.urandom(2))[0]
#         generated.append(r)

#     test(tree_size, generated)
#     print(tree_size, len(generated))
