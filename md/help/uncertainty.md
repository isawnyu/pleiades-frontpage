You are here: [Home](http://pleiades.stoa.org/home) →
[Help](http://pleiades.stoa.org/help) →  Uncertainty

[Skip to content.](http://pleiades.stoa.org/help/uncertainty?from=tom.elliott%
40nyu.edu&user-agent=Paregoriosian%2F0.1#documentContent) | [Skip to navigatio
n](http://pleiades.stoa.org/help/uncertainty?from=tom.elliott%40nyu.edu&user-
agent=Paregoriosian%2F0.1#portlet-navigation-tree)

#  Uncertainty

Creators: [Tom Elliott](/author/thomase) Copyright © The Contributors. Sharing
and remixing permitted under terms of the Creative Commons Attribution 3.0
License (cc-by).

Last modified  Jun 18, 2013 12:22 PM

tags:  [concept](http://pleiades.stoa.org/search?Subject%3Alist=concept),
[help](http://pleiades.stoa.org/search?Subject%3Alist=help)

How we model (un)certainty in Pleiades.

We cannot always be certain about things. This is as true of geography as it
is other aspects of life. In historical geography, uncertainty is not
uncommon. It stems from confusion and incompleteness in our sources, as well
as the limitations of our ability to understand them. In developing our data
models and interfaces for Pleiades -- and in conducting editing of data by the
community -- we must take stock of the varied ways in which uncertainty
affects us. We must avoid giving the false appearance of exactitude while
maintaining ease of use.

Fortunately, the designers, editors and compilers of the [Classical Atlas
Project](http://www.atlantides.org/trac/pleiades/wiki/CAP) grappled with these
issues in some detail. We will build on their work, ensuring that none of the
essential distinctions they identified are lost when we bring their data into
Pleiades.

Uncertainty affects the following content types and relationships:

## Names

  1. **Accuracy** of attestation 
    1. Accurate: string of characters in witness is thought to be correct (BAtlas: no special indication) 
    2. Inaccurate: witness is thought to be incorrect (BAtlas: name enclosed in inverted commas) 
    3. False: witness (or modern interpreter) is thought to have thoroughly confused, or even made up, a name (BAtlas: name listed in "False Names" list in Map-by-Map Directory) 
  2. **Completeness** of attestation 
    1. Complete: witness is thought to give complete name in an unproblematic fashion (BAtlas: no special indication) 
    2. Fragmentary, but reconstructable: witness is lacunose such that the complete name is not provided, but the missing character(s) can be restored with confidence (BAtlas: asterisk prefixed to reconstructed form; fragmentary version from witness not indicated) 
    3. Fragmentary and not reconstructable (BAtlas: ellipsis inside parentheses used to mark lacunae) 
  3. **Periodicity** of name 
    1. Certain (BAtlas: period codes in directory) 
    2. Certain but there is no contemporary witness; i.e., usage inferred from an earlier or later witness (BAtlas: period codes in directory and name rendered in square brackets) 
    3. Less certain (BAtlas: period codes plus question marks in directory) 
    4. Less certain and there is no contemporary witness (BAtlas: period codes in directory plus question marks, and name itself rendered in square brackets) 

### Names and uncertainty: examples from BAtlas directory listings

Name | Period | Modern Name / Location | Relevant entries from above  
---|---|---|---  
(...)lense | RL | Henchir el Abiod | 1.1, 2.3, 3.1  
Adada | HRL | Karabaulo | 1.1, 2.1, 3.1  
[Agrai] | L | Ağras, Atabey | 1.1, 2.1, 3.2  
Alina? Ins. | H | Yassıca Ada | 1.1, 2.1, 3.1 and see below: association of
name and location  
Anaboura | HRL? | Enevre | 1.1, 2.1, 3.3  
Aquae (...) | L | Yavuzeli | 1.1, 2.3, 3.1  
C(…)o § *Calambrio | RL | St-Germain-du-Salembre? | 1.1, 2.3, 3.1; the
question mark on the modern name corresponds to a hollow symbol plus question
mark on the map, see below  
*Eleinokapria | R | near Bucalı | 1.1, 2.1, 3.1  
‘Madamprus’ | H | Osmankalfalar | 1.2, 2.1, 3.1  
[*Praedium Plancianum] | R | near Belen, Bozova | 1.1, 2.2, 3.2  
*Syneta? | H | Bucakköy | 1.1, 2.2, 3.1 and see below: association of name and location  
  
## Locations

  1. Positional **accuracy** (horizontal) 
    1. Definition: the degree to which information on a map or in a digital database matches true or accepted values (see Geographer's Craft, s.v. "[Error, Accuracy and Precision](http://www.colorado.edu/geography/gcraft/notes/error/error_f.html)") 
    2. See separate discussion: [DataPrecisionAndAccuracy](http://www.atlantides.org/trac/pleiades/wiki/DataPrecisionAndAccuracy)
  2. Positional **precision** (horizontal) 
    1. Definition: the level of measurement (i.e., smallest order of magnitude or number of significant digits captured) 
    2. See separate discussion: [DataPrecisionAndAccuracy](http://www.atlantides.org/trac/pleiades/wiki/DataPrecisionAndAccuracy)
  3. **Placement confidence**/certainty 
    1. Explanation: some ancient sites were placed in the BAtlas on the basis of ancient textual description, inference from topography and the like (for example, an ancient source may indicate the location of a settlement, along a road and between two other nearby settlements; if the two settlements are securely locable and the route of the road is well known to us, there may be grounds to mark the location of the intermediate settlement on the map, even though we must do so with less confidence than for a site securely located by archaeology). 
    2. States (see [Refining Geographic Attribution](http://www.atlantides.org/trac/pleiades/wiki/RefiningGeographicPrecision)): 
      1. Pleiades "Known" = BAtlas "Certain" (solid symbol) 
      2. Pleiades "Approximate" = BAtlas "Less certain" (hollow symbol) or BAtlas "Tentative" (hollow symbol plus question mark); metadata will be used to distinguish the degree of certainty within the "approximate" category 
      3. Pleiades "Weak" = BAtlas Unlocated, but with some probable location expressed (see further below) 
  4. **Periodicity** of location 
    1. Certain (BAtlas: period codes in directory) 
    2. Less certain (BAtlas: period codes plus question marks in directory) 

### Locations and uncertainty: examples from BAtlas maps

[![Map 65 examples of point symbol certainty indications](http://www.atlantide
s.org/trac/pleiades/attachment/wiki/Uncertainty/PlacementCertaintyExamples.png
?format=raw)](http://www.atlantides.org/trac/pleiades/attachment/wiki/Uncertai
nty/PlacementCertaintyExamples.png)

  * Placement of Attalea is certain = Pleiades "Known" 
  * Placement of Magydos is less certain = Pleiades "Approximate" 
  * Placement of Limnai is tentative = Pleiades "Approximate" with extra hesitancy 

### Locations and uncertainty: examples from BAtlas Directory "Unlocateable
Toponyms" lists

In the case of "unlocateable" features, compilers had the option of adding a
textual entry in the "Probable Location" column in the Map-by-Map Directory.
Such notes were used to communicate whatever might bound the possible location
of the feature. Any feature for which a probable location has been noted in
BAtlas produces a location with "weak" attribution in Pleiades. For those
attested names where the compilers could not provide a probable location, the
Pleiades location attribution will be "none" (i.e., no location will be
associated with the name). A number of examples constituting weak locative
attribution follows.

Name | Period | Probable Location  
---|---|---  
Agris | H?RL | along coast of Gedrosia/Carmania  
Arai | H?R | tribe in Carmania  
Karpella Pr. | H?R | on border between Carmania and Gedrosia  
Magusum | R | town in Yemen  
Napegus | R | near Ras Mutayna  
Fines | R | on Durocortorum → Divodurum road; Marcheville or Mars-la-Tour?  
Accion | AH | Lacus Lemannus or Lake Le Bourget  
Cremonis Iugum | H | Col. Grimone or Tête du Cramont  
Vetonina | RL? | possibly Veldidena or Teriolis  
Soxotai | H?R | tribe in Carmanian desert  
  
## Associations of Names and Locations

Our confidence in associating attested names with mapable locations (whether
inferred from description or identified by survey or excavation) varies from
feature to feature. The BAtlas distinguished the following 3 main certainty
levels with respect to such associations:

  1. Certain: symbol and name placed on map with no special indicia (note that the symbol might be solid, hollow or hollow with a question mark, depending on the **separate** issue of placement confidence) 
  2. Less certain: symbol placed on map, together with name to which a question mark was postfixed 
  3. Uncertain: no symbol placed on map; name entered in a special "Unlocated toponyms" list in the relevant directory. 

Pleiades models the relationship between location and name slightly
differently, as follows:

  1. BAtlas certain = a Pleiades place containing 1..n locations (all spatially coincident) and 1..n names (nb: Pleiades location attribution may be "known" or "approximate") 
  2. BAtlas less certain = a Pleiades place containing 1..n locations (all spatially coincident) and 1..n names, plus metadata indicating lower degree of confidence in the association (nb: Pleiades location attribution may be "known" or "approximate") 
  3. BAtlas uncertain 
    1. Where compilers provided a general "probable location", the Pleiades place will contain 1..n locations (all spatially coincident) and 1..n names (nb: Pleiades location attribution will be "weak") 
    2. Where compilers provided a limited series of alternative associations for "probable location", the Pleiades place will contain 2..n locations (spatially distinct) and 1..n names (nb: Pleiades location attribution for each location may vary) 
    3. Where compilers provided no "probable location", the Pleiades place will contain 0 locations and 1..n names 

Note: In future enhancements to Pleiades, we may wish to add support for
modeling a number of the topological relationships implied by contents in the
**Probable Location** column; however, there is one state for which support
must be built-in early. This is the state (3.3 above) wherein the
identification of an attested name may be narrowed to a small number (usually
only 2 or 3) of archaeologically and topographically appropriate locations.
Fines, Accion, Cremonis Iugum and Vetonina would all fall into this category.
It will be important to be able to programmatically identify and manipulate
records that fall into this class, hence the creation of ticket
[#202](http://www.atlantides.org/trac/pleiades/ticket/202 "support single name
object appearing "in" multiple places \(closed\)" ).

History

    

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on Jun 18, 2013 12:22 PM 

Edited

[View this revision](http://pleiades.stoa.org/help/uncertainty/versions_histor
y_form?version_id=3#version_preview) · [Compare with current revision](http://
pleiades.stoa.org/help/uncertainty/@@history?one=current&two=3)

[ ↑ Compare ↓
](http://pleiades.stoa.org/help/uncertainty/@@history?one=3&two=2 "Compare
with previous revision" )

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on Jun 18, 2013 12:22 PM 

Initial revision

[View this revision](http://pleiades.stoa.org/help/uncertainty/versions_histor
y_form?version_id=2#version_preview) · [Compare with current revision](http://
pleiades.stoa.org/help/uncertainty/@@history?one=current&two=2)

[ ↑ Compare ↓
](http://pleiades.stoa.org/help/uncertainty/@@history?one=2&two=1 "Compare
with previous revision" )

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on Jun 18, 2013 12:21 PM 

got rid of extra heading

[View this revision](http://pleiades.stoa.org/help/uncertainty/versions_histor
y_form?version_id=1#version_preview) · [Compare with current revision](http://
pleiades.stoa.org/help/uncertainty/@@history?one=current&two=1)

[ ↑ Compare ↓
](http://pleiades.stoa.org/help/uncertainty/@@history?one=1&two=0 "Compare
with previous revision" )

  * Edited by [Tom Elliott](http://pleiades.stoa.org/author/thomase) on Jun 18, 2013 12:20 PM 

migrated in from the old wiki

[View this revision](http://pleiades.stoa.org/help/uncertainty/versions_histor
y_form?version_id=0#version_preview) · [Compare with current revision](http://
pleiades.stoa.org/help/uncertainty/@@history?one=current&two=0)

##### Document Actions

  * [Print this](javascript:this.print\(\); "" )

