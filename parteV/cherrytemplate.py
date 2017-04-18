#!/usr/bin/python

from cherrytemplate import renderTemplate

progs = ['Yes', 'Genesis', 'King Crimsom']

template = '<html>\n<body>\n'\
'<py-for="prog in progs">'\
'<py-eval="prog"><br>\n'\
'</body>\n</html>\n'

print renderTemplate(template)