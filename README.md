Inline Quote Extension for Python-Markdown
==================================

Wraps the inline content surrounded by two single quotes into `q` tags.


Installation
------------

    pip install git+git://github.com/gumblex/mdx_quote.git

Usage
-----

    >>> import markdown
    >>> src = "The man said ''Things that are impossible just take longer''. I disagreed with him."
    >>> html = markdown.markdown(src, ['quote'])
    >>> print(html)
    <p>The man said <q>Things that are impossible just take longer</q>. I disagreed with him.</p>

Dependencies
------------

* [Markdown 2.0+](http://www.freewisdom.org/projects/python-markdown/)


Copyright
---------

2011, 2012 [The active archives contributors](http://activearchives.org/)
2016 Dingyuan Wang
All rights reserved.

This software is released under the modified BSD License. 
See LICENSE.md for details.
