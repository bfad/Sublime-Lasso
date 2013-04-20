Sublime Text Package for Lasso
==============================

Lasso is an excellent programming language with a long history of being used for web development. This is a Package for Sublime Text 2 intended to aid in developing solutions in Lasso 9. It provides syntax highlighting, some snippets, and basic syntax checking build system.

Lasso Homepage: http://www.lassosoft.com/


## Installation Using Package Control

If you're not using Will Bond's [Package Control](http://wbond.net/sublime_packages/package_control) solution for Sublime Text, you really should be.

1. If you haven't already, [install Package Control](http://wbond.net/sublime_packages/package_control/installation)
1. In Sublime Text, bring up the command palette (Tools > Command Palette)
1. In the Command Palette, find and select "Package Control: Install Package" and hit return
1. In the resulting palette, find and select the "Lasso" package and hit return

That's it. Package Control will do the rest and you can begin using it right away.


## Manual Installation on OS X

To manually install the package, issue the following command in a terminal:

    $> git clone git://github.com/bfad/Sublime-Lasso ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/Lasso

To update to the latest version of this package:

    $> cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/Lasso
    $> git pull


## Syntax Highlighters

There are two syntax highlighters: "Lasso" and "HTML (Lasso)". The former treats the file as completely Lasso code - no delimiters necessary. The latter treats the document as HTML with Lasso sprinkled in by any of the standard Lasso 9 delimiters.


## License Information

This package is provided as-is and is placed in the Public Domain.
Sublime Text itself is proprietary software and is probably copyrighted by Sublime HQ Pty Ltd