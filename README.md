Python 3 utilities for reading wikimedia dump files
=================================================

*    `dump_utils.dump_reader` takes `.sql.gz` MySQL dump,
     tortures it with some sed magic^1 and returns a csv reader

        for page_id, page_ns, page_title, *_ in dump_reader('enwiki-latest-page.sql.gz'):
            print(page_id, '->', page_title)

    `dump_reader` takes extra positional arguments for additional text-level steps
    (like `"grep \",'pl',\""`) which can speed up the process significantly

    Because wikipedia dumps sometimes contain invalid utf-8, there is extra
    keyword-only `fix_utf8` argument to `dump_reader`. Set it to true if you
    have encoding problems

This library is Python 3-only and depends on you having sane linux environment
(awk, sed, grep, zcat, etc.)

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
