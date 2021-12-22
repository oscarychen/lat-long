# Lat-long

A Latitude-Longitude coodinates library.

### Install

```
pip install git+https://github.com/oscarychen/lat-long.git
```

### Usage

```python
from lat_long.coordinates import Coordinates
coordinatesA = Coordinates()
coordinatesB = Coordinates()
coordinatesC = Coordinates()
coordinatesA.from_str("-51.07243737494296,-179.13425063752352")
coordinatesB.from_str("51°04'20.8\"N114°08'03.3\"W")
coordinatesC.from_dms(lat_degree=51, lat_minute=5, lat_second=0, south_north='N',
                 long_degree=114, long_minute=8, long_second=5.5, east_west='E')
print(coordinatesA)
print(coordinatesB)
print(coordinatesC)
```

### To-do

- Calculate distance between two coordinates
- Add tests
