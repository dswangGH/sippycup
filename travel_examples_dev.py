from example import Example

travel_dev_examples = [
    Example(input='airfare from san angelo tx to shreveport la',
            semantics={'domain': 'travel',
                       'origin': {'id': 5530022, 'name': 'San Angelo, TX, US'},
                       'destination': {'id': 4341513, 'name': 'Shreveport, LA, US'},
                       'mode': 'air'}),
    Example(input='direct flights from cincinnati to panama city pty',
            semantics={'domain': 'travel',
                       'origin': {'id': 4508722, 'name': 'Cincinnati, OH, US'},
                       'destination': {'id': 3700562, 'name': 'Tocumen International Airport, PA'},
                       'mode': 'air'}),
    Example(input='vancouver to seattle bus service',
            semantics={'domain': 'travel',
                       'origin': {'id': 6173331, 'name': 'Vancouver, CA'},
                       'destination': {'id': 5809844, 'name': 'Seattle, WA, US'},
                       'mode': 'bus'}),
    Example(input='car transport from florida to long island',
            semantics={'domain': 'travel',
                       'origin': {'id': 4155751, 'name': 'Florida, US'},
                       'destination': {'id': 5125123, 'name': 'Long Island, NY, US'},
                       'mode': 'car'}),
    Example(input='newark to san francisco flight deals',
            semantics={'domain': 'travel',
                       'origin': {'id': 5101798, 'name': 'Newark, NJ, US'},
                       'destination': {'id': 5391959, 'name': 'San Francisco, CA, US'},
                       'mode': 'air'}),
    Example(input='train travel chicago to los angles',
            semantics={'domain': 'travel',
                       'origin': {'id': 4887398, 'name': 'Chicago, IL, US'},
                       'destination': {'id': 5368361, 'name': 'Los Angeles, CA, US'},
                       'mode': 'train'}),
    Example(input='where to buy cigarettes from western new york state',
            semantics={'domain': 'other'}),
    Example(input='lakefront chartered bus trips schedule to detroit casinos',
            semantics={'domain': 'travel',
                       'destination': {'id': 4990729, 'name': 'Detroit, MI, US'},
                       'mode': 'bus'}),
    Example(input='cruises from philadelphia',
            semantics={'domain': 'travel',
                       'origin': {'id': 4560349, 'name': 'Philadelphia, PA, US'},
                       'mode': 'boat'}),
    Example(input='san francisco plane flights to christchurch new zealand',
            semantics={'domain': 'travel',
                       'origin': {'id': 5391959, 'name': 'San Francisco, CA, US'},
                       'destination': {'id': 2192362, 'name': 'Christchurch, NZ'},
                       'mode': 'plane'}),
    Example(input='nonstop flight direct flight to greece from boston or nyc',
            semantics={'domain': 'travel',
                       'mode': 'air',
                       'destination': {'id': 390903, 'name': 'Greece'},
                       'origin': {'id': 4930956, 'name': 'Boston, MA, US'}}),
    Example(input='i have no time on my cell need code to enter so it will give me time on my t mobile',
            semantics={'domain': 'other'}),
    Example(input='alaska flights sfo to palm springs',
            semantics={'domain': 'travel',
                       'origin': {'id': 5391989, 'name': 'San Francisco International Airport, CA, US'},
                       'destination': {'id': 5380668, 'name': 'Palm Springs, CA, US'},
                       'mode': 'air'}),
    Example(input='bus service to washington',
            semantics={'domain': 'travel',
                       'destination': {'id': 4140963, 'name': 'Washington, DC, US'},
                       'mode': 'bus'}),
    Example(input='codes to enter for t mobile for free time',
            semantics={'domain': 'other'}),
    Example(input='bus to boston',
            semantics={'domain': 'travel',
                       'destination': {'id': 4930956, 'name': 'Boston, MA, US'},
                       'mode': 'bus'}),
    Example(input='how long to see alj judge for ssdi in wilmington de',
            semantics={'domain': 'other'}),
    Example(input='bus tours from charleston sc',
            semantics={'domain': 'travel',
                       'origin': {'id': 4574324, 'name': 'Charleston, SC, US'},
                       'mode': 'bus'}),
    Example(input='travel columbus ohio to las vegas nv.',
            semantics={'domain': 'travel',
                       'origin': {'id': 4509177, 'name': 'Columbus, OH, US'},
                       'destination': {'id': 5506956, 'name': 'Las Vegas, NV, US'}}),
    Example(input='cheap flights to st.lucia to new york',
            semantics={'domain': 'travel',
                       'origin': {'id': 5128581, 'name': 'New York, US'},
                       'destination': {'id': 3576468, 'name': 'Saint Lucia'},
                       'mode': 'air'}),
    Example(input='cheap flights to florida',
            semantics={'domain': 'travel',
                       'destination': {'id': 4155751, 'name': 'Florida, US'},
                       'mode': 'air'}),
    Example(input='how long does it take to see the alj judge in a disability claim in state of delaware',
            semantics={'domain': 'other'}),
    Example(input='bus norfolk to philly',
            semantics={'domain': 'travel',
                       'origin': {'id': 4776222, 'name': 'Norfolk, VA, US'},
                       'destination': {'id': 4560349, 'name': 'Philadelphia, PA, US'},
                       'mode': 'bus'}),
    Example(input='how long does it take to get to the bahamas from new york',
            semantics={'domain': 'travel',
                       'origin': {'id': 5128581, 'name': 'New York, US'},
                       'destination': {'id': 3572887, 'name': 'Bahamas'},
                       'type': 'schedule'}),
    Example(input='flight ticket cheap from albany ny to germany frankfurt',
            semantics={'domain': 'travel',
                       'origin': {'id': 5106834, 'name': 'Albany, NY, US'},
                       'destination': {'id': 2925533, 'name': 'Frankfurt am Main, DE'},
                       'mode': 'air'}),
    Example(input='t mobile code to use to add time',
            semantics={'domain': 'other'}),
    Example(input='trains from boston to philadelphia',
            semantics={'domain': 'travel',
                       'origin': {'id': 4930956, 'name': 'Boston, MA, US'},
                       'destination': {'id': 4560349, 'name': 'Philadelphia, PA, US'},
                       'mode': 'train'}),
    Example(input='www.fun places to fly .com asap event state texas',
            semantics={'domain': 'other'}),
    Example(input='bus to foxwood from fall river',
            semantics={'domain': 'travel',
                       'origin': {'id': 4936159, 'name': 'Fall River, MA, US'},
                       'destination': {'id': 4834737, 'name': 'Foxwoods Casino, CT, US'},
                       'mode': 'bus'}),
    Example(input='flights from tampa to seattle',
            semantics={'domain': 'travel',
                       'origin': {'id': 4174757, 'name': 'Tampa, FL, US'},
                       'destination': {'id': 5809844, 'name': 'Seattle, WA, US'},
                       'mode': 'air'}),
    Example(input='best time of year to cruise alaska',
            semantics={'domain': 'other'}),
    Example(input='travel from broad and jersey st in elizabeth nj to385 tremont ave east orange nj',
            semantics={'domain': 'travel',
                       'origin': {'id': 5097598, 'name': 'Elizabeth, NJ, US'},
                       'destination': {'id': 5097441, 'name': 'East Orange, NJ, US'}}),
    Example(input='directions to hartsfield jackson international airport',
            semantics={'domain': 'travel',
                       'destination': {'id': 4199556, 'name': 'HartsfieldJackson Atlanta International Airport, GA, US'},
                       'type': 'directions'}),
    Example(input='cheap flights to atlanta',
            semantics={'domain': 'travel',
                       'destination': {'id': 4180439, 'name': 'Atlanta, GA, US'},
                       'mode': 'air'}),
    Example(input='how long is it taking to receive the state of illinois tax return checks',
            semantics={'domain': 'other'}),
    Example(input='directions to garinger high school north carolina',
            semantics={'domain': 'travel',
                       'destination': {'id': 4467643, 'name': 'Garinger High School, NC, US'},
                       'type': 'directions'}),
    Example(input='maxwell hu. 1899. the history of barbour county west virginia from its earliest exploration and settlement to the present time',
            semantics={'domain': 'other'}),
    Example(input='lax airport transportation to riverside california',
            semantics={'domain': 'travel',
                       'origin': {'id': 5368418, 'name': 'Los Angeles International Airport, CA, US'},
                       'destination': {'id': 5368361, 'name': 'Los Angeles, CA, US'}}),
    Example(input='bus lines from las vegas nevada to los angeles california',
            semantics={'domain': 'travel',
                       'origin': {'id': 5506956, 'name': 'Las Vegas, NV, US'},
                       'destination': {'id': 5368361, 'name': 'Los Angeles, CA, US'},
                       'mode': 'bus'}),
    Example(input='cheap flights from rochester to tampa',
            semantics={'domain': 'travel',
                       'origin': {'id': 5134086, 'name': 'Rochester, NY, US'},
                       'destination': {'id': 4174757, 'name': 'Tampa, FL, US'},
                       'mode': 'air'}),
    Example(input='telephone calling cards from bahamas to usa',
            semantics={'domain': 'other'}),
    Example(input='travel to new york city',
            semantics={'domain': 'travel',
                       'destination': {'id': 5128581, 'name': 'New York, US'}}),
    Example(input='black and white porn from the 1930 to the 1950 literotica',
            semantics={'domain': 'other'}),
    Example(input='new jersey transit to long branch',
            semantics={'domain': 'travel',
                       'destination': {'id': 5100619, 'name': 'Long Branch, NJ, US'}}),
    Example(input='cheap fares from montana',
            semantics={'domain': 'travel',
                       'origin': {'id': 5667009, 'name': 'Montana, US'},
                       'mode': 'air'}),
    Example(input='shortest route from avon mass. to nashville tenneessee.',
            semantics={'domain': 'travel',
                       'origin': {'id': 4929476, 'name': 'Avon, MA, US'},
                       'destination': {'id': 4644585, 'name': 'Nashville, TN, US'},
                       'type': 'directions'}),
    Example(input='directions to copper hill country club ringoes new jersey',
            semantics={'domain': 'travel',
                       'destination': {'id': 5096943, 'name': 'Copper Hill Country Club, NJ, US'},
                       'type': 'directions'}),
    Example(input='travel to noth georgia',
            semantics={'domain': 'travel',
                       'destination': {'id': 4197000, 'name': 'Georgia, US'}}),
    Example(input='airfare to athens greece from boston',
            semantics={'domain': 'travel',
                       'origin': {'id': 4930956, 'name': 'Boston, MA, US'},
                       'destination': {'id': 264371, 'name': 'Athens, GR'},
                       'mode': 'air'}),
    Example(input='instructions from 4313 verde vista-georgetwown tx to nearest motel in branson missouri',
            semantics={'domain': 'travel',
                       'origin': {'id': 4693342, 'name': 'Georgetown, TX, US'},
                       'destination': {'id': 4378219, 'name': 'Branson, MO, US'},
                       'type': 'directions'}),
    Example(input='car shipping from new orleans',
            semantics={'domain': 'other'}),
    Example(input='how to grow red maples from seed',
            semantics={'domain': 'other'}),
    Example(input='bus from new york to pennsylvania',
            semantics={'domain': 'travel',
                       'origin': {'id': 5128581, 'name': 'New York, US'},
                       'destination': {'id': 6254927, 'name': 'Pennsylvania, US'},
                       'mode': 'bus'}),
    Example(input='cheap tickets to florida',
            semantics={'domain': 'travel',
                       'destination': {'id': 4155751, 'name': 'Florida, US'},
                       'mode': 'air'}),
    Example(input='cheap air fare to chicago',
            semantics={'domain': 'travel',
                       'destination': {'id': 4887398, 'name': 'Chicago, IL, US'},
                       'mode': 'air'}),
    Example(input='airfare to orlando',
            semantics={'domain': 'travel',
                       'destination': {'id': 4167147, 'name': 'Orlando, FL, US'},
                       'mode': 'air'}),
    Example(input='best time to cruise alaska',
            semantics={'domain': 'other'}),
    Example(input='directions to east boston high school softball field',
            semantics={'domain': 'travel',
                       'destination': {'id': 4935306, 'name': 'East Boston High School, MA, US'},
                       'type': 'directions'}),
    Example(input='last minute cheap flights newark nj to san francisco ca',
            semantics={'domain': 'travel',
                       'origin': {'id': 5101798, 'name': 'Newark, NJ, US'},
                       'destination': {'id': 5391959, 'name': 'San Francisco, CA, US'},
                       'mode': 'air'}),
    Example(input='cruises from baltimore',
            semantics={'domain': 'travel',
                       'origin': {'id': 4347778, 'name': 'Baltimore, MD, US'},
                       'mode': 'boat'}),
    Example(input='1 day cruises from the port of miami to the bahamas',
            semantics={'domain': 'travel',
                       'origin': {'id': 4164181, 'name': 'Miami International Airport, FL, US'},
                       'destination': {'id': 3572887, 'name': 'Bahamas'},
                       'mode': 'boat'}),
    Example(input='tickets to memphis redbirds',
            semantics={'domain': 'other'}),
    Example(input='view recent mail to or from buddy list member houston',
            semantics={'domain': 'other'}),
    Example(input='from trenton ga to niceville fla',
            semantics={'domain': 'travel',
                       'origin': {'id': 4227012, 'name': 'Trenton, GA, US'},
                       'destination': {'id': 4165995, 'name': 'Niceville, FL, US'}}),
    Example(input='cruises from new orleans',
            semantics={'domain': 'travel',
                       'origin': {'id': 4335045, 'name': 'New Orleans, LA, US'},
                       'mode': 'boat'}),
    Example(input='cheap airline tickets to san francisco',
            semantics={'domain': 'travel',
                       'destination': {'id': 5391959, 'name': 'San Francisco, CA, US'},
                       'mode': 'air'}),
    Example(input='driving to maroon bells colorado',
            semantics={'domain': 'travel',
                       'destination': {'id': 5430143, 'name': 'Maroon Bells, CO, US'},
                       'mode': 'car'}),
    Example(input='flights from chicago to agadir',
            semantics={'domain': 'travel',
                       'origin': {'id': 4887398, 'name': 'Chicago, IL, US'},
                       'destination': {'id': 2542007, 'name': 'Morocco'},
                       'mode': 'air'}),
    Example(input='flights to hawaii',
            semantics={'domain': 'travel',
                       'destination': {'id': 5855797, 'name': 'Hawaii, US'},
                       'mode': 'air'}),
    Example(input='directions to levittown memorial',
            semantics={'domain': 'travel',
                       'destination': {'id': 7232808, 'name': 'Levittown Memorial Special Education Center, NY, US'},
                       'type': 'directions'}),
    Example(input='ferry vallejo to san francisco',
            semantics={'domain': 'travel',
                       'origin': {'id': 5405380, 'name': 'Vallejo, CA, US'},
                       'destination': {'id': 5391959, 'name': 'San Francisco, CA, US'},
                       'mode': 'boat'}),
    Example(input='flights to st. louis mo from new orleans la',
            semantics={'domain': 'travel',
                       'origin': {'id': 4335045, 'name': 'New Orleans, LA, US'},
                       'destination': {'id': 4407066, 'name': 'St Louis, MO, US'},
                       'mode': 'air'}),
    Example(input='michigan to wisconsin ferry service',
            semantics={'domain': 'travel',
                       'origin': {'id': 5001836, 'name': 'Michigan, US'},
                       'destination': {'id': 5279468, 'name': 'Wisconsin, US'},
                       'mode': 'boat'}),
    Example(input='how to remove green chlorine from hair',
            semantics={'domain': 'other'}),
    Example(input='a free people ought not only to be armed and disciplined but they should have sufficient arms and ammunition to maintain a status of independence from any who might attempt to abuse them which would include their own government.',
            semantics={'domain': 'other'}),
    Example(input='airfare to phoenix',
            semantics={'domain': 'travel',
                       'destination': {'id': 5308655, 'name': 'Phoenix, AZ, US'},
                       'mode': 'air'}),
    Example(input='flights newark to orlando',
            semantics={'domain': 'travel',
                       'origin': {'id': 5101798, 'name': 'Newark, NJ, US'},
                       'destination': {'id': 4167147, 'name': 'Orlando, FL, US'},
                       'mode': 'air'}),
    Example(input='shortest route from austin to lake charles',
            semantics={'domain': 'travel',
                       'origin': {'id': 4671654, 'name': 'Austin, TX, US'},
                       'destination': {'id': 4330236, 'name': 'Lake Charles, LA, US'},
                       'type': 'directions'}),
    Example(input='airfare to california',
            semantics={'domain': 'travel',
                       'destination': {'id': 5332921, 'name': 'California, US'},
                       'mode': 'air'}),
    Example(input='interstate toll fees for highway 80 from utah to pennsylvania for a semi truck',
            semantics={'domain': 'other'}),
    Example(input='airfare tucson to costa rica',
            semantics={'domain': 'travel',
                       'origin': {'id': 5318313, 'name': 'Tucson, AZ, US'},
                       'destination': {'id': 3624060, 'name': 'Costa Rica'},
                       'mode': 'air'}),
    Example(input='when is the best time to go to las vegas',
            semantics={'domain': 'other'}),
    Example(input='from 774 cedar ln. trenton ga. to 801 east john sims parkway. niceville fla',
            semantics={'domain': 'travel',
                       'origin': {'id': 4227012, 'name': 'Trenton, GA, US'},
                       'destination': {'id': 4165995, 'name': 'Niceville, FL, US'}}),
    Example(input='southwest airline on time schedule san antonio to baton rouge',
            semantics={'domain': 'travel',
                       'origin': {'id': 4726206, 'name': 'San Antonio, TX, US'},
                       'destination': {'id': 4315588, 'name': 'Baton Rouge, LA, US'},
                       'type': 'schedule'}),
    Example(input='all airlines with one-way flights from las vegas nv. to charlotte n.c.',
            semantics={'domain': 'travel',
                       'origin': {'id': 5506956, 'name': 'Las Vegas, NV, US'},
                       'destination': {'id': 4460243, 'name': 'Charlotte, NC, US'},
                       'mode': 'air'}),
    Example(input='cheap flights to athens greece from boston ma.',
            semantics={'domain': 'travel',
                       'origin': {'id': 4930956, 'name': 'Boston, MA, US'},
                       'destination': {'id': 264371, 'name': 'Athens, GR'},
                       'mode': 'air'}),
    Example(input='cheap flights to detroit michigan',
            semantics={'domain': 'travel',
                       'destination': {'id': 4990729, 'name': 'Detroit, MI, US'},
                       'mode': 'air'}),
    Example(input='driving directions from california to zacatecas',
            semantics={'domain': 'travel',
                       'origin': {'id': 5332921, 'name': 'California, US'},
                       'destination': {'id': 3979840, 'name': 'Zacatecas, MX'},
                       'mode': 'car',
                       'type': 'directions'}),
    Example(input='places to walk dog in st. louis mo',
            semantics={'domain': 'other'}),
    Example(input='airlines that fly to hawaii',
            semantics={'domain': 'other'}),
    Example(input='transfers from cassette to cd in new york city',
            semantics={'domain': 'other'}),
    Example(input='cheap flights to estonia from new york',
            semantics={'domain': 'travel',
                       'origin': {'id': 5128581, 'name': 'New York, US'},
                       'destination': {'id': 453733, 'name': 'Estonia'},
                       'mode': 'air'}),
    Example(input='white flight from black communities',
            semantics={'domain': 'other'}),
    Example(input='japanese red maple crimson queen large size to purchase from nursery',
            semantics={'domain': 'other'}),
    Example(input='distance from las vegas to palm springs',
            semantics={'domain': 'travel',
                       'origin': {'id': 5506956, 'name': 'Las Vegas, NV, US'},
                       'destination': {'id': 5380668, 'name': 'Palm Springs, CA, US'},
                       'type': 'distance'}),
    Example(input='cheapest place to live in michigan',
            semantics={'domain': 'other'}),
    Example(input='65\' aluminum crew boat to buy in louisiana',
            semantics={'domain': 'other'}),
    Example(input='san juan puerto rico ferry to st thomas',
            semantics={'domain': 'travel',
                       'origin': {'id': '', 'name': 'San Juan, PR'},
                       'destination': {'id': 3488688, 'name': 'Parish of Saint Thomas, JM'},
                       'mode': 'boat'}),
    Example(input='cheap flights to jackson ms',
            semantics={'domain': 'travel',
                       'destination': {'id': 4431410, 'name': 'Jackson, MS, US'},
                       'mode': 'air'}),
    Example(input='airfares for oneway non-stop flights from las vegas nv. to charlotte nc. with senior rate',
            semantics={'domain': 'travel',
                       'origin': {'id': 5506956, 'name': 'Las Vegas, NV, US'},
                       'destination': {'id': 4460243, 'name': 'Charlotte, NC, US'},
                       'mode': 'air'})
]
