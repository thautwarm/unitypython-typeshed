# UnityPython typeshed

This work is based on [typeshed](https://github.com/python/typeshed/), and the main IDE target is Pylance.

UnityPython has different builtins and different standard libraries wrapping the .NET standard libraries.

When using UnityPython, clone this repo into your UnityPython game's root directory, and write the following JSON configuration in `.vscode/settings.json`:

```json
{
    "python.analysis.typeshedPaths": ["unitypython-typeshed"]
}
```

## Contributing

After implementing new built-in functions at [UnityPython](https://github.com/thautwarm/Traffy.UnityPython/issues), please submit a PR to update this repo as well.

If you develop [`UnityPython.BackEnd`](https://github.com/thautwarm/Traffy.UnityPython/tree/main/UnityPython.BackEnd), you should also clone this project into `$UnityPython/UnityPython.BackEnd`.