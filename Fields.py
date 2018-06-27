# Fields.py

# This file is for a 2D vector field
#
# Mathematically, there is a 2D vector space R and a set of n-dimensional vectors U. A 2D vector field is a function
# V(x,y) that maps each R-vector to a U-vector: V(x, y) = (u1, u2, ..., un)
#
#

class ScalarField:
	dim = 1
	def __init__(self, xlength, ylength):
		self.xlength = xlength
		self.ylength = ylength
		self.pos = {}
 
	def initConstantMap(self, c):
		for x in range(0, self.xlength):
			for y in range(0, self.ylength):
				self.pos[x, y] = c

	def equals(self, field):
		for x in range(self.xlength):
			for y in range(self.ylength):
				self.pos[x, y] = field.pos[x, y]

	def times(self, factor):
		target = self
		if type(factor) == type(self):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
					target.pos[x, y] *= factor.pos[x, y]
		elif type(factor) == type(0.0) or type(divisor) == type(0) or type() == type(1j):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
					target.pos[x, y] *= factor
		return target

	def dividedBy(self, divisor):
		target = self
		if type(divisor) == type(self):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
					target.pos[x, y] /= divisor.pos[x, y]
		elif type(divisor) == type(0.0) or type(divisor) == type(0) or type() == type(1j):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
					target.pos[x, y] /= divisor
		return target

	def dividedFrom(self, dividend):
		target = self
		if type(dividend) == type(self):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
					if target.pos[x, y] == 0:
						target.pos[x, y] = dividend.pos[x, y] * (10 ** 300)
					else:
						target.pos[x, y] = dividend.pos[x, y] / target.pos[x, y]
		elif type(divisor) == type(0.0) or type(divisor) == type(0) or type(divisor) == type(1j):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
					if target.pos[x, y] == 0:
						target.pos[x, y] = dividend * (10 ** 300)
					else:
						target.pos[x, y] = dividend / target.pos[x, y]
		return target

	def plus(self, addend):
		target = self
		if type(addend) == type(self):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
					target.pos[x, y] += addend.pos[x, y]
		elif type(addend) == type(0.0) or type(addend) == type(0) or type(addend) == type(1j):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
					target.pos[x, y] += addend
		return target

	def minus(self, subtrachend):
		target = self
		if type(subtrachend) == type(self):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
					target.pos[x, y] -= subtrachend.pos[x, y]
		elif type(subtrachend) == type(0.0) or type(subtrachend) == type(0) or type(subtrachend) == type(1j):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
					target.pos[x, y] -= subtrachend
		return target

	def raisedTo(self, exponent):
		target = self
		if type(exponent) == type(self):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
					target.pos[x, y] = target.pos[x, y] ** exponent.pos[x, y]
		elif type(exponent) == type(0.0) or type(exponent) == type(0) or type(exponent) == type(1j):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
					target.pos[x, y] = target.pos[x, y] ** exponent
		return target

	def raisedFrom(self, base):
		target = self
		if type(base) == type(self):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
					target.pos[x, y] = base.pos[x, y] ** target.pos[x, y]
		elif type(base) == type(0.0) or type(base) == type(0) or type() == type(1j):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
					target.pos[x, y] = base ** target.pos[x, y]
		return target


class VectorField:

	def __init__(self, xlength, ylength, dim):
		self.xlength = xlength
		self.ylength = ylength
		self.dim = dim # dim is the number of dimensions of the target vector space (e.g. dim = 4 -> pos[2, 4] = (1, 5, 3, 1))
		self.pos = {}
 
	def initConstantMap(self, c):
		for x in range(0, self.xlength):
			for y in range(0, self.ylength):
				self.pos[x, y] = [c] * self.dim

	def equals(self, field):
		if self.dim != field.dim:
			print('dimensions do not equal')
		else:
			for x in range(self.xlength):
				for y in range(self.ylength):
					for n in range(self.dim):
						self.pos[x, y][n] = field.pos[x, y][n]

	def times(self, factor):
		target = self
		if type(factor) == type(self):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
						target.pos[x, y] *= factor.pos[x, y]
		elif type(divisor) == type(0.0) or type(divisor) == type(0) or type() == type(1j):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
					target.pos[x, y] *= factor
		return target

	def dividedBy(self, divisor):
		target = self
		if type(divisor) == type(self):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
						target.pos[x, y] /= divisor.pos[x, y]
		elif type(divisor) == type(0.0) or type(divisor) == type(0) or type() == type(1j):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
					target.pos[x, y] /= divisor
		return target

	def dividedFrom(self, dividend):
		target = self
		if type(dividend) == type(self):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
						if target.pos[x, y] == 0:
							target.pos[x, y] = dividend.pos[x, y] * (10 ** 300)
						else:
							target.pos[x, y] = dividend.pos[x, y] / target.pos[x, y]
		elif type(divisor) == type(0.0) or type(divisor) == type(0) or type(divisor) == type(1j):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
					if target.pos[x, y] == 0:
						target.pos[x, y] = dividend * (10 ** 300)
					else:
						target.pos[x, y] = dividend / target.pos[x, y]
		return target

	def plus(self, addend):
		target = self
		if type(addend) == type(self):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
						target.pos[x, y] += addend.pos[x, y]
		elif type(addend) == type(0.0) or type(addend) == type(0) or type(addend) == type(1j):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
					target.pos[x, y] += addend
		return target

	def minus(self, subtrachend):
		target = self
		if type(subtrachend) == type(self):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):

							target.pos[x, y] -= subtrachend.pos[x, y]
		elif type(subtrachend) == type(0.0) or type(subtrachend) == type(0) or type(subtrachend) == type(1j):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
					target.pos[x, y] -= subtrachend
		return target

	def raisedTo(self, exponent):
		target = self
		if type(exponent) == type(self):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):

							target.pos[x, y] = target.pos[x, y] ** exponent.pos[x, y]
		elif type(exponent) == type(0.0) or type(exponent) == type(0) or type(exponent) == type(1j):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
					target.pos[x, y] = target.pos[x, y] ** exponent
		return target

	def raisedFrom(self, base):
		target = self
		if type(base) == type(self):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):

							target.pos[x, y] = base.pos[x, y] ** target.pos[x, y]
		elif type(base) == type(0.0) or type(base) == type(0) or type() == type(1j):
			for x in range(0, self.xlength):
				for y in range(0, self.ylength):
					target.pos[x, y] = base ** target.pos[x, y]
		return target


