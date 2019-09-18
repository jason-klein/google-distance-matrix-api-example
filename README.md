# Mean Time to Lunch (MTTL)

This code supplements my lightning talk at [**DevFest Springfield 2019**](https://devfestsgf.com). 
I demonstrate how to use the Google Distance Matrix API to calculate the most convenient lunch location given a list of potential attendee addresses and a list of potential event locations.

## Getting Started  

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

This code requires Python 3

```
$ python -V
Python 3.7.0
```

This code also requires a [Google Maps API key](https://cloud.google.com/maps-platform/). Be sure to allow Google Distance Matrix API calls.

Cost: Be aware that calls to the Google Distance Matrix API cost $5 per 1K elements. 
Each origin/destination pair in your request is considered an element, 
so multiply the number of origins with the number of destinations to determine the number of elements in your API call. 
For example, an API call with 100 origins (potential lunch attendees) and 10 destinations (potential lunch event locations) would contain 1000 elements (100 x 10) and would cost $5.00 total.

Caveats: This sample code queries each element separately and caches the results to allow repeat analysis without incurring additional charges. 
Be sure to avoid caching invalid responses (e.g. errors). Be sure to manage cache expiration if you choose to cache API responses.


### Installing

You must clone or download this repository, initialize a Python environment with dependencies, and populate your data files before you can run the demo scripts.

Clone the repository to your computer
```
git clone https://github.com/jason-klein/google-distance-matrix-api-example.git
```

Create virtual environment

```
python -m venv venv
```

Activate virtual environment

```
source ./venv/bin/activate
```

Install package requirements

```
pip install -r requirements.txt
```

Copy sample member data file OR download member data

```
cp members.dat.sample members.dat
# or
python members.py
```

Prune member data to remove PO Boxes and out of state addresses

```
./members-prune.sh
```

Copy sample event location data

```
cp events.dat.sample events.dat
```

Calculate distances from each member to potential event locations

```
python distance.py
```

Analyze pipe-delimited data file

```
cat distance.csv
```

## Running the tests

This demo does not contain tests.

## Deployment

This demo is not intended for production.

## Built With

* [Python](https://www.python.org/) - The programming language used
* [Google Maps](https://cloud.google.com/maps-platform/) - The maps platform used

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

This demo is not versioned

## Authors

* **Jason Klein** - *Initial work* - [jason-klein](https://github.com/jason-klein)

See also the list of [contributors](https://github.com/google-distance-matrix-api-example/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [AITP of the Ozarks](https://aitpozarks.org) - 
Thank you for the opportunity to serve as your board President (2016-2017). 
This demo is based on code I wrote in early 2016 to calculate the average travel time to potential meeting locations after our chapter outgrew the meeting space at [eFactory](https://efactory.missouristate.edu). 
This code determined that Hilton Garden Inn was the most convenient location for our 280 members. 
The chapter met at HGI for two years (2017-2018).
* [Google DevFest Springfield](https://devfestsgf.com) - 
Thank you for the opportunity to speak at your event again this year.
* [Mid-America Technology Alliance](https://matasgf.com) 
and [Springfield Devs](https://sgf.dev) - 
Thank you to everyone involved in these organizations for doing their part to help make tech events like DevFest possible in the Springfield Missouri technology community.
* [Logic Forte](http://logicforte.com) - 
Thank you for paying for the API costs related to producing this demo.
