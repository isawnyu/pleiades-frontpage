title: Places
creator: The Editors
description: You don't need a login to start searching, reading and using Pleiades information, but you do need one if you wish to contribute corrections and new content.
date: 2015-11-14
subjects: Geography, Ancient; Data, Geospatial; Places; Placenames; Toponyms; Locations; Coordinates
dctype:
language:
citation: 
url: places
ogtype:
ogimage: 

# Places

_Pleiades_ is a gazetteer of ancient places. At present, it has extensive coverage for the Greek and Roman world, and is expanding into Ancient Near Eastern, Byzantine, Celtic, Early Islamic, and Early Medieval geography.

## Key Concepts {: #concepts }

Information about ancient places in _Pleiades_ is organized differently from both traditional gazetteers and standard GIS datasets. [In our view](/docs/papers-and-presentations/whats-an-un-gis), neither an alphabetical list of placesnames nor a set of thematic layers is sufficiently flexible and rigorous to represent a complex, partial, and changing understanding of ancient geography. Instead, _Pleiades_ content is organized into three types of "information resource": _places_, _locations_, and _names_. Although some other projects have adopted this pattern since we introduced it, it remains uncommon; consequently, all but the most casual user will want to familiarize themselves with the distinctions between, and relationships among, these resources by reading the [Pleiades Data Structure document](help/data-structure).

*[GIS]: Geographic Information System

## Find and Use Content {: #use .section:pleiades-btn-panel }

All published information resources in _Pleiades_ are free and open to the public. No login is required. The following starting points will help you find the content you seek:

### [Search](/search) {: .btn .btn-lg .btn-primary .pleiades-btn-glossed }

[Visit our home page](/), click in the "search" box, and start typing a name, a _Pleiades_ ID, or a _Pleiades_ URI to see a list of possible matching _places_. As you type, the list automatically narrows, and thumbnail maps appear below. Click on the corresponding ID number or map icon to visit the appropriate _place_ page.

### [Advanced Search](/search_form) {: .btn .btn-lg .btn-primary .pleiades-btn-glossed }

[The Advanced Search page](/search_form) lets you construct more complex queries, but it can be much slower than the [Search](/search) page. See [Using Advanced Search](help/using-advanced-search) for tips.

### [Download](/downloads) {: .btn .btn-lg .btn-primary .pleiades-btn-glossed }

Regular exports of _Pleiades_ content can be [downloaded en masse in a number of formats](/downloads).

### [API](http://api.pleiades.stoa.org) {: .btn .btn-lg .btn-primary .pleiades-btn-glossed }

Interact programmatically with published content via our [Application Programming Interface](http://api.pleiades.stoa.org)

### [Indexes]() {: .btn .btn-lg .btn-primary .pleiades-btn-glossed .disabled }

The _Pleiades_ faceted indexes for _places_ and _names_ have been taken offline temporarily to improve site performance. They will be replaced as part of [a major technical upgrade](https://github.com/isawnyu/pleiades-gazetteer#pleiades-3) now underway. 

## A Request:<br />Please don't pummel our site {: .section:sidebar .section:dogear }

The _Pleiades_ website is presently undergoing [a major technical upgrade](https://github.com/isawnyu/pleiades-gazetteer#pleiades-3) to improve speed, performance, and reliability; however, at the present it remains vulnerable to excessively rapid and aggressively simultaneous usage. During this transitional period, we ask for your assistance in keeping the site stable and available to all.

### Humans

Please limit your browser interactions with the site to a single window or tab, especially when running advanced searches or waiting for slow pages (e.g., Athens, Rome) to load.

### Bots

Users of the [API](http://api.pleiades.stoa.org) should abide by the "crawl delay" and other directives in the [robots.txt file](/robots.txt). Please interpret a 500-series [HTTP status code](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) (particularly 503 or 504) as a request to refrain from additional HTTP requests for 15 minutes or more. Note that repeated violation of our [crawl-delay directive](https://en.wikipedia.org/wiki/Robots_exclusion_standard#Crawl-delay_directive) may result in your bot being banned (403 for all requests). If you think your bot has been banned in error, please email [pleiades.admin@nyu.edu] to start a conversation about the problem.

*[API]: Application Programming Interface
*[HTTP]: Hypertext Transfer Protocol
