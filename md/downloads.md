# Downloads

## Exports

Regularly updated, abridged exports ("dumps") of the published items in the _Pleiades_ dataset may be downloaded in three different formats as described below. The on-line resources under [http://pleiades.stoa.org/places/] remain the canonical versions; the contents of the exports are not comprehensive. The [recently modified page](http://pleiades.stoa.org/recently_modified) or [its corresponding RSS feed](http://pleiades.stoa.org/news/changes/RSS) are the best ways to track what is changing.

### Comma-Separated Values (CSV)

Each morning, tables summarizing the published _locations_, _names_, and _places_ are written to compressed CSV files at [http://atlantides.org/downloads/pleiades/dumps/]. CSV is a widely used, well-known format that can be used by many computer programs. We keep a week's worth of files, deleting older ones. The files named `pleiades-*-latest.csv.gz` will always get you the most recent versions.

Users of these files will want to be aware of the following documentation:

*   The structure and contents of these files are documented in [a README file](http://atlantides.org/downloads/pleiades/dumps/README.txt).
*   We use [UTF-8 character encoding](https://en.wikipedia.org/wiki/UTF-8) for the text in these files. Some CSV readers (e.g., Microsoft Excel) assume or default to [ASCII encoding](https://en.wikipedia.org/wiki/ASCII) for CSV, which can lead to the mangling of Roman characters with diacritics as well as characters in non-Roman scripts.
*   We use the [gzip compression algorithm](https://en.wikipedia.org/wiki/Gzip) to reduce file size for download.
*   The CSV format is [well-documented on the Library of Congress _Digital Formats_ website](http://www.digitalpreservation.gov/formats/fdd/fdd000323.shtml "CSV format documentation from the Library of Congress").

### Keyhole Markup Language (KML)

Suitable for use in [Google Earth](https://www.google.com/earth/), [QGIS](http://www.qgis.org/en/site/), and other KML-capable software.

Information about all mappable _places_ are read from our database and written to a zipped KML (KMZ) file each morning. We keep a week's worth of files at [http://atlantides.org/downloads/pleiades/kml/] and delete older ones. The KML format is [well-documented on the Library of Congress _Digital Formats_ website](http://www.digitalpreservation.gov/formats/fdd/fdd000340.shtml "KML format documentation from the Library of Congress").

### Resource Description Framework (RDF)

The latest data for all _places_, _errata_, _authors_, _place types_, and _time periods_ is available for download in Turtle (Terse RDF Triple Language) via [http://atlantides.org/downloads/pleiades/rdf/pleiades-latest.tar.gz]. This is a gzip-compressed, TAR archive. Previous RDF dumps are also available at [http://atlantides.org/downloads/pleiades/rdf/]. RDF dumps are updated weekly on Sundays.

NB: RDF serializations of data for individual _places_ — in both Turtle and RDF/XML syntax — can be had from links on the place pages, such as [http://pleiades.stoa.org/places/579885/turtle] for Athens, or by a negotiated request for the resource [http://pleiades.stoa.org/places/579885#this]. Please see the [README](https://github.com/isawnyu/pleiades-rdf/blob/master/README.rst) in [https://github.com/isawnyu/pleiades-rdf] for a description of the RDF and the vocabularies and ontologies used.

## Derived and Enhanced Versions

### Pleiades Plus

_Pleiades Plus_ (also known as _Pleiades+_) is an experimental machine alignment between _Pleiades_ _place_ resources and content in the [GeoNames gazetteer](http://www.geonames.org/). It pairs [_Pleiades_ Uniform Resource Identifiers (URIs)](http://pleiades.stoa.org/help/what-are-pleiades-uris) with _GeoNames_ URIs when a given pair seems likely to identify the same place. This alignment was conceived and prototyped by Leif Isaksen ([Pelagios Project](http://pelagios-project.blogspot.com/)) under the auspices of the [Google Ancient Places project](http://googleancientplaces.wordpress.com/about/) (you can read [the original announcement from 2011 on the GAP Blog](http://googleancientplaces.wordpress.com/2011/01/24/pleiades-adapting-the-ancient-world-gazetteer-for-gap-%E2%80%93-by-leif-isaksen/)). The current version is produced daily by [Ryan Baumann](http://ryanfb.github.io/) ([Duke Collaboratory for Classics Computing](http://blogs.library.duke.edu/dcthree/)). Code and data are available from [https://github.com/ryanfb/pleiades-plus]. There is also [an essential README file](https://github.com/ryanfb/pleiades-plus/blob/master/README.md).
