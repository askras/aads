#!/usr/bin/env python3

'''Example class Vector

In mathematics and physics, vector is a term that refers colloquially to some quantities that
cannot be expressed by a single number (a scalar), or to elements of some vector spaces.

Historically, vectors were introduced in geometry and physics (typically in mechanics) for
quantities that have both a magnitude and a direction, such as displacements, forces and velocity.
Such quantities are represented by geometric vectors in the same way as distances, masses and
time are represented by real numbers.

See also: https://en.wikipedia.org/wiki/Vector_(mathematics_and_physics)
'''

from typing import Any, Self

import math


class Vector:
    '''Vector in 2D Euclidean space'''

    def __init__(self, x: float = 0, y: float = 0) -> None:
        """Create and initialize vector in 2D Euclidean space

        Create zero vector
        >>> Vector()
        Vector(x=0, y=0)

        Create 2D vector
        >>> Vector(1, 2)
        Vector(x=1, y=2)

        >>> Vector(x=1, y=2)
        Vector(x=1, y=2)

        """
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        '''Get the string representation of this node (for programmer)

        >>> Vector(1, 2).__repr__()
        'Vector(x=1, y=2)'

        >>> repr(Vector(0, 0))
        'Vector(x=0, y=0)'

        '''
        return f'Vector(x={self.x}, y={self.y})'

    def __str__(self) -> str:
        '''Get the string representation of this node (for user)

        >>> print(Vector(1, 2))
        \\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix}

        >>> got = str(Vector(x=0, y=0))
        >>> expected = r'\\begin{pmatrix} 0 \\\\ 0 \\end{pmatrix}'
        >>> got == expected
        True
        '''
        return r'\begin{pmatrix} ' + str(self.x) + r' \\ ' + str(self.y) + r' \end{pmatrix}'

    def norm(self, p: [int, str] = 2) -> float:
        '''Returns the Lp-norm of the vector

        In mathematics, a norm is a function from a real or complex vector space to the non-negative real
        numbers that behaves in certain ways like the distance from the origin: it commutes with scaling,
        obeys a form of the triangle inequality, and is zero only at the origin.
        In particular, the Euclidean distance in a Euclidean space is defined by a norm on the associated
        Euclidean vector space, called the Euclidean norm, the 2-norm, or, sometimes, the magnitude of the vector.
        This norm can be defined as the square root of the inner product of a vector with itself.
        See also: https://en.wikipedia.org/wiki/Norm_(mathematics)

        >>> Vector(0, 0).norm()
        0.0

        >>> Vector(-30, 20.2).norm('infty')
        30

        >>> Vector(3, 4).norm(2)
        5.0

        >>> Vector(-3, 4.5).norm(1)
        7.5

        >>> Vector(1, 2).norm(-1)
        Traceback (most recent call last):
        ...
        ValueError: p must be positiv integer or "infty"

        '''
        if p == 1:
            return abs(self.x) + abs(self.y)
        elif p == 'infty':
            return max((abs(self.x), abs(self.y)))
        elif p > 0 and p == round(p, 0):
            return (self.x**p + self.y**p)**(1/p)
        else:
            raise ValueError('p must be positiv integer or "infty"')

    def scalar_multiply(self, scalar: [int, float]) -> Self:
        '''Multiplies a vector by a scalar

        In mathematics, scalar multiplication is one of the basic operations defining a vector space in linear algebra
        (or more generally, a module in abstract algebra).
        In common geometrical contexts, scalar multiplication of a real Euclidean vector by a positive real number
        multiplies the magnitude of the vector without changing its direction.
        Scalar multiplication is the multiplication of a vector by a scalar (where the product is a vector),
        and is to be distinguished from inner product of two vectors (where the product is a scalar).
        See also: https://en.wikipedia.org/wiki/Scalar_multiplication

        >>> Vector(1, 2).scalar_multiply(2)
        Vector(x=2, y=4)

        >>> Vector(0, 0).scalar_multiply(2)
        Vector(x=0, y=0)
        '''
        return Vector(self.x * scalar, self.y * scalar)

    def scalar_product(self, other_vector: Self) -> float:
        '''Returns the scalar product of vectors

        In mathematics, the dot product or scalar product[note 1] is an algebraic operation that takes two equal-length
        sequences of numbers (usually coordinate vectors), and returns a single number. In Euclidean geometry, the dot
        product of the Cartesian coordinates of two vectors is widely used. It is often called the inner product
        (or rarely projection product) of Euclidean space, even though it is not the only inner product that can be
        defined on Euclidean space (see Inner product space for more).
        See also: https://en.wikipedia.org/wiki/Dot_product

        >>> a = Vector(4, 3)
        >>> b = Vector(4, 11)
        >>> a.scalar_product(b)
        7.0
        '''
        return (self.x * other_vector.x + self.y * other_vector.y)**0.5

    def __mul__(self, other_vector: Self) -> float:
        '''Returns the scalar product of vectors. See scalar_product

        >>> a = Vector(4, 3)
        >>> b = Vector(4, 11)
        >>> a * b
        7.0
        '''
        return self.scalar_product(other_vector)

    @property
    def magnitude(self):
        '''Returns the magnitude of a vector in Euclidean space

        In mathematics, the magnitude or size of a mathematical object is a property which determines
        whether the object is larger or smaller than other objects of the same kind.
        More formally, an object's magnitude is the displayed result of an ordering (or ranking) of the
        class of objects to which it belongs.
        In physics, magnitude can be defined as quantity or distance.
        See also: https://en.wikipedia.org/wiki/Magnitude_(mathematics)

        >>> Vector(3, 4).magnitude
        5.0
        '''
        return self.norm(2)

    def __len__(self) -> int:
        '''Returns the size of a vector

        >>> len(Vector(1, 2))
        2

        >>> len(Vector())
        0

        >>> len(Vector(x=1))
        1
        '''
        size = 0
        if self.x:
            size += 1
        if self.y:
            size += 1
        return size

    @property
    def radius(self) -> float:
        '''Returns the length of the radius vector

        In geometry, a position or position vector, also known as location vector or radius vector,
        is a Euclidean vector that represents the position of a point P in space in relation to an
        arbitrary reference origin O. Usually denoted x, r, or s, it corresponds to the straight line
        segment from O to P. In other words, it is the displacement or translation that maps the origin to P.
        See also: https://en.wikipedia.org/wiki/Position_(geometry)

        >>> Vector(4, 3).radius
        5.0

        >>> Vector(1, 1).radius
        1.4142135623730951

        >>> a = Vector(1,1)
        >>> a.radius
        1.4142135623730951
        >>> a.radius = 4
        >>> a.radius
        4.0


        '''
        return self.norm(2)

    @property
    def angle(self) -> float:
        '''Returns the angle between the vector and the x axis (radians)

        >>> Vector(1, 1).angle
        0.7853981633974484

        >>> Vector(0, 1).angle
        0.0

        >>> Vector(-1, 0).angle
        1.5707963267948966

        '''
        return math.acos(self.y / self.radius)

    @radius.setter
    def radius(self, r: [int, float]) -> None:
        '''Sets the radius of the vector'''
        current_angle = self.angle
        self.x = r * math.cos(current_angle)
        self.y = r * math.sin(current_angle)

    @angle.setter
    def angle(self, a: [int, float]) -> None:
        '''Sets the angle of the vector and the x axis (radians)'''
        current_radius = self.radius
        a %= (2 * math.pi)
        self.x = current_radius * math.cos(a)
        self.y = current_radius * math.sin(a)


if __name__ == '__main__':

    import doctest
    doctest.testmod()
