# Lat-long

A Latitude-Longitude coordinates library.

### Install

```
pip install git+https://github.com/oscarychen/lat-long.git
```

### Quick start

#### Instantiating a Coordinates object

```python
from lat_long.coordinates import Coordinates
```

Create coordinates by specifying DMS components:

```python
coor = Coordinates(lat_degree=37, lat_minute=14, lat_second=35.16, south_north='N',
                 long_degree=115, long_minute=47, long_second=34.8, east_west='E')
```

Create coordinates by specifying decimals:

```python
coor = Coordinates(lat=37.2431, long=115.7930)
```

Create coordinates by parsing a string description of decimals:

```python
coor = Coordinates("37.2431, 115.793")
```

Create coordinates by parsing a string description of DMS:

```python
coor = Coordinates("37°14'35.16\"N 115°47'34.8\"E")
```

#### Usage

Get DMS representation:

```python
coor.to_dms()
# 37°14'35.16"N 115°47'34.8"E
```

Get decimal representation:

```python
coor.to_decimals()
# 37.2431, 115.793
```

Check equality:

```python
coor1 = Coordinates(lat=37.2431, long=115.7930)
coor2 = Coordinates("37°14'35.16\"N 115°47'34.8\"E")
print(coor1 == coor2)
# True
```

### To-do

- Calculate distance between two coordinates
- Add tests

```

```
