# <a href="url"><img src="https://user-images.githubusercontent.com/90220978/156864431-985232c6-a0b3-42b6-85f9-f66b5932ebad.png" align="middle" width="60" height="60"></a> AirBnB Clone - The Console

<div id='id-section1'/>
<p align="center">
  <img src="https://i.imgur.com/ogbfW3k.png">
</p>

<h3>Welcome to the AirBnB clone project! ✌️ </h3>

The goal of the project is to deploy on your server a simple copy of the AirBnB website. This is the first step towards building our first full web application: the AirBnB clone. A command interpreter is created in this segment to manage objects for the AirBnB website.

### Table of Content

- [AirBnB Clone](#id-section1)
- [Description](#id-section2)
- [Installation](#id-section3)
- [Usage](#id-section4)
- [Commands](#id-section5)
- [Classes](#id-section6)
- [Requeriments](#id-section7)
- [Authors](#id-section8)

<div id='id-section2'/>
<h4>First step: Write a command interpreter to manage your AirBnB objects.</h4>

<p>This is the first step towards building your first full web application: the <strong>AirBnB clone</strong>.
This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration… </p>

<p>Each task is linked and will help you to:</p>

<ul>
<li>put in place a parent class (called <code>BaseModel</code>) to take care of the initialization, serialization and deserialization of your future instances</li>
<li>create a simple flow of serialization/deserialization: Instance &lt;-&gt; Dictionary &lt;-&gt; JSON string &lt;-&gt; file</li>
<li>create all classes used for AirBnB (<code>User</code>, <code>State</code>, <code>City</code>, <code>Place</code>…) that inherit from <code>BaseModel</code></li>
<li>create the first abstracted storage engine of the project: File storage. </li>
<li>create all unittests to validate all our classes and storage engine</li>
</ul>

<h3> What’s a command interpreter? 💻</h3>
<p>Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:</p>

<ul>
<li>Create a new object (ex: a new User or a new Place)</li>
<li>Retrieve an object from a file, a database etc…</li>
<li>Do operations on objects (count, compute stats, etc…)</li>
<li>Update attributes of an object</li>
<li>Destroy an object</li>
</ul>

<div id='id-section3'/>

### Installation 🔧

Use [git](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) to clone this repository in your local machine

```bash
git clone https://github.com/SharaGB/AirBnB_clone.git
```

<div id='id-section4'/>

### Usage 👾
* All files are interpreted/compiled on Ubuntu 40.04 LTS using Python3 (version 3.8.10)
* You can run it writting <code>./console.py</code> in your terminal
* You can use the console in two different modes:

Your console should work like this in interactive mode:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

<div id='id-section5'/>

### Commands incorporated in our console 🐚

|   *Command*   |                                                *Description*                                                 |       *Example*       |
| ------------- | ------------------------------------------------------------------------------------------------------------ | --------------------  |
|     quit      |                                               Exit the program                                               |         quit          |
|     EOF       |                                               Exit the program                                               |        Ctrl+D         |
|     help      |                                            Description to function                                           |       help quit       |
|  empty line   |                                           Shouldn’t execute anything                                         |         ENTER         |
|    create     |                    Creates a new instance, saves it (to the JSON file) and prints the id                     |      create User      |
|     show      |                  Prints the string representation of an instance based on the class name and id              |     show User 'id'    |
|    destroy    |                               Deletes an instance based on the class name and id                             |   destroy User 'id'   |
|      all      |                 Prints all string representation of all instances based or not on the class name             |       all User        |
|    update     |                 Updates an instance based on the class name and id by adding or updating attribute           | update User+key+value |

<div id='id-section6'/>

### Classes you can use

|   *All Classes*   |                                   *Description*                                       |
| ----------------- |  ------------------------------------------------------------------------------------ |
|       User        |   Class User, that inherits from BaseModel and contains specific public attributes    |
|       State       |   Class State, that inherits from BaseModel and contains specific public attributes   |
|       City        |   Class City, that inherits from BaseModel and contains specific public attributes    |
|       Amenity     |   Class Amenity, that inherits from BaseModel and contains specific public attributes |
|       Place       |   Class Place, that inherits from BaseModel and contains specific public attributes   |
|       Review      |   Class Review, that inherits from BaseModel and contains specific public attributes  |


<div id='id-section7'/>

### Example

(hbnb) create User
* ecd15b51-1b07-4dcc-a0ee-6f9ababb00fe

This command create a new entrance in the memory and return a unique id number.

(hbnb) show User ecd15b51-1b07-4dcc-a0ee-6f9ababb00fe
* \[User\] (ecd15b51-1b07-4dcc-a0ee-6f9ababb00fe) {'id': 'ecd15b51-1b07-4dcc-a0ee-6f9ababb00fe', 'created_at': datetime.datetime(2022, 3, 5, 16, 43, 31, 938584), 'updated_at': datetime.datetime(2022, 3, 5, 16, 43, 31, 938671)}

This command displays a dictionary with all the attributes that was create for the new entrance.

<div id='id-section8'/>

### Requeriments ✔️

- [x] Write a [README]()
- [x] Have an [AUTHORS](https://github.com/SharaGB/AirBnB_clone/blob/main/AUTHORS) file at the root of your repository
- [x] Use brances and pull requests on GitHub
- [x] Write beautiful code that passes the PEP8 checks.
- [x] All your files, classes, functions must be tested with unit tests
- [x] Write a class [BaseModel](https://github.com/SharaGB/AirBnB_clone/blob/main/models/base_model.py) that defines all common attributes/methods for other classes
- [x] Write a class [FileStorage](https://github.com/SharaGB/AirBnB_clone/blob/main/models/engine/file_storage.py) that recreates a BaseModel from another one by using a dictionary representation
- [x] Write a [console](https://github.com/SharaGB/AirBnB_clone/blob/main/console.py) that contains the entry point of the command interpreter
- [x] Write all those classes that inherit from BaseModel


<div id='id-section8'/>

## Authors 🖋️

* [__Daniela Botero__](https://github.com/DaboRestrepo)
* [__Shara García__](https://github.com/SharaGB)
