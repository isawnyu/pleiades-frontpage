You are here: [Home](http://pleiades.stoa.org/home) →
[Help](http://pleiades.stoa.org/help) →  Pleiades Data Model

[Skip to content.](http://pleiades.stoa.org/help/pleiades-data-
model?from=tom.elliott%40nyu.edu&user-
agent=Paregoriosian%2F0.1#documentContent) | [Skip to
navigation](http://pleiades.stoa.org/help/pleiades-data-
model?from=tom.elliott%40nyu.edu&user-agent=Paregoriosian%2F0.1#portlet-
navigation-tree)

#  Pleiades Data Model

Creators: [Tom Elliott](/author/thomase) Copyright © The Contributors. Sharing
and remixing permitted under terms of the Creative Commons Attribution 3.0
License (cc-by).

Last modified  Apr 21, 2015 03:34 PM

tags:  [portlet:places](http://pleiades.stoa.org/search?Subject%3Alist=portlet
%3Aplaces),
[concept](http://pleiades.stoa.org/search?Subject%3Alist=concept),
[help](http://pleiades.stoa.org/search?Subject%3Alist=help)

This document provides an overview of the manner in which Pleiades content is
modeled in the database.

Pleiades uses an [object-relational
database](http://en.wikipedia.org/wiki/Object-relational_database) called Zope
to store its content. We make use of six classes for organizing Pleiades
content in the database:

  * **Place resources**: provide a descriptive and conceptual context for geographic, toponymic, bibliographic, and temporal information. This is the primary entity in the Pleiades database model. Pleiades place resources represent conceptual places.  

  * **Name resources**: record the details of modern and historical geographic names, including the languages and scripts in which they are attested.  

  * **Location resources:** record information about measureable spots and areas on the earth's surface  

  * **Reference Citations:** actionable citations of primary or secondary literature and data (both in print and online) that underpin or expand upon the information contained in Pleiades.   

  * **Temporal Attestations:** Assertions that a name or location was in active use during a particular period in history, together with assessments of confidence concerning those assertions.  

  * **Positional Accuracy Assessments:** Documents that describe the methods, precision, and accuracy of spatial data used in location resources.  

The following diagram, which makes use of the conventions of the [Unified
Modeling Language](http://en.wikipedia.org/wiki/Unified_Modeling_Language),
illustrates the structural relationships between the classes of the Pleiades
data model:

[![Pleiades Data
Model](images/pleiadesdd.jpg/image_preview)](images/pleiadesdd.jpg "Pleiades
Data Model" )

Any Pleiades **Place Resource** can contain zero-to-many **Location
Resources** and zero-to-many **Name Resources**. This structure gives us the
flexibility to model places that have no known ancient or modern name (e.g., a
bridge, a fortification, or even an entire settlement known only from
archaeology), as well as places that are mentioned by name in a historical
source but whose precise location cannot be determined today.

**Place, Name,** and **Location Resources** can each contain **Reference Citations** that point to external data, descriptive information, and the like. **Name Resources** always include at least one citation that demonstrates the use of that name in a contemporary textual context.

**Name** and **Location Resources** also include at least one **Temporal Attestation**, which fixes in time the other information provided by that resource. This approach also permits flexibility in modeling. For example, the city of Pompeii was destroyed by the eruption of Mt. Vesuvius in 79 CE, but because of the historical significance of the event and the long, active life of associated literature, the name "Pompeii" continued in use for centuries.

Each **Location Resource** is associated with a **Positional Accuracy
Assessment,** thereby providing crucial geospatial metadata.

Any **Pleiades Place Resource** can be associated with other **Place
Resources** through simple relationships we call "[Connections](what-are-
connections "What are "connections?"" )". We use Connections to create
hierarchies (settlements making up a region), networks (connecting roads to
settlements or settlements to rivers), and other topological relationships
(junction, overlap). It is a very coarse-grained relationship, but it does not
extend to cover more general notions of proximity (e.g., "nearness",
"between").

We use [Plone's "Add-On Product" (plugin)
architecture](http://plone.org/documentation/manual/add-on-products-developer-
manual/) to implement the Pleiades data model on our site. Our
_[PleiadesEntity](https://github.com/isawnyu/PleiadesEntity)_ product
implements the Pleiades data model in Plone. Because it makes use of [the
Plone Archetypes framework](http://plone.org/products/archetypes), software
classes in _PleiadesEntity_ inherit from multiple levels of ancestor classes
across different packages, making it challenging for even seasoned Python
programmers to gain an understanding of all the attributes and methods owned
by each of our six classes. To facilitate understanding of the code,
therefore, we make available [an Excel spreadsheet of Pleiades
attributes](files/pleiades-attributes-2014-05-30 "Pleiades Attributes
\(2014-05-30\)" ), which functions like a traditional data dictionary, listing
the major data items found in each class and describing them by type and
constraints.

History

    

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on Apr 21, 2015 03:34 PM 

Edited

[View this revision](http://pleiades.stoa.org/help/pleiades-data-
model/versions_history_form?version_id=13#version_preview) · [Compare with
current revision](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=current&two=13)

[ ↑ Compare ↓ ](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=13&two=12 "Compare with previous revision" )

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on May 30, 2014 07:24 AM 

Edited

[View this revision](http://pleiades.stoa.org/help/pleiades-data-
model/versions_history_form?version_id=12#version_preview) · [Compare with
current revision](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=current&two=12)

[ ↑ Compare ↓ ](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=12&two=11 "Compare with previous revision" )

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on May 30, 2014 07:24 AM 

Initial revision

[View this revision](http://pleiades.stoa.org/help/pleiades-data-
model/versions_history_form?version_id=11#version_preview) · [Compare with
current revision](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=current&two=11)

[ ↑ Compare ↓ ](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=11&two=10 "Compare with previous revision" )

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on May 30, 2014 07:22 AM 

Edited

[View this revision](http://pleiades.stoa.org/help/pleiades-data-
model/versions_history_form?version_id=10#version_preview) · [Compare with
current revision](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=current&two=10)

[ ↑ Compare ↓ ](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=10&two=9 "Compare with previous revision" )

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on May 30, 2014 07:22 AM 

Initial revision

[View this revision](http://pleiades.stoa.org/help/pleiades-data-
model/versions_history_form?version_id=9#version_preview) · [Compare with
current revision](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=current&two=9)

[ ↑ Compare ↓ ](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=9&two=8 "Compare with previous revision" )

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on May 30, 2014 07:21 AM 

Edited

[View this revision](http://pleiades.stoa.org/help/pleiades-data-
model/versions_history_form?version_id=8#version_preview) · [Compare with
current revision](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=current&two=8)

[ ↑ Compare ↓ ](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=8&two=7 "Compare with previous revision" )

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on May 30, 2014 07:17 AM 

Edited

[View this revision](http://pleiades.stoa.org/help/pleiades-data-
model/versions_history_form?version_id=7#version_preview) · [Compare with
current revision](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=current&two=7)

[ ↑ Compare ↓ ](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=7&two=6 "Compare with previous revision" )

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on May 30, 2014 06:49 AM 

Edited

[View this revision](http://pleiades.stoa.org/help/pleiades-data-
model/versions_history_form?version_id=6#version_preview) · [Compare with
current revision](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=current&two=6)

[ ↑ Compare ↓ ](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=6&two=5 "Compare with previous revision" )

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on May 30, 2014 06:28 AM 

Edited

[View this revision](http://pleiades.stoa.org/help/pleiades-data-
model/versions_history_form?version_id=5#version_preview) · [Compare with
current revision](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=current&two=5)

[ ↑ Compare ↓ ](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=5&two=4 "Compare with previous revision" )

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on May 30, 2014 06:25 AM 

Edited

[View this revision](http://pleiades.stoa.org/help/pleiades-data-
model/versions_history_form?version_id=4#version_preview) · [Compare with
current revision](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=current&two=4)

[ ↑ Compare ↓ ](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=4&two=3 "Compare with previous revision" )

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on May 30, 2014 06:22 AM 

Edited

[View this revision](http://pleiades.stoa.org/help/pleiades-data-
model/versions_history_form?version_id=3#version_preview) · [Compare with
current revision](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=current&two=3)

[ ↑ Compare ↓ ](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=3&two=2 "Compare with previous revision" )

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on May 27, 2014 05:06 PM 

Edited

[View this revision](http://pleiades.stoa.org/help/pleiades-data-
model/versions_history_form?version_id=2#version_preview) · [Compare with
current revision](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=current&two=2)

[ ↑ Compare ↓ ](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=2&two=1 "Compare with previous revision" )

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on May 27, 2014 04:56 PM 

Edited

[View this revision](http://pleiades.stoa.org/help/pleiades-data-
model/versions_history_form?version_id=1#version_preview) · [Compare with
current revision](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=current&two=1)

[ ↑ Compare ↓ ](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=1&two=0 "Compare with previous revision" )

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on May 27, 2014 04:42 PM 

Initial revision

[View this revision](http://pleiades.stoa.org/help/pleiades-data-
model/versions_history_form?version_id=0#version_preview) · [Compare with
current revision](http://pleiades.stoa.org/help/pleiades-data-
model/@@history?one=current&two=0)

##### Document Actions

  * [Print this](javascript:this.print\(\); "" )

