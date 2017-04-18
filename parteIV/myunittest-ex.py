#!/usr/bin/python

#coding: utf-8

"""fibtest.py
Usa unittest para testar fib.py
"""
import fib
import unittest

class TestSequenceFunctions(unittest.TestCase):

	def setup(self):
		self.seq = range(10)

	def test0(self):
		self.assertEqual(fib.fib(0),1)

	def test1(self):
		self.assertEqual(fib.fib(1),1)

	def test10(self):
		self.assertEqual(fib.fib(10), 89)

	def testseq(self):
		fibs = [1,1,2,3,5,8,13,21,34,55]
		for x, y in zip(fibs,[fib.fib(x)for x in self.seq]):
			self.assert_(x is y)
	def testtype(self):
		self.assertRaises(TypeError, fib.fib, '')

if __name__ == "__main__":
	unittest.main()