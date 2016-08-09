# -*- coding: utf-8 -*-
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 * 2.54 # inches
weight = 180 *0.45 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %4f cm tall." % height 
print "He's %4f kg  heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair) 
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %s, %s, and %s I get %s." % (
      age, height, weight, age + height + weight)


