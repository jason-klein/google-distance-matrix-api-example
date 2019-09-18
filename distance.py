from logic.cache import url_fetch
import json
import sys


def get_drive_time(key, origin, destination):
    """
    Return the driving time in seconds between origin and destination addresses
    using the Google Maps Distance Matrix API.
    API: https://developers.google.com/maps/documentation/distance-matrix/start
    COST: $5 per 1000 elements. Each origin/destination pair is one element.
    Multiply number of origins by number of destinations to calculate total
    number of elements in your request (e.g. 10 orig. x 2 dest. = 20 elements)

    # INPUT -------------------------------------------------------------------
    key                     [str]
    origin                  [str]
    destination             [str]

    # RETURN ------------------------------------------------------------------
    drive_time              [integer] (seconds)
    """
    # remove periods and commas, replace space with plus (+)
    origin = origin.replace('.', '')
    origin = origin.replace(',', '')
    origin = origin.replace(' ', '+')

    # remove periods and commas, replace space with plus (+)
    destination = destination.replace('.', '')
    destination = destination.replace(',', '')
    destination = destination.replace(' ', '+')

    url = ('https://maps.googleapis.com/maps/api/distancematrix/json'
           + '?language=en-US&units=imperial'
           + '&origins={}'
           + '&destinations={}'
           + '&key={}'
           ).format(origin, destination, key)

    response = url_fetch(url)

    try:
        response_json = json.loads(response)
        drive_time_seconds = response_json['rows'][0]['elements'][0]['duration']['value']
    except:
        print('ERROR: {}, {}'.format(origin, destination))
        drive_time_seconds = 0

    return drive_time_seconds


def get_key():
    filename = 'key.txt'
    file = open(filename, 'r')
    return file.read().strip()


def save_lines_to_file(lines, file):
    with open(file, 'w') as f:
        for line in lines:
            f.write("%s\n" % line)


if __name__ == '__main__':
    api_key = get_key()

    origins_filename = 'members.dat'
    """
    SAMPLE MEMBER LOCATION DATA
    
    Bass Pro Shops|(417) 873-5000|2500 E. Kearney, Springfield, MO 65898|www.basspro.com
    Hotels.com, a division of Expedia, Inc.|(417) 521-1760|5000 W. Kearney, Springfield, MO 65803|www.expedia.com
    Jack Henry & Associates|(417) 888-4900|3725 E. Battlefield, Springfield, MO 65809|www.jackhenry.com
    JMARK Business Solutions, Inc.|(417) 863-1700|601 N. National, Suite 102, Springfield, MO 65802|www.jmark.com
    KPM Technology, LLC|(417) 875-1100|1445 E. Republic, Springfield, MO 65804|www.kpmtechnology.com
    Logic Forte|(417) 720-2325|PO Box 358, Nixa, MO 65714|logicforte.com/about/our-office/
    Missouri State University efactory|(417) 837-2600|901 S. National, Springfield, MO 65897|efactory.missouristate.edu
    Mostly Serious Interactive Agency|(417) 501-6552|4064 S Lone Pine Ave, Springfield, MO 65804|www.mostlyserious.io
    Ozarks Technical Community College||1001 E. Chestnut Expressway, Springfield, MO 65802|
    Pearson-Kelly Technology|(417) 877-0003|2013 W. Woodland, Springfield, MO 65807|www.pearsonkelly.com
    Pitt Technology Group, LLC|(417) 831-7077|1900 LeCompte, Building 15, Springfield, MO 65802|www.pitttechnologygroup.com
    """

    destinations_filename = 'events.dat'
    """
    SAMPLE EVENT LOCATION DATA
    
    202 S John Q Hammons Parkway, Springfield, MO 65806
    2340 W Grand St, Springfield, MO 65802
    2431 N Glenstone Ave, Springfield, MO 65803
    405 N Jefferson Ave, Springfield, MO 65806
    4155 S Nature Center Way, Springfield, MO 65804
    305 E Walnut St, Springfield, MO 65806
    1111 E Brookside Dr, Springfield, MO 65807
    600 W Sunshine, Springfield, MO 65807
    """

    destination_addresses = [destinations_line.rstrip('\n') for destinations_line in open(destinations_filename)]

    csv_lines = []
    deliminator = '|'

    # Construct CSV Header (title + each destination address)
    csv_line = 'Origin' + deliminator + deliminator.join(destination_addresses)
    csv_lines.append(csv_line)

    origins_lines = [origins_line.rstrip('\n') for origins_line in open(origins_filename)]
    for origins_line in origins_lines:
        origin_name, origin_phone, origin_address, origin_website = origins_line.split('|')
        drive_times = []

        print('Origin: ' + origin_address + '  ', end='')
        for destination_address in destination_addresses:
            drive_time = get_drive_time(api_key, origin_address, destination_address)
            drive_times.append(str(drive_time))
            print('.', end='')
            # flush output buffer so individual dots are displayed after each destination
            sys.stdout.flush()
        print()

        # Construct CSV Line (origin address + each destination drive time)
        csv_line = origin_address + deliminator + deliminator.join(drive_times)
        csv_lines.append(csv_line)

    csv_file = 'distance.csv'
    save_lines_to_file(csv_lines, csv_file)

    print('Distances saved to file: ' + csv_file)

    """
    SAMPLE OUTPUT DATA
    
    Origin|202 S John Q Hammons Parkway, Springfield, MO 65806|2340 W Grand St, Springfield, MO 65802|2431 N Glenstone Ave, Springfield, MO 65803|405 N Jefferson Ave, Springfield, MO 65806|4155 S Nature Center Way, Springfield, MO 65804|305 E Walnut St, Springfield, MO 65806|521 E St Louis St, Springfield, MO 65806|1111 E Brookside Dr, Springfield, MO 65807|333 S John Q Hammons Parkway, Springfield , MO 65806|600 W Sunshine, Springfield, MO 65807
    2500 E. Kearney, Springfield, MO 65898|751|1091|415|748|1037|858|780|881|779|1078
    5000 W. Kearney, Springfield, MO 65803|1077|811|798|946|1347|1038|1003|1279|1105|1097
    3725 E. Battlefield, Springfield, MO 65809|937|1135|894|978|492|1088|974|841|965|901
    601 N. National, Suite 102, Springfield, MO 65802|172|557|420|215|919|323|221|302|200|500
    1445 E. Republic, Springfield, MO 65804|846|860|1181|977|178|964|902|620|854|673
    901 S. National, Springfield, MO 65897|208|515|711|378|943|307|272|295|216|441
    4064 S Lone Pine Ave, Springfield, MO 65804|1028|1060|1192|1138|371|1122|1083|802|1036|862
    1001 E. Chestnut Expressway, Springfield, MO 65802|204|511|478|169|985|278|201|378|233|576
    2013 W. Woodland, Springfield, MO 65807|787|420|1051|671|595|643|733|585|795|330
    1900 LeCompte, Building 15, Springfield, MO 65802|737|1063|488|720|703|830|774|861|765|884
    """
