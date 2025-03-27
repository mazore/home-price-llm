city_data = [#_batch_one = [
    # Alabama
    ("Alabama", "Birmingham", "AL", "35203"), ("Alabama", "Montgomery", "AL", "36104"), ("Alabama", "Mobile", "AL", "36602"),
    ("Alabama", "Huntsville", "AL", "35801"), ("Alabama", "Tuscaloosa", "AL", "35401"), ("Alabama", "Hoover", "AL", "35244"),
    ("Alabama", "Dothan", "AL", "36301"), ("Alabama", "Auburn", "AL", "36830"), ("Alabama", "Decatur", "AL", "35601"),
    ("Alabama", "Madison", "AL", "35758"),
    # Alaska
    ("Alaska", "Anchorage", "AK", "99501"), ("Alaska", "Juneau", "AK", "99801"), ("Alaska", "Fairbanks", "AK", "99701"),
    ("Alaska", "Wasilla", "AK", "99654"), ("Alaska", "Sitka", "AK", "99835"), ("Alaska", "Ketchikan", "AK", "99901"),
    ("Alaska", "Kenai", "AK", "99611"), ("Alaska", "Kodiak", "AK", "99615"), ("Alaska", "Bethel", "AK", "99559"),
    ("Alaska", "Palmer", "AK", "99645"),
    # Arizona
    ("Arizona", "Phoenix", "AZ", "85001"), ("Arizona", "Tucson", "AZ", "85701"), ("Arizona", "Mesa", "AZ", "85201"),
    ("Arizona", "Chandler", "AZ", "85225"), ("Arizona", "Scottsdale", "AZ", "85251"), ("Arizona", "Gilbert", "AZ", "85234"),
    ("Arizona", "Glendale", "AZ", "85301"), ("Arizona", "Tempe", "AZ", "85281"), ("Arizona", "Peoria", "AZ", "85345"),
    ("Arizona", "Surprise", "AZ", "85374"),
    # Arkansas
    ("Arkansas", "Little Rock", "AR", "72201"), ("Arkansas", "Fort Smith", "AR", "72901"), ("Arkansas", "Fayetteville", "AR", "72701"),
    ("Arkansas", "Springdale", "AR", "72762"), ("Arkansas", "Jonesboro", "AR", "72401"), ("Arkansas", "Rogers", "AR", "72756"),
    ("Arkansas", "Conway", "AR", "72032"), ("Arkansas", "North Little Rock", "AR", "72114"), ("Arkansas", "Bentonville", "AR", "72712"),
    ("Arkansas", "Pine Bluff", "AR", "71601"),
    # California
    ("California", "Los Angeles", "CA", "90001"), ("California", "San Diego", "CA", "92101"), ("California", "San Jose", "CA", "95112"),
    ("California", "San Francisco", "CA", "94102"), ("California", "Fresno", "CA", "93722"), ("California", "Sacramento", "CA", "95814"),
    ("California", "Long Beach", "CA", "90802"), ("California", "Oakland", "CA", "94601"), ("California", "Bakersfield", "CA", "93309"),
    ("California", "Anaheim", "CA", "92801"),
    # Colorado
    ("Colorado", "Denver", "CO", "80202"), ("Colorado", "Colorado Springs", "CO", "80903"), ("Colorado", "Aurora", "CO", "80012"),
    ("Colorado", "Fort Collins", "CO", "80521"), ("Colorado", "Lakewood", "CO", "80226"), ("Colorado", "Thornton", "CO", "80229"),
    ("Colorado", "Arvada", "CO", "80002"), ("Colorado", "Westminster", "CO", "80031"), ("Colorado", "Pueblo", "CO", "81003"),
    ("Colorado", "Centennial", "CO", "80112"),
    # Connecticut
    ("Connecticut", "Bridgeport", "CT", "06604"), ("Connecticut", "New Haven", "CT", "06510"), ("Connecticut", "Stamford", "CT", "06901"),
    ("Connecticut", "Hartford", "CT", "06103"), ("Connecticut", "Waterbury", "CT", "06702"), ("Connecticut", "Norwalk", "CT", "06850"),
    ("Connecticut", "Danbury", "CT", "06810"), ("Connecticut", "New Britain", "CT", "06051"), ("Connecticut", "Meriden", "CT", "06450"),
    ("Connecticut", "Bristol", "CT", "06010"),
    # Delaware
    ("Delaware", "Wilmington", "DE", "19801"), ("Delaware", "Dover", "DE", "19901"), ("Delaware", "Newark", "DE", "19711"),
    ("Delaware", "Middletown", "DE", "19709"), ("Delaware", "Smyrna", "DE", "19977"), ("Delaware", "Milford", "DE", "19963"),
    ("Delaware", "Seaford", "DE", "19973"), ("Delaware", "Georgetown", "DE", "19947"), ("Delaware", "Elsmere", "DE", "19805"),
    ("Delaware", "New Castle", "DE", "19720"),
    # Florida
    ("Florida", "Jacksonville", "FL", "32202"), ("Florida", "Miami", "FL", "33101"), ("Florida", "Tampa", "FL", "33602"),
    ("Florida", "Orlando", "FL", "32801"), ("Florida", "St. Petersburg", "FL", "33701"), ("Florida", "Hialeah", "FL", "33010"),
    ("Florida", "Tallahassee", "FL", "32301"), ("Florida", "Fort Lauderdale", "FL", "33301"), ("Florida", "Port St. Lucie", "FL", "34952"),
    ("Florida", "Cape Coral", "FL", "33904"),
    # Georgia
    ("Georgia", "Atlanta", "GA", "30301"), ("Georgia", "Augusta", "GA", "30901"), ("Georgia", "Columbus", "GA", "31901"),
    ("Georgia", "Macon", "GA", "31201"), ("Georgia", "Savannah", "GA", "31401"), ("Georgia", "Athens", "GA", "30601"),
    ("Georgia", "Sandy Springs", "GA", "30328"), ("Georgia", "Roswell", "GA", "30075"), ("Georgia", "Albany", "GA", "31701"),
    ("Georgia", "Johns Creek", "GA", "30022"),
    # Hawaii
    ("Hawaii", "Honolulu", "HI", "96813"), ("Hawaii", "Hilo", "HI", "96720"), ("Hawaii", "Kailua", "HI", "96734"),
    ("Hawaii", "Kapolei", "HI", "96707"), ("Hawaii", "Waipahu", "HI", "96797"), ("Hawaii", "Kaneohe", "HI", "96744"),
    ("Hawaii", "Mililani", "HI", "96789"), ("Hawaii", "Kihei", "HI", "96753"), ("Hawaii", "Ewa Beach", "HI", "96706"),
    ("Hawaii", "Lahaina", "HI", "96761"),
    # Idaho
    ("Idaho", "Boise", "ID", "83702"), ("Idaho", "Meridian", "ID", "83642"), ("Idaho", "Nampa", "ID", "83651"),
    ("Idaho", "Idaho Falls", "ID", "83402"), ("Idaho", "Pocatello", "ID", "83201"), ("Idaho", "Caldwell", "ID", "83605"),
    ("Idaho", "Coeur d'Alene", "ID", "83814"), ("Idaho", "Twin Falls", "ID", "83301"), ("Idaho", "Lewiston", "ID", "83501"),
    ("Idaho", "Post Falls", "ID", "83854"),
    # Illinois
    ("Illinois", "Chicago", "IL", "60601"), ("Illinois", "Aurora", "IL", "60502"), ("Illinois", "Naperville", "IL", "60540"),
    ("Illinois", "Joliet", "IL", "60431"), ("Illinois", "Rockford", "IL", "61101"), ("Illinois", "Springfield", "IL", "62701"),
    ("Illinois", "Elgin", "IL", "60120"), ("Illinois", "Peoria", "IL", "61602"), ("Illinois", "Champaign", "IL", "61820"),
    ("Illinois", "Waukegan", "IL", "60085"),
    # Indiana
    ("Indiana", "Indianapolis", "IN", "46204"), ("Indiana", "Fort Wayne", "IN", "46802"), ("Indiana", "Evansville", "IN", "47708"),
    ("Indiana", "South Bend", "IN", "46601"), ("Indiana", "Carmel", "IN", "46032"), ("Indiana", "Bloomington", "IN", "47401"),
    ("Indiana", "Fishers", "IN", "46037"), ("Indiana", "Hammond", "IN", "46320"), ("Indiana", "Gary", "IN", "46402"),
    ("Indiana", "Muncie", "IN", "47303"),
    # Iowa
    ("Iowa", "Des Moines", "IA", "50309"), ("Iowa", "Cedar Rapids", "IA", "52401"), ("Iowa", "Davenport", "IA", "52801"),
    ("Iowa", "Sioux City", "IA", "51101"), ("Iowa", "Iowa City", "IA", "52240"), ("Iowa", "Waterloo", "IA", "50701"),
    ("Iowa", "Ames", "IA", "50010"), ("Iowa", "West Des Moines", "IA", "50265"), ("Iowa", "Council Bluffs", "IA", "51501"),
    ("Iowa", "Ankeny", "IA", "50021"),
    # Kansas
    ("Kansas", "Wichita", "KS", "67202"), ("Kansas", "Overland Park", "KS", "66204"), ("Kansas", "Kansas City", "KS", "66101"),
    ("Kansas", "Olathe", "KS", "66061"), ("Kansas", "Topeka", "KS", "66603"), ("Kansas", "Lawrence", "KS", "66044"),
    ("Kansas", "Shawnee", "KS", "66203"), ("Kansas", "Manhattan", "KS", "66502"), ("Kansas", "Lenexa", "KS", "66215"),
    ("Kansas", "Salina", "KS", "67401"),
    # Kentucky
    ("Kentucky", "Louisville", "KY", "40202"), ("Kentucky", "Lexington", "KY", "40507"), ("Kentucky", "Bowling Green", "KY", "42101"),
    ("Kentucky", "Owensboro", "KY", "42301"), ("Kentucky", "Covington", "KY", "41011"), ("Kentucky", "Richmond", "KY", "40475"),
    ("Kentucky", "Georgetown", "KY", "40324"), ("Kentucky", "Florence", "KY", "41042"), ("Kentucky", "Hopkinsville", "KY", "42240"),
    ("Kentucky", "Nicholasville", "KY", "40356"),
    # Louisiana
    ("Louisiana", "New Orleans", "LA", "70112"), ("Louisiana", "Baton Rouge", "LA", "70801"), ("Louisiana", "Shreveport", "LA", "71101"),
    ("Louisiana", "Lafayette", "LA", "70501"), ("Louisiana", "Lake Charles", "LA", "70601"), ("Louisiana", "Kenner", "LA", "70062"),
    ("Louisiana", "Bossier City", "LA", "71111"), ("Louisiana", "Monroe", "LA", "71201"), ("Louisiana", "Alexandria", "LA", "71301"),
    ("Louisiana", "Houma", "LA", "70360"),
    # Maine
    ("Maine", "Portland", "ME", "04101"), ("Maine", "Lewiston", "ME", "04240"), ("Maine", "Bangor", "ME", "04401"),
    ("Maine", "South Portland", "ME", "04106"), ("Maine", "Auburn", "ME", "04210"), ("Maine", "Biddeford", "ME", "04005"),
    ("Maine", "Sanford", "ME", "04073"), ("Maine", "Saco", "ME", "04072"), ("Maine", "Westbrook", "ME", "04092"),
    ("Maine", "Augusta", "ME", "04330"),
    # Maryland
    ("Maryland", "Baltimore", "MD", "21201"), ("Maryland", "Columbia", "MD", "21044"), ("Maryland", "Germantown", "MD", "20874"),
    ("Maryland", "Silver Spring", "MD", "20910"), ("Maryland", "Waldorf", "MD", "20601"), ("Maryland", "Frederick", "MD", "21701"),
    ("Maryland", "Ellicott City", "MD", "21042"), ("Maryland", "Glen Burnie", "MD", "21061"), ("Maryland", "Gaithersburg", "MD", "20877"),
    ("Maryland", "Rockville", "MD", "20850"),
    # Massachusetts
    ("Massachusetts", "Boston", "MA", "02108"), ("Massachusetts", "Worcester", "MA", "01608"), ("Massachusetts", "Springfield", "MA", "01103"),
    ("Massachusetts", "Lowell", "MA", "01850"), ("Massachusetts", "Cambridge", "MA", "02139"), ("Massachusetts", "New Bedford", "MA", "02740"),
    ("Massachusetts", "Brockton", "MA", "02301"), ("Massachusetts", "Quincy", "MA", "02169"), ("Massachusetts", "Lynn", "MA", "01901"),
    ("Massachusetts", "Fall River", "MA", "02720"),
    # Michigan
    ("Michigan", "Detroit", "MI", "48201"), ("Michigan", "Grand Rapids", "MI", "49503"), ("Michigan", "Warren", "MI", "48089"),
    ("Michigan", "Sterling Heights", "MI", "48310"), ("Michigan", "Ann Arbor", "MI", "48103"), ("Michigan", "Lansing", "MI", "48906"),
    ("Michigan", "Flint", "MI", "48502"), ("Michigan", "Dearborn", "MI", "48126"), ("Michigan", "Livonia", "MI", "48150"),
    ("Michigan", "Westland", "MI", "48185"),
    # Minnesota
    ("Minnesota", "Minneapolis", "MN", "55401"), ("Minnesota", "Saint Paul", "MN", "55101"), ("Minnesota", "Rochester", "MN", "55901"),
    ("Minnesota", "Duluth", "MN", "55802"), ("Minnesota", "Bloomington", "MN", "55420"), ("Minnesota", "Brooklyn Park", "MN", "55443"),
    ("Minnesota", "Plymouth", "MN", "55447"), ("Minnesota", "Maple Grove", "MN", "55369"), ("Minnesota", "Woodbury", "MN", "55125"),
    ("Minnesota", "St. Cloud", "MN", "56301"),
    # Mississippi
    ("Mississippi", "Jackson", "MS", "39201"), ("Mississippi", "Gulfport", "MS", "39501"), ("Mississippi", "Southaven", "MS", "38671"),
    ("Mississippi", "Biloxi", "MS", "39530"), ("Mississippi", "Hattiesburg", "MS", "39401"), ("Mississippi", "Olive Branch", "MS", "38654"),
    ("Mississippi", "Tupelo", "MS", "38801"), ("Mississippi", "Meridian", "MS", "39301"), ("Mississippi", "Greenville", "MS", "38701"),
    ("Mississippi", "Horn Lake", "MS", "38637"),
    # Missouri
    ("Missouri", "Kansas City", "MO", "64106"), ("Missouri", "St. Louis", "MO", "63101"), ("Missouri", "Springfield", "MO", "65806"),
# ]
# city_data = [
    ("Missouri", "Columbia", "MO", "65201"), ("Missouri", "Independence", "MO", "64050"), ("Missouri", "Lee's Summit", "MO", "64063"),
    ("Missouri", "O'Fallon", "MO", "63366"), ("Missouri", "St. Joseph", "MO", "64501"), ("Missouri", "St. Charles", "MO", "63301"),
    ("Missouri", "Blue Springs", "MO", "64014"),
    # Montana
    ("Montana", "Billings", "MT", "59101"), ("Montana", "Missoula", "MT", "59801"), ("Montana", "Great Falls", "MT", "59401"),
    ("Montana", "Bozeman", "MT", "59715"), ("Montana", "Butte", "MT", "59701"), ("Montana", "Helena", "MT", "59601"),
    ("Montana", "Kalispell", "MT", "59901"), ("Montana", "Havre", "MT", "59501"), ("Montana", "Anaconda", "MT", "59711"),
    ("Montana", "Miles City", "MT", "59301"),
    # Nebraska
    ("Nebraska", "Omaha", "NE", "68102"), ("Nebraska", "Lincoln", "NE", "68508"), ("Nebraska", "Bellevue", "NE", "68005"),
    ("Nebraska", "Grand Island", "NE", "68801"), ("Nebraska", "Kearney", "NE", "68845"), ("Nebraska", "Fremont", "NE", "68025"),
    ("Nebraska", "Hastings", "NE", "68901"), ("Nebraska", "North Platte", "NE", "69101"), ("Nebraska", "Norfolk", "NE", "68701"),
    ("Nebraska", "Columbus", "NE", "68601"),
    # Nevada
    ("Nevada", "Las Vegas", "NV", "89101"), ("Nevada", "Henderson", "NV", "89002"), ("Nevada", "Reno", "NV", "89501"),
    ("Nevada", "North Las Vegas", "NV", "89030"), ("Nevada", "Sparks", "NV", "89431"), ("Nevada", "Carson City", "NV", "89701"),
    ("Nevada", "Fernley", "NV", "89408"), ("Nevada", "Elko", "NV", "89801"), ("Nevada", "Mesquite", "NV", "89027"),
    ("Nevada", "Boulder City", "NV", "89005"),
    # New Hampshire
    ("New Hampshire", "Manchester", "NH", "03101"), ("New Hampshire", "Nashua", "NH", "03060"), ("New Hampshire", "Concord", "NH", "03301"),
    ("New Hampshire", "Derry", "NH", "03038"), ("New Hampshire", "Dover", "NH", "03820"), ("New Hampshire", "Rochester", "NH", "03867"),
    ("New Hampshire", "Salem", "NH", "03079"), ("New Hampshire", "Merrimack", "NH", "03054"), ("New Hampshire", "Hudson", "NH", "03051"),
    ("New Hampshire", "Londonderry", "NH", "03053"),
    # New Jersey
    ("New Jersey", "Newark", "NJ", "07102"), ("New Jersey", "Jersey City", "NJ", "07302"), ("New Jersey", "Paterson", "NJ", "07501"),
    ("New Jersey", "Elizabeth", "NJ", "07201"), ("New Jersey", "Edison", "NJ", "08817"), ("New Jersey", "Woodbridge", "NJ", "07095"),
    ("New Jersey", "Lakewood", "NJ", "08701"), ("New Jersey", "Toms River", "NJ", "08753"), ("New Jersey", "Hamilton", "NJ", "08610"),
    ("New Jersey", "Trenton", "NJ", "08608"),
    # New Mexico
    ("New Mexico", "Albuquerque", "NM", "87101"), ("New Mexico", "Las Cruces", "NM", "88001"), ("New Mexico", "Rio Rancho", "NM", "87124"),
    ("New Mexico", "Santa Fe", "NM", "87501"), ("New Mexico", "Roswell", "NM", "88201"), ("New Mexico", "Farmington", "NM", "87401"),
    ("New Mexico", "Clovis", "NM", "88101"), ("New Mexico", "Hobbs", "NM", "88240"), ("New Mexico", "Alamogordo", "NM", "88310"),
    ("New Mexico", "Carlsbad", "NM", "88220"),
    # New York
    ("New York", "New York City", "NY", "10001"), ("New York", "Buffalo", "NY", "14201"), ("New York", "Rochester", "NY", "14604"),
    ("New York", "Yonkers", "NY", "10701"), ("New York", "Syracuse", "NY", "13202"), ("New York", "Albany", "NY", "12207"),
    ("New York", "New Rochelle", "NY", "10801"), ("New York", "Mount Vernon", "NY", "10550"), ("New York", "Schenectady", "NY", "12305"),
    ("New York", "Utica", "NY", "13501"),
    # North Carolina
    ("North Carolina", "Charlotte", "NC", "28202"), ("North Carolina", "Raleigh", "NC", "27601"), ("North Carolina", "Greensboro", "NC", "27401"),
    ("North Carolina", "Durham", "NC", "27701"), ("North Carolina", "Winston-Salem", "NC", "27101"), ("North Carolina", "Fayetteville", "NC", "28301"),
    ("North Carolina", "Cary", "NC", "27511"), ("North Carolina", "Wilmington", "NC", "28401"), ("North Carolina", "High Point", "NC", "27260"),
    ("North Carolina", "Asheville", "NC", "28801"),
    # North Dakota
    ("North Dakota", "Fargo", "ND", "58102"), ("North Dakota", "Bismarck", "ND", "58501"), ("North Dakota", "Grand Forks", "ND", "58201"),
    ("North Dakota", "Minot", "ND", "58701"), ("North Dakota", "West Fargo", "ND", "58078"), ("North Dakota", "Williston", "ND", "58801"),
    ("North Dakota", "Dickinson", "ND", "58601"), ("North Dakota", "Mandan", "ND", "58554"), ("North Dakota", "Jamestown", "ND", "58401"),
    ("North Dakota", "Wahpeton", "ND", "58075"),
    # Ohio
    ("Ohio", "Columbus", "OH", "43215"), ("Ohio", "Cleveland", "OH", "44101"), ("Ohio", "Cincinnati", "OH", "45202"),
    ("Ohio", "Toledo", "OH", "43604"), ("Ohio", "Akron", "OH", "44308"), ("Ohio", "Dayton", "OH", "45402"),
    ("Ohio", "Parma", "OH", "44129"), ("Ohio", "Canton", "OH", "44702"), ("Ohio", "Youngstown", "OH", "44503"),
    ("Ohio", "Lorain", "OH", "44052"),
    # Oklahoma
    ("Oklahoma", "Oklahoma City", "OK", "73102"), ("Oklahoma", "Tulsa", "OK", "74103"), ("Oklahoma", "Norman", "OK", "73069"),
    ("Oklahoma", "Broken Arrow", "OK", "74012"), ("Oklahoma", "Edmond", "OK", "73013"), ("Oklahoma", "Lawton", "OK", "73501"),
    ("Oklahoma", "Moore", "OK", "73160"), ("Oklahoma", "Midwest City", "OK", "73110"), ("Oklahoma", "Enid", "OK", "73701"),
    ("Oklahoma", "Stillwater", "OK", "74074"),
    # Oregon
    ("Oregon", "Portland", "OR", "97201"), ("Oregon", "Salem", "OR", "97301"), ("Oregon", "Eugene", "OR", "97401"),
    ("Oregon", "Gresham", "OR", "97030"), ("Oregon", "Hillsboro", "OR", "97123"), ("Oregon", "Beaverton", "OR", "97005"),
    ("Oregon", "Bend", "OR", "97701"), ("Oregon", "Medford", "OR", "97501"), ("Oregon", "Springfield", "OR", "97477"),
    ("Oregon", "Corvallis", "OR", "97330"),
    # Pennsylvania
    ("Pennsylvania", "Philadelphia", "PA", "19104"), ("Pennsylvania", "Pittsburgh", "PA", "15222"), ("Pennsylvania", "Allentown", "PA", "18102"),
    ("Pennsylvania", "Erie", "PA", "16501"), ("Pennsylvania", "Reading", "PA", "19601"), ("Pennsylvania", "Scranton", "PA", "18503"),
    ("Pennsylvania", "Bethlehem", "PA", "18018"), ("Pennsylvania", "Lancaster", "PA", "17602"), ("Pennsylvania", "Harrisburg", "PA", "17101"),
    ("Pennsylvania", "York", "PA", "17401"),
    # Rhode Island
    ("Rhode Island", "Providence", "RI", "02903"), ("Rhode Island", "Cranston", "RI", "02910"), ("Rhode Island", "Warwick", "RI", "02886"),
    ("Rhode Island", "Pawtucket", "RI", "02860"), ("Rhode Island", "East Providence", "RI", "02914"), ("Rhode Island", "Woonsocket", "RI", "02895"),
    ("Rhode Island", "Coventry", "RI", "02816"), ("Rhode Island", "Cumberland", "RI", "02864"), ("Rhode Island", "North Providence", "RI", "02911"),
    ("Rhode Island", "West Warwick", "RI", "02893"),
    # South Carolina
    ("South Carolina", "Columbia", "SC", "29201"), ("South Carolina", "Charleston", "SC", "29401"), ("South Carolina", "North Charleston", "SC", "29405"),
    ("South Carolina", "Mount Pleasant", "SC", "29464"), ("South Carolina", "Rock Hill", "SC", "29730"), ("South Carolina", "Greenville", "SC", "29601"),
    ("South Carolina", "Summerville", "SC", "29483"), ("South Carolina", "Goose Creek", "SC", "29445"), ("South Carolina", "Sumter", "SC", "29150"),
    ("South Carolina", "Hilton Head Island", "SC", "29926"),
    # South Dakota
    ("South Dakota", "Sioux Falls", "SD", "57104"), ("South Dakota", "Rapid City", "SD", "57701"), ("South Dakota", "Aberdeen", "SD", "57401"),
    ("South Dakota", "Brookings", "SD", "57006"), ("South Dakota", "Watertown", "SD", "57201"), ("South Dakota", "Mitchell", "SD", "57301"),
    ("South Dakota", "Yankton", "SD", "57078"), ("South Dakota", "Pierre", "SD", "57501"), ("South Dakota", "Huron", "SD", "57350"),
    ("South Dakota", "Vermillion", "SD", "57069"),
    # Tennessee
    ("Tennessee", "Nashville", "TN", "37201"), ("Tennessee", "Memphis", "TN", "38103"), ("Tennessee", "Knoxville", "TN", "37902"),
    ("Tennessee", "Chattanooga", "TN", "37402"), ("Tennessee", "Clarksville", "TN", "37040"), ("Tennessee", "Murfreesboro", "TN", "37130"),
    ("Tennessee", "Franklin", "TN", "37064"), ("Tennessee", "Jackson", "TN", "38301"), ("Tennessee", "Johnson City", "TN", "37601"),
    ("Tennessee", "Bartlett", "TN", "38134"),
    # Texas
    ("Texas", "Houston", "TX", "77002"), ("Texas", "San Antonio", "TX", "78205"), ("Texas", "Dallas", "TX", "75201"),
    ("Texas", "Austin", "TX", "78701"), ("Texas", "Fort Worth", "TX", "76102"), ("Texas", "El Paso", "TX", "79901"),
    ("Texas", "Arlington", "TX", "76010"), ("Texas", "Corpus Christi", "TX", "78401"), ("Texas", "Plano", "TX", "75024"),
    ("Texas", "Laredo", "TX", "78040"),
    # Utah
    ("Utah", "Salt Lake City", "UT", "84101"), ("Utah", "West Valley City", "UT", "84119"), ("Utah", "Provo", "UT", "84601"),
    ("Utah", "West Jordan", "UT", "84084"), ("Utah", "Orem", "UT", "84057"), ("Utah", "Sandy", "UT", "84070"),
    ("Utah", "St. George", "UT", "84770"), ("Utah", "Layton", "UT", "84041"), ("Utah", "Taylorsville", "UT", "84129"),
    ("Utah", "Lehi", "UT", "84043"),
    # Vermont
    ("Vermont", "Burlington", "VT", "05401"), ("Vermont", "South Burlington", "VT", "05403"), ("Vermont", "Rutland", "VT", "05701"),
    ("Vermont", "Barre", "VT", "05641"), ("Vermont", "Montpelier", "VT", "05602"), ("Vermont", "Winooski", "VT", "05404"),
    ("Vermont", "St. Albans", "VT", "05478"), ("Vermont", "Newport", "VT", "05855"), ("Vermont", "Vergennes", "VT", "05491"),
    ("Vermont", "St. Johnsbury", "VT", "05819"),
    # Virginia
    ("Virginia", "Virginia Beach", "VA", "23451"), ("Virginia", "Norfolk", "VA", "23510"), ("Virginia", "Chesapeake", "VA", "23320"),
    ("Virginia", "Richmond", "VA", "23219"), ("Virginia", "Newport News", "VA", "23607"), ("Virginia", "Alexandria", "VA", "22314"),
    ("Virginia", "Hampton", "VA", "23669"), ("Virginia", "Roanoke", "VA", "24011"), ("Virginia", "Portsmouth", "VA", "23704"),
    ("Virginia", "Suffolk", "VA", "23434"),
    # Washington
    ("Washington", "Seattle", "WA", "98101"), ("Washington", "Spokane", "WA", "99201"), ("Washington", "Tacoma", "WA", "98402"),
    ("Washington", "Vancouver", "WA", "98660"), ("Washington", "Bellevue", "WA", "98004"), ("Washington", "Kent", "WA", "98032"),
    ("Washington", "Everett", "WA", "98201"), ("Washington", "Renton", "WA", "98057"), ("Washington", "Yakima", "WA", "98901"),
    ("Washington", "Spokane Valley", "WA", "99206"),
    # West Virginia
    ("West Virginia", "Charleston", "WV", "25301"), ("West Virginia", "Huntington", "WV", "25701"), ("West Virginia", "Morgantown", "WV", "26505"),
    ("West Virginia", "Parkersburg", "WV", "26101"), ("West Virginia", "Wheeling", "WV", "26003"), ("West Virginia", "Weirton", "WV", "26062"),
    ("West Virginia", "Fairmont", "WV", "26554"), ("West Virginia", "Martinsburg", "WV", "25401"), ("West Virginia", "Beckley", "WV", "25801"),
    ("West Virginia", "Clarksburg", "WV", "26301"),
    # Wisconsin
    ("Wisconsin", "Milwaukee", "WI", "53202"), ("Wisconsin", "Madison", "WI", "53703"), ("Wisconsin", "Green Bay", "WI", "54301"),
    ("Wisconsin", "Kenosha", "WI", "53140"), ("Wisconsin", "Racine", "WI", "53403"), ("Wisconsin", "Appleton", "WI", "54911"),
    ("Wisconsin", "Waukesha", "WI", "53186"), ("Wisconsin", "Eau Claire", "WI", "54701"), ("Wisconsin", "Oshkosh", "WI", "54901"),
    ("Wisconsin", "Janesville", "WI", "53545"),
    # Wyoming
    ("Wyoming", "Cheyenne", "WY", "82001"), ("Wyoming", "Casper", "WY", "82601"), ("Wyoming", "Laramie", "WY", "82070"),
    ("Wyoming", "Gillette", "WY", "82716"), ("Wyoming", "Rock Springs", "WY", "82901"), ("Wyoming", "Sheridan", "WY", "82801"),
    ("Wyoming", "Green River", "WY", "82935"), ("Wyoming", "Evanston", "WY", "82930"), ("Wyoming", "Riverton", "WY", "82501"),
    ("Wyoming", "Cody", "WY", "82414")
]
