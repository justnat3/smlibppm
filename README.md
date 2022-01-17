# smlibppm
Small ppm library

## Test it out! 

```sh
# generate a pixel map of random noise
$ py ./ppm.py 
```

## Gettings started

Here is a simple program from this library

The following code generates a 50x50 rectangle of a random colors at position 1,1
in a pixel map
```python
from smlibppm import *
import sys

def main() -> int:

    # init ppm
    ppm = PPM(255, 255)

    # export generate rand color
    ppm.fill_rect(generate_rand_color(), 50, 50, [1,1])
    
    # save the ppm and catch potential errors passed up
    if not ppm.save_as_ppm("./examples/colorful_rect.ppm"):
        print("writing file failed")
        exit(1)

    # success!
    print("Success! Built %s" % sys.argv[1])
    return 0

if __name__ == "__main__":
    main()
```

## Developing
This library follows the current [Python packaging standards](https://packaging.python.org/en/latest/).

[Poetry](https://python-poetry.org) is the build backend and [Poe](https://github.com/nat-n/poethepoet) is the task runner.

### Docs
Documentation is available via [Sphinx](https://www.sphinx-doc.org/en/master/)
and can be built by running:
```shell
poetry run poe docs
```

## References 
- http://netpbm.sourceforge.net/doc/ppm.html
