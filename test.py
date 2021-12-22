from lat_long.coordinates import Coordinates

# TODO: add assertion target and make test
tests = [
    ("-51.07243737494296,-179.13425063752352", None),
    ("51.07243737494296, -114.13425063752352", None),
    ("51.07243737494296, 114.13425063752352", None),
    ("51.07243737494296,114.13425063752352", None),
    ("51°04'20.8\"N114°08'03.3\"W", None),
    ("51°04'20.8\"N 114°08'03.3\"W", None),
    ("51°04'20.8\"N 114°08'03.3\"E", None),
    ("51°04'20.8\"N114°08'03.3\"E", None),
    ("51°04'20.8\"S 114°08'03.3\"E", None),
    ("51°04'20\"N 114°08'03\"W", None),
    ("51°04'20N 114°08'03W", None),
    ("51°04'N 114°08'W", None),
    ("51°04N 114°08W", None),
    ("51°N 114°W", None),
    ("51N 114W", None),
]

for i, test in enumerate(tests):
    coor_str, target = test
    coordinates = Coordinates()
    coordinates.from_str(coor_str)
    print(f"Case {i}: {coordinates}")
