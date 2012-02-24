#!/usr/bin/env python
# encoding: utf-8
"""
builder.py

Created by Stephan Wallentin on 2011-11-19.

UML Diagram
  Can be viewed or downloaded from,
  http://www.dofactory.com/Patterns/PatternBuilder.aspx#UML

The classes and/or objects participating in this pattern are:

  Builder  (VehicleBuilder)
    specifies an abstract interface for creating parts of a Product object

  ConcreteBuilder  (MotorCycleBuilder, CarBuilder, ScooterBuilder)
    constructs and assembles parts of the product by implementing the Builder interface
    defines and keeps track of the representation it creates
    provides an interface for retrieving the product

  Director  (Shop)
    constructs an object using the Builder interface

  Product  (Vehicle)
    represents the complex object under construction. ConcreteBuilder builds the product's internal representation and defines the process by which it's assembled
    includes classes that define the constituent parts, including interfaces for assembling the parts into the final result


"""

import sys
import os
import unittest

class htmlapp():
  def __init__(self):
    self.headerbuilder    = headerbuilder()
    self.bodybuilder = bodybuilder()
    self.footerbuilder    = footerbuilder()
  
  def build(self):
    self.headerbuilder.build()
    self.bodybuilder.build()
    self.footerbuilder.build()
      
  def render(self):
    self.headerbuilder.render()
    self.bodybuilder.render()
    self.footerbuilder.render()

class htmlapp():
  def __init__(self):
    pass
    
class motorcyclebuilder():
  def __init__(self):
    pass

class carbuilder():
  def __init__(self):
    pass

class scooterbuilder():
  def __init__(self):
    pass

    
class vehicle(object):
  def __init__(self):
    pass

class untitledTests(unittest.TestCase):
  def setUp(self):
    pass

  def testvehiclebuilder(self):
    builder     = None
    htmlmanager = htmlManager()
    
    builder     = new headerbuilder()
    shop.construct(builder)
    # insert test here
    builder.html.render()

    builder     = new bodybuilder()
    shop.construct(builder)
    # insert test here
    builder.html.render()    
    
    builder     = new footerbuilder()
    shop.construct(builder)
    # insert test here
    builder.html.render()
    
if __name__ == '__main__':
  unittest.main()