Big.Brother - Introduction
==========================
This product will install a viewlet that tracks who has viewed a document 
and when. It will also add a portlet for people with permission X to see 
the last time that each person viewed that item.

It uses sqlalchemy and a sqlite database to store all the results. It's not 
meant then for large sites or multi-site hosting. It could be configured that 
way but not right now. 

I am using a relational database because it makes more sense for data monkeys 
to parse through the data in the end. This would likely be useful for admin 
and IT types than developers. It's also fast, which is a nice feature.

For known issues, see docs/TODO.txt.