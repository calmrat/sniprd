
======================
    sniprd
======================

DESCRIPTION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Comfortably archive the stuff you get done. Compatible with 
status-report. Made for Humans.


EXAMPLES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Save a basic snip with now() timestamp::

    snip #home #car I went to the post-office to buy stamps

Save a snip as completed yesterday::

    snip yesterday #project_x reported 36 bugs in BZ, 14 in JIRA

Save a snip as completed on a specific date in the past::

    snip 2015-01-01 pushed 14 code #commits

Save a snip and connect with others involved::

    snip washed dads car today @philly @dad #allowance

Save multiple snips at once completed the day before yesterday::

    snip -1 #project_x did this; #private arrived 30m late

See snip --help for complete list of available commands.

To retrieve your current week's saved snips, use status-report::

    status-report --snips project_x

To sync your current week's saved snips with a remote db::

    snip sync project_x [https://kejbaly2.sniprd.com]


CONFIGURATION - sniprd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The config file ~/.sniprd is used to store general settings::

    [general]
    uri = ~/.sniprd.db  # DEFAULT

    # push (sync) ALL snips to another db
    [push]
    uri = postgresql://user:pass@sniphub.com/shared
    exclude_tags = ["private", "confidential"]
    exclude_regex = ["secret_code", "fsck"]

    # push snips with hashtag #home to another db
    [push-home]
    uri = postgresql://user:pass@server.com/db:5432

    # email #project_x snips to someone
    [push-project_x]
    uri = email://get@it.done
    include_tags = ["project_x"]

    [at-philly]
    uri = email://philly@cheeze.com


CONFIGURATION - status-report 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Update the config file ~/.status-report to enable snips::

    [snips]
    # default place to query for snips
    uri = ~/.snips.db  # DEFAULT
    enabled = ["project_x", "home", "other"]

    [home]
    type = snips
    # where else to look for home tagged queries
    uri = postgresql://user:pass@server.com/db:5432
    aggregate = True  # also include those found in default db


Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Snippets can never be updated; each snip stored along with a
unique SHA-256 hash. 
Config options 'exclude_*' and 'include_*' are mutually exclusive

COPYRIGHT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Copyright (c) 2015 Red Hat, Inc. All rights reserved.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 2 of
the License, or (at your option) any later version.

