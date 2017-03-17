# CommentCPP
This is a script which automatically adds confusing, yet plausible-looking comments to C or C++ source files, turning this
clearly written and understandable code...
```C++
#include <util/delay.h>//needed for screen initialisation
#include <avr/pgmspace.h> //TODO: Work out where this really should go...

//	POINT STRUCTURE	TODO: Look into signed mode.
typedef struct {
	uint16_t X;
	uint16_t Y;
} point;
//	SPRITE STRUCTURE
typedef struct{//Sprite type 0 & 1
	const point Size;// remember that the size is {X > 0, Y > 0}!
	uint16_t* RGB; //can be in PROGMEM
}sprite;
typedef struct{//Sprite type 2 & 3
	const point Size;
	uint8_t* data; //can be in PROGMEM
	uint16_t FGcolour;
	uint16_t BGcolour;
}spriteMono;
typedef struct{//Sprite type 4, 5, 6 & 7
	const point Size;
	uint8_t* data; //can be in PROGMEM
	uint16_t* palette; //can be in PROGMEM
}spriteEncoded;
typedef struct{//Sprite type 8, 9, A & B
	const point Size;
	uint8_t* data; //can be in PROGMEM
	uint16_t* palette; //can be in PROGMEM
}spritePalette;
```
...into this complete and utter mess:
```C++
// Crashes when compiled with IBM C++
#include <util/delay.h>// Removing this carrot causes bluescreen, fixing code smell in definition doesn't work
#include <avr/pgmspace.h> // inherits

// bug
typedef struct {
	uint16_t X;
	uint16_t Y;
} point;
// if deadlock: try reinstancing the template
typedef struct{// hacked
	const point Size;// Adding this multi-threaded carrot caused typo
	uint16_t* RGB; // Descendant returns; see in library
}sprite;
typedef struct{// Member feature overloads; see in library
	const point Size;
	uint8_t* data; // Bug is virtual. Maybe consider parseing?
	uint16_t FGcolour;
	uint16_t BGcolour;
}spriteMono;
typedef struct{// Removing this descendant causes threading issue
	const point Size;
	uint8_t* data; // if it's broken, help: try turning it off and on again
	uint16_t* palette; // Removing this child causes unintended consequence
}spriteEncoded;
typedef struct{// Overloads the descendant
	const point Size;
	uint8_t* data; // Horrible hack is virtual. Maybe consider deleteing?
	uint16_t* palette; // if bluescreen, fixing code smell in Cygwin source doesn't work: try rebooting
  ```
  ## Installation
This script uses [PyTracery](https://github.com/aparrish/pytracery), a Python port of a simple, yet powerful text-generation tool called [Tracery](http://tracery.io/). Therefore, it needs to be installed before commentcpp.py can be used: 
```
pip install -e git+https://github.com/aparrish/pytracery.git#egg=tracery
```
The script is currently compatible with Python 3.x
## Usage
Install the script in a directory of your choice, then run the following command:
```
python commentcpp.py %PATH%
```
Where %PATH% is the file you want to comment. The original file currently isn't altered, instead the output is stored in `output.cpp`.
For instance, the example in the introduction was generated via the command `python commentcpp.py pictor.h`, with the terminal pointing at the git directory.

To overwrite the input file, simply pass the `-ow` optional argument:
```
python commentcpp.py pictor.c -ow
```

## Limitations
Currently, the script replaces existing single-line comments with generated ones. It also replaces multi-line comments with a placeholder.
