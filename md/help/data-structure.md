title: Pleiades Data Structure
creator: The Editors
description: 
date: 2015-11-14
subjects: Geography, Ancient; Data, Geospatial; 
dctype:
language:
citation: 
url: help/data-structure
ogtype:
ogimage: 

# Pleiades Data Structure

_Pleiades_ content is organized into three types of "information resource": _places_, _locations_, and _names_.

### Places

In _Pleiades_, _places_ are conceptual entities. They are objects of thought, speech, or writing, not tangible, mappable points on the earth’s surface. Even though they are usually tied closely to some aspect or feature of the physical world — a sea, a bay, a river, a mountain range, a pass, a road, a settlement, or an ethnic region — They have no spatial or temporal attributes of their own. Their primary quality is that, in the words of Yi-fu Tuan [1], they are "constructed by human experience."

A _place_ can be known only through a name mentioned an ancient source, without any surviving material correlate; conversely, an archaeological site can be understood as a _place_ even if we do not know what it was called in antiquity. Even a modern city known or presumed to be located atop an ancient settlement is a _place_ for _Pleiades_ purposes. Places may be no larger than a family dwelling or as big as an empire, be temporally enduring or fleeting. They may expand, contract and evolve over time. A place may be unnamed, unlocated, falsely attested or even mythical. 

### Locations and Names

The spatial aspects of _Pleiades_ _places_ (i.e., latitude and longitude coordinates), as well as their ancient and modern names, are addressed through two other conceptual entities: _locations_ and _names_.

_Locations_ connect _places_ to coordinates in space. A _location_ identifies a specific area of interest on the earth's surface that is associated with a _place_ during a particular date range. A _place_ can contain multiple _locations_. Depending on the state of the evidence, the association between _location_ and _place_ may vary in certainty; some _places_, attested by name in ancient sources, may have no associated _location_ at all because modern scholarship cannot pinpoint reliably the ancient site or area in question.

_Names_ are also connected with _places_. A _name_ reflects the identity of a _place_ in human language, not its physical location in the landscape. _Names_ have no spatial coordinates, but they are always annotated with the time period(s) of the textual source(s) in which they are attested. As with _locations_, a single _place_ can have multiple _names_, but an individual _name_ can be associated with one and only one _place_ (even if the same sequence of characters is attested as a _name_ for another _place_ as well).

### Database Structure

The _Pleiades_ system documents and describes each of these three conceptual entities using a corresponding "information resource". Information resources are bundles of structured data that are similar in function to records in a database or index cards in a card file. Each _place_ resource contains the _name_ and _location_ resources with which it is associated. This encapsulation is expressed in the layout of information on the _Pleiades_ website, and in the hierarchical structure of the Uniform Resource Identifiers (URIs: web addresses) _Pleiades_ assigns to each resource. Each _place_ resource has a corresponding web page in _Pleiades_, and each of these _place_ pages links to individual pages for all the _name_ and _location_ resources that have been associated with it. 

The structure and implementation of the _Pleiades_ database are described in more detail in the [Pleiades Data Model document](http://pleiades.stoa.org/help/pleiades-data-model).

### Example: Condercum

Consider the Roman fort of _Condercum_ (at modern Benwell, near Hadrian's Wall in the United Kingdom). _Pleiades_ has assigned the permanent identifying number 89150 to this conceptual place. Entering the _Pleiades_ URI [http://pleiades.stoa.org/places/89150] in a browser yields the corresponding _place_ page. Links to individual pages for the associated _locations_ ("Centerpoint of the ancient site", "Boundary of fort walls") and _names_ ("Benwell", "Condercum") are listed under the appropriate headings. The map on the _place_ page is derived from the contained _location_ resources.


