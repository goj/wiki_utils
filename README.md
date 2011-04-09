Python utilities for reading wikimedia dump files
-------------------------------------------------

*    `dump_utils.dump_reader` takes `.sql.gz` MySQL dump,
     tortures it with some sed magic[1] and returns a csv reader

    for page_id, page_ns, page_title, *_ in dump_reader('enwiki-20110317-page.sql.gz'):
        print(page_id, '->', page_title)

[1] - This is quite quick & dirthy approach, but it worked
reliably for me. You probably want to use it just to
populate your custom database using few dump files.
This is an offline process, so you do it once,
use the result and not worry about bugs-that-may-have-happened.
