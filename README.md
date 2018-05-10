# ud036_StarterCode
This is a Source code for a Movie Trailer website.
you could use this code to show your favorite movies as if they are being 
hosted in a web server.


## Installation

clone the github repository and use python to run the code
```
 $ git clone https://github.com/ibrasec/ud036_StarterCode
 $ cd ud036_StarterCode
 $ python entertainment_center.py
```



## File hierarchy

If you clone or download this repository you should have 3 python files:

 1- **fresh_tomatoes.py**: Creates the Movies Trailer Website.

 2- **media.py**: Stores the Movie class

 3- **entertainment_center.py** : Uses both the fresh_tomatoes and the media modules to finally construct the Movies Trailer Website.


## Usage

If you want to add your favorite movies to the list, you have to know the below
informations for each movie:

* movie's title
* movie's storyline
* movie's poster image
* movie's Youtube URL

Open the **entertainment_center.py** file and add a variable name ( as example: _Somevaraible_ )
to meet the below format, and pass the movies related arguments each as a string:

somevariable = media.Movie(**movie's title**, **movie's storyline**, **movie's poster image**, **movie's Youtube URL**)

Append the varaible name you already created to the movies list:

`movies = [ , , , somevariable]`

Now simply save and run the code:

` $ python entertainment_center.py`


## License

ud036_StarterCode is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

ud036_StarterCode is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with ud036_StarterCode.  If not, see <http://www.gnu.org/licenses/>.
