# Eolymp SDK in Python

This is SDK to talk to Eolymp API server pragmatically. [Learn more](https://support.eolymp.com/dev)

## Quick start example

```python
import eolymp.universe.universe_pb2 as universe_pb2
from eolymp.universe.universe_http import UniverseClient
from eolymp.core.http_client import HttpClient

transport = HttpClient(token="etkn-...")

universe = UniverseClient(transport)
out = universe.ListSpaces(request=universe_pb2.ListSpacesInput())

for space in out.items:
    print(space.name)
```