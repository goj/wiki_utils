Python utilities for reading wikimedia dump files
=================================================

*    `dump_utils.dump_reader` takes `.sql.gz` MySQL dump,
     tortures it with some sed magic^1 and returns a csv reader

        for page_id, page_ns, page_title, *_ in dump_reader('enwiki-latest-page.sql.gz'):
            print(page_id, '->', page_title)

Where to get the dump files?
----------------------------

*  [http://dumps.wikimedia.org/enwiki/latest/](http://dumps.wikimedia.org/enwiki/latest/)
*  [http://dumps.wikimedia.org/enwiktionary/latest/](http://dumps.wikimedia.org/enwiktionary/latest/)
*  [http://dumps.wikimedia.org/plwiki/latest/](http://dumps.wikimedia.org/plwiki/latest/)
*  [http://dumps.wikimedia.org/plwiktionary/latest/](http://dumps.wikimedia.org/plwiktionary/latest/)
*  [full list](http://dumps.wikimedia.org/)

<hr/>

<sup>1</sup> - This is quite quick & dirthy approach, but it worked
reliably for me. You probably want to use it just to
populate your custom database using few dump files.
This is an offline process, so you do it once,
use the result and not worry about bugs-that-may-have-happened.
