# Eolymp SDK in Python

This is SDK to talk to Eolymp API server pragmatically. [Learn more](https://support.eolymp.com/dev)

## Quick start example

```python
import eolymp.universe
import eolymp.core

transport = eolymp.core.HttpClient(token="etkn-...")

spaces = eolymp.universe.SpaceServiceClient(transport)
out = spaces.ListSpaces(request=eolymp.universe.ListSpacesInput())

for space in out.items:
    print(space.name)
```