You are here: [Home](http://pleiades.stoa.org/home) →
[Help](http://pleiades.stoa.org/help) →  Pleiades Identifiers (place numbers)

[Skip to content.](http://pleiades.stoa.org/help/pleiades-identifiers-place-
numbers?from=tom.elliott%40nyu.edu&user-
agent=Paregoriosian%2F0.1#documentContent) | [Skip to
navigation](http://pleiades.stoa.org/help/pleiades-identifiers-place-
numbers?from=tom.elliott%40nyu.edu&user-agent=Paregoriosian%2F0.1#portlet-
navigation-tree)

#  Pleiades Identifiers (place numbers)

Creators: [Tom Elliott](/author/thomase) Copyright © The Contributors. Sharing
and remixing permitted under terms of the Creative Commons Attribution 3.0
License (cc-by).

Last modified  Nov 17, 2014 05:02 PM

tags:  [using](http://pleiades.stoa.org/search?Subject%3Alist=using),
[concept](http://pleiades.stoa.org/search?Subject%3Alist=concept),
[help](http://pleiades.stoa.org/search?Subject%3Alist=help)

This document describes the various identifier schemes that have been used for
Place Resources in Pleiades over the lifetime of the project. It also provides
information about how data using one set or another of legacy identifiers can
be "crosswalked" to the current, stable Uniform Resource Identifiers that are
used throughout the site today.

## Current Identifier Scheme

### Uniform Resource Identifiers (URIs)

Pleiades identifies each of its Place Resources with a Uniform Resource
Identifier (URI). This identifier scheme and its use is fully documented in a
separate document entitled "[What are Pleiades URIs?](what-are-pleiades-uris
"What are Pleiades URIs?" )".

### Pleiades IDs

The URIs incorporate a component known as a "Pleiades ID." Each Pleiades ID is
a string unique to the container at http://pleiades.stoa.org/places/. When
concatenated to that URL it produces the permanent URIs of objects in the
Pleiades system (like '148107' -> 'http://pleiades.stoa.org/places/148107').
Bare Pleiades IDs are used in some third-party systems for tagging purposes,
e.g., in Flickr machine tags.

Legacy Identifier Schemes

There are two earlier identifier schemes, now both deprecated, that were used
during earlier phases of the project.

### Feature IDs

The "feature id" is our oldest legacy identifier and is formatted like
"batlas-MM-TT-RR" where MM is the map number, TT is the table number within
the map directory, and RR is the row number within the table.

### BAtlas IDs

The "batlas id" is formed by normalizing to ASCII the map labels for a given
place (spaces replaced with hyphens) and concatenating "-MM-GG" where MM is
the map number and GG is the grid cell in lower case. All BAtlas IDs created
by the project were released online in machine-readable form at
<http://www.atlantides.org/batlas/>, including human-readable PDF and HTML
versions for manual reference.

## Conversion

Datasets that contain legacy identifier schemes can be programmatically and
reliably updated (cross-walked) to Pleiades IDs and URIs. A complete machine-
readable concordance for this purpose (in comma-separated-values -- i.e. "CSV"
-- format) between feature IDs, BAtlas IDs, and Pleiades IDs may be downloaded
at [http://www.atlantides.org/downloads/pleiades/batlasids-2011.tar.gz](http:/
/www.atlantides.org/downloades/pleiades/batlasids-2011.tar.gz).

History

    

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on Nov 17, 2014 05:01 PM 

Edited

[View this revision](http://pleiades.stoa.org/help/pleiades-identifiers-place-
numbers/versions_history_form?version_id=4#version_preview) · [Compare with
current revision](http://pleiades.stoa.org/help/pleiades-identifiers-place-
numbers/@@history?one=current&two=4)

[ ↑ Compare ↓ ](http://pleiades.stoa.org/help/pleiades-identifiers-place-
numbers/@@history?one=4&two=3 "Compare with previous revision" )

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on Nov 17, 2014 04:59 PM 

supersession

[View this revision](http://pleiades.stoa.org/help/pleiades-identifiers-place-
numbers/versions_history_form?version_id=3#version_preview) · [Compare with
current revision](http://pleiades.stoa.org/help/pleiades-identifiers-place-
numbers/@@history?one=current&two=3)

[ ↑ Compare ↓ ](http://pleiades.stoa.org/help/pleiades-identifiers-place-
numbers/@@history?one=3&two=2 "Compare with previous revision" )

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on Nov 17, 2014 04:57 PM 

fixed typo

[View this revision](http://pleiades.stoa.org/help/pleiades-identifiers-place-
numbers/versions_history_form?version_id=2#version_preview) · [Compare with
current revision](http://pleiades.stoa.org/help/pleiades-identifiers-place-
numbers/@@history?one=current&two=2)

[ ↑ Compare ↓ ](http://pleiades.stoa.org/help/pleiades-identifiers-place-
numbers/@@history?one=2&two=1 "Compare with previous revision" )

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on Nov 17, 2014 04:56 PM 

links to downloads

[View this revision](http://pleiades.stoa.org/help/pleiades-identifiers-place-
numbers/versions_history_form?version_id=1#version_preview) · [Compare with
current revision](http://pleiades.stoa.org/help/pleiades-identifiers-place-
numbers/@@history?one=current&two=1)

[ ↑ Compare ↓ ](http://pleiades.stoa.org/help/pleiades-identifiers-place-
numbers/@@history?one=1&two=0 "Compare with previous revision" )

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on Nov 17, 2014 04:36 PM 

initial content transfer from TRAC

[View this revision](http://pleiades.stoa.org/help/pleiades-identifiers-place-
numbers/versions_history_form?version_id=0#version_preview) · [Compare with
current revision](http://pleiades.stoa.org/help/pleiades-identifiers-place-
numbers/@@history?one=current&two=0)

##### Document Actions

  * [Print this](javascript:this.print\(\); "" )

