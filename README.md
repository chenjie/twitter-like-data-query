# twitter-like-data-query
A simple program illustrates the basic idea of query language such as SQL, which is widely used in industrial relational databases. This plays an important role in retrieving customized data from huge amount of information based on the data query.

## Getting Started

### Prerequisites

* Python 3.x
* Termial (in Unix) OR PowerShell (in Windows)

### Download and run the program
```
# Change to HOME directory
$ cd ~

# Clone this repo and 'cd' into it
$ git clone https://github.com/jellycsc/twitter-like-data-query.git
$ cd twitter-like-data-query/

# Let's start playing
$ python3 twitterverse_program.py 
```

## Example
```
Data file: data.txt
Query file: query.txt
----------
a
name: Alex D
location: Abbottsford, British Columbia
website: www.abbotsford.ca
bio:
Love the outdoors, even 
in the rain.
following: ['tomfan']
----------
b
name: Benny Lewis
location: Bankok
website: 
bio:

following: ['tomfan']
----------
```
The program searches the data file and correctly filteres out the information that user needs based on the data query.  
[Here](data.txt) is the content of example data file, which you can get using API calls.
```
tomCruise
Tom Cruise
Los Angeles, CA
http://www.tomcruise.com
Official TomCruise.com crew tweets. We love you guys! 
Visit us at Facebook!
ENDBIO
katieH
NicoleKidman
END
PerezHilton
Perez Hilton
Hollywood, California
http://www.PerezH...
Perez Hilton is the creator and writer of one of the most famous websites
in the world. And he also loves music - a lot!
ENDBIO
tomCruise
katieH
NicoleKidman
END
katieH
Katie Holmes

www.tomkat.com
ENDBIO
END
NicoleKidman
Nicole Kidman
Oz

At my house celebrating Halloween! I Know Haven't been on like 
years So Sorry,Be safe And have fun tonight
ENDBIO
END
...
```

## Authors

| Name             | GitHub                                     | Email
| ---------------- | ------------------------------------------ | -------------------------
| Chenjie Ni       | [jellycsc](https://github.com/jellycsc)    | nichenjie2013@gmail.com

## Thoughts and future improvements 

* The only piece missing here is how to get data directly from Twitter server, rather than through a static data file.

## Contributing to this project

1. Fork it ( https://github.com/jellycsc/twitter-like-data-query/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to your feature branch (`git push origin my-new-feature`)
5. Create a new Pull Request

Details are described [here](https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project).

## Bug Reporting
Please log bugs under [Issues](https://github.com/jellycsc/twitter-like-data-query/issues) tab on github.  
OR you can shoot an email to <nichenjie2013@gmail.com>
