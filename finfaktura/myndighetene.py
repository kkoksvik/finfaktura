#!/usr/bin/env python
# -*- coding:utf8 -*-
###########################################################################
#    Copyright (C) 2005-2008- Håvard Gulldahl 
#    <havard@lurtgjort.no>
#
#    Lisens: GPL2
#
# $Id$
###########################################################################

__all__ = ['BRUK_MYNDIGHETENE', 'myndighetene']

try:
    import BeautifulSoup
    BRUK_MYNDIGHETENE=True
except ImportError:
    BRUK_MYNDIGHETENE=False
    

import re, urllib

from htmlentitydefs import name2codepoint, codepoint2name

urllib.URLopener.version = 'Mozilla/5.0 (compatible; Konqueror/3.4; Linux) KHTML/3.4.1 (like Gecko)'
urllib.FancyURLopener.prompt_user_passwd = lambda self, host, realm: (None, None)

def unescape(data):
    "convert html entitydefs into unicode characters"
    #thanks to http://www.intertwingly.net/stories/2003/08/28/atomef.py
    chunks = re.split('&(#?\w+);',data)
    for i in range(1,len(chunks),2):
        if chunks[i] in name2codepoint:
            chunks[i] = unichr(name2codepoint[chunks[i]])
        elif re.match('#\d+$',chunks[i]):
            chunks[i] = unichr(int(chunks[i][1:]))
    return "".join(chunks)

class myndighetene:
    "Slår opp på nettet og letter kontakten med de offentlige myndighetene"

    def orgInfo(self, orgnr):
        "Slår opp nøkkelinformasjon for foretaket i Brønnøysundregisterene"
        orginfo = {}
        #http://w2.brreg.no/enhet/sok/detalj.jsp?orgnr=987719508
        url = 'http://w2.brreg.no/enhet/sok/detalj.jsp?orgnr=%s' % self.rensOrgnr(orgnr)
        #s = urllib.urlopen(url).read()
        s = file("/var/tmp/orginfo.html").read()
        suppe = BeautifulSoup.BeautifulSoup(s)
        info = suppe.fetch('table', {'cellspacing':1})[0]
        for z in info.fetch('tr'):
            orginfo[z.b.string] = z.fetch('td')[1].contents[0].strip()
        return orginfo

    def skjemaplikter(self, orgnr):
        "Slår opp skjemaplikter for foretaket i Brønnøysundregisterene"
        #http://w2.brreg.no/oppgaveregisteret/oversikt_orgnr.jsp?orgnr=987719508
        url = 'http://w2.brreg.no/oppgaveregisteret/oversikt_orgnr.jsp?orgnr=%s' % self.rensOrgnr(orgnr)
        #s = urllib.urlopen(url).read()
        s = file("/var/tmp/oppgaver.html").read()
        suppe = BeautifulSoup.BeautifulSoup(s)
        for rad in suppe.fetch("table")[-1].fetch("tr")[2:]:
            r = rad.td.p
            skjemanr = r.contents[0].string
            skjemanavn = r.a.string
            skjemaurl = 'http://w2.brreg.no/oppgaveregisteret/' + r.a['href']
            skjemainstans = rad.td.nextSibling('a')[0].string
            yield [unescape(s) for s in (skjemanr, skjemanavn, skjemainstans, skjemaurl)]


    def rensOrgnr(self, orgnr):
        return orgnr.replace(" ", "")

if __name__ == "__main__":
    #test 
    foretak = myndighetene()
    print "nøkkelinfo:"
    print foretak.orgInfo(987719508)
    print "skjemaplikter:"
    print foretak.skjemaplikter(987719508)


