#!/bin/bash

# These filters are used to prune the member list to Missouri cities only. The filters
# also exclude PO Boxes. You can include specific cities or exclude specific cities.
# 
# TIP: Combine the two statements to view a list of cities that do not appear on either list

# Include Specific Cities (e.g. within approximately one hour drive from Springfield MO)
grep ' MO ' members.dat | grep -v 'PO Box' | egrep '(Springfield|Joplin|Nixa|Ozark|Republic|Neosho|Branson|Bolivar|Battlefield|Rogersville|Willard|Clever|Strafford|Mt Vernon|Highlandville|Hollister|Monett|Brookline), MO' > members-prune.dat

# Exclude Specific Cities
#grep ' MO ' members.dat | grep -v 'PO Box' | egrep -v '(St. Louis|St Louis|Kansas City|Columbia|Jefferson City|Kirkwood|Overland Park|Maryland Heights|Eldon|Osage Beach|Eureka)' > members-prune.dat

rm members.dat
mv members-prune.dat members.dat

echo See Output: members.dat

