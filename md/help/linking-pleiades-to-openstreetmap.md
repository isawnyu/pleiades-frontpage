You are here: [Home](http://pleiades.stoa.org/home) →
[Help](http://pleiades.stoa.org/help) →  Linking Pleiades to OpenStreetMap

[Skip to content.](http://pleiades.stoa.org/help/linking-pleiades-to-
openstreetmap?from=tom.elliott%40nyu.edu&user-
agent=Paregoriosian%2F0.1#documentContent) | [Skip to
navigation](http://pleiades.stoa.org/help/linking-pleiades-to-
openstreetmap?from=tom.elliott%40nyu.edu&user-
agent=Paregoriosian%2F0.1#portlet-navigation-tree)

#  Linking Pleiades to OpenStreetMap

tags:  [adding](http://pleiades.stoa.org/search?Subject%3Alist=adding),
[howto](http://pleiades.stoa.org/search?Subject%3Alist=howto),
[help](http://pleiades.stoa.org/search?Subject%3Alist=help)

Creators: [Sean Gillies](/author/sgillies)

Contributors: [Tom Elliott](/author/thomase)

Copyright © The Contributors. Sharing and remixing permitted under terms of
the Creative Commons Attribution 3.0 License (cc-by).

Last modified  Feb 07, 2013 06:44 PM

We've made it much easier to get coordinates from and make ties to entities in
OpenStreetMap, the world's foremost open geographical database. Easy enough,
we hope, that this will become the first choice for Pleiades users.

I'm a Pleiades user as well as its developer, and I try to get coordinates
from OpenStreetMap whenever I can for several reasons.

  * Citing a specific OpenStreetMap entity, as [http://pleiades.stoa.org/places/628932/summit](../../places/628932/summit) cites <http://www.openstreetmap.org/browse/node/100778739>, makes a discoverable and actionable link between Pleiades and the world's foremost open spatial database.
  * I'm an OpenStreetMap user too, and very interested in getting historical data into OSM. These are steps in that direction. The links I've made in Pleiades can be used someday in finding the appropriate OSM objects to improve using information from Pleiades.
  * OpenStreetMap has editing tools far beyond anything that Pleiades can or will provide. See the new [iD editor](http://ideditor.com/) for example. I'd like to explore the possibilities of digitizing in OSM and then pulling coordinates back into Pleiades.

To make it easier for myself (and hopefully for others), I've added a new
option to the familiar "Add Location" button on every place page. Click the
downward caret on the right side of that button and a short form will be
revealed. Type in the ID of a OpenStreetMap Node such as 100778739 for the
entity mentioned above (only nodes, for now), an optional title (which also
becomes the location's short name, a sensible default is produced if left
blank), and click "Go."

![OSM Location Form](images/osm-location-form/image_large)

The form's handler then makes a request to the OSM API, parses the response,
and creates a new Pleiades location object with many fields already filled out
for you: the title and description, the coordinates, the citation, the
provenance – and best of all – the accuracy assessment. Add some time periods
for which this location is related to the parent place, and a citation for
those, and it's ready to be submitted for publication.

How do you find the right OSM node to use? If you're a registered
OpenStreetMap user (signup [here](http://www.openstreetmap.org/user/new) if
you haven't), you can use the Potlatch2 editor to pick nodes within a map view
and get their IDs. Here's a sketch of the process.

Starting from
<http://en.wikipedia.org/wiki/Church_of_Sant'Urbano_alla_Caffarella>, click
the coordinates link to get to <http://toolserver.org/~geohack/geohack.php?pag
ename=Church_of_Sant%27Urbano_alla_Caffarella&params=41.857844_N_12.524306_E_r
egion:IT-RM_type:landmark>. Under "Global Services" there's a link to an OSM
map: <http://www.openstreetmap.org/?mlat=41.857844&mlon=12.524306&zoom=15&laye
rs=M>. If you're logged in, you'll see an "edit" option above the map. Click
it and select the Potlatch 2 editor. It's a Flash plugin, takes a few seconds
to load, but then shows you the objects in the map. You can click on any to
select and information will be shown in tables to the left of the map. The
"simple" view (see the options under the table) doesn't show the Node's
identifier, but the advanced view does. Click on the node number and you'll
get a table showing the node's history. Click on "More details" and your
browser will open a page such as
<http://www.openstreetmap.org/browse/node/259712693>.

That's all a bit tricky. Work is underway to replace Potlatch 2 with something
more modern and less complicated, and the prototype iD editor is actually
quite usable now. It allows you to see OSM objects anonymously (of course, you
can't make any changes) and provides a shorter path to the node identifiers.
For example, browse to <http://geowiki.com/iD/#map=17.00/41.85784/12.52432>
and click the "dev" link at the bottom to switch to the actual live OSM
database. After the nodes load on screen, select one of the corner nodes of
the church we're using as an example, and then click on the "view on OSM" link
to get to <http://www.openstreetmap.org/browse/node/259712693>. Much more
direct, don't you agree?

History

    

  * Edited by [Sean Gillies](http://pleiades.stoa.org/author/sgillies) on Feb 07, 2013 06:44 PM 

Edited

[View this revision](http://pleiades.stoa.org/help/linking-pleiades-to-
openstreetmap/versions_history_form?version_id=3#version_preview) · [Compare
with current revision](http://pleiades.stoa.org/help/linking-pleiades-to-
openstreetmap/@@history?one=current&two=3)

[ ↑ Compare ↓ ](http://pleiades.stoa.org/help/linking-pleiades-to-
openstreetmap/@@history?one=3&two=2 "Compare with previous revision" )

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on Feb 07, 2013 06:09 PM 

Edited

[View this revision](http://pleiades.stoa.org/help/linking-pleiades-to-
openstreetmap/versions_history_form?version_id=2#version_preview) · [Compare
with current revision](http://pleiades.stoa.org/help/linking-pleiades-to-
openstreetmap/@@history?one=current&two=2)

[ ↑ Compare ↓ ](http://pleiades.stoa.org/help/linking-pleiades-to-
openstreetmap/@@history?one=2&two=1 "Compare with previous revision" )

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on Feb 07, 2013 06:09 PM 

Initial revision

[View this revision](http://pleiades.stoa.org/help/linking-pleiades-to-
openstreetmap/versions_history_form?version_id=1#version_preview) · [Compare
with current revision](http://pleiades.stoa.org/help/linking-pleiades-to-
openstreetmap/@@history?one=current&two=1)

[ ↑ Compare ↓ ](http://pleiades.stoa.org/help/linking-pleiades-to-
openstreetmap/@@history?one=1&two=0 "Compare with previous revision" )

  * Edited by [Sean Gillies](http://pleiades.stoa.org/author/sgillies) on Feb 07, 2013 05:51 PM 

Initial revision

[View this revision](http://pleiades.stoa.org/help/linking-pleiades-to-
openstreetmap/versions_history_form?version_id=0#version_preview) · [Compare
with current revision](http://pleiades.stoa.org/help/linking-pleiades-to-
openstreetmap/@@history?one=current&two=0)

##### Document Actions

  * [Print this](javascript:this.print\(\); "" )

