import operator
import collections.abc

class CookieJar:
    # INIT + PROPERTIES
    def __init__(self, chocolateChip, pbChip, butterscotchChip):
        """Create a new CookieJar object."""
        self.cChip = chocolateChip
        self.pbChip = pbChip
        self.bsChip = butterscotchChip

    @property
    def cChip(self):
        """Returns the number of galleon coins in this object."""
        return self._cChip

    @cChip.setter
    def cChip(self, value):
        if not isinstance(value, int):
             raise CookieJarException('cChip attr must be set to an int, not a ' + value.__class__.__qualname__)
        if value < 0:
            raise CookieJarException('cChip attr must be a positive int, not ' + value.__class__.__qualname__)
        self._cChip = value
    
    @cChip.deleter
    def cChip(self):
        del self.cChip

    @property
    def pbChip(self): # This is the "getter" method.
        return self._pbChip

    @pbChip.setter
    def pbChip(self, value): # This is the "setter" method.
        if not isinstance(value, int):
             raise CookieJarException('pbChip attr must be set to an int, not a ' + value.__class__.__qualname__)
        if value < 0:
            raise CookieJarException('pbChip attr must be a positive int, not ' + value.__class__.__qualname__)
        self._pbChip = value

    @pbChip.deleter
    def pbChip(self): # This is the "deleter" method.
        del self._pbChip

    @property
    def bsChip(self): # This is the "getter" method.
        return self._bsChip

    @bsChip.setter
    def bsChip(self, value): # This is the "setter" method.
        if not isinstance(value, int):
             raise CookieJarException('bsChip attr must be set to an int, not a ' + value.__class__.__qualname__)
        if value < 0:
            raise CookieJarException('bsChip attr must be a positive int, not ' + value.__class__.__qualname__)
        self._bsChip = value

    @bsChip.deleter
    def bsChip(self): # This is the "deleter" method.
        del self._bsChip

    @property
    def total(self):
        """Total value (in chips) of all the chips in this cookie jar object."""
        return (self.cChip * 29) + (self.pbChip * 22) + (self.bsChip * 15)
    # Note that there is no setter or deleter method for `total`. That means it's read only.

    # DUNDER METHODS

    def __repr__(self):
        """Returns a string of an expression that re-creates this object."""
        return f'{self.__class__.__qualname__}({self.cChip}, {self.pbChip}, {self.bsChip})'

    def __str__(self):
        """Returns a human-readable string representation of this object."""
        return f"{self.cChip} chocolate chip cookies, {self.pbChip} peanut butter chip cookies, {self.bsChip} butterscotch chip cookies"

    def __add__(self, other):
        """Adds the cookie amounts in two CookieJar objects together."""
        if not isinstance(other, CookieJar):
            return NotImplemented
        return CookieJar(other.cChip + self.cChip, other.pbChip + self.pbChip, other.bsChip + self.bsChip)
    
    def __iadd__(self, other):
        """Add the amounts in another CookieJar object to this object."""
        if not isinstance(other, CookieJar):
            return NotImplemented

        # We modify the `self` object in-place:
        self.cChip += other.cChip
        self.pbChip += other.pbChip
        self.bsChip += other.pbChip
        return self  # In-place dunder methods almost always return self.
    
    def __mul__(self, other):
        """Multiplies the cookie amounts by a non-negative integer."""
        if not isinstance(other, int):
            return NotImplemented
        if other < 0:
            # Multiplying by a negative int results in negative
            # amounts of coins, which is invalid.
            raise CookieJarException('cannot multiply with negative integers')

        return CookieJar(self.cChip * other, self.pbChip * other, self.bsChip * other)
    
    def __rmul__(self, other):
        """Multiplies the cookie amounts by a non-negative integer."""
        if not isinstance(other, int):
            return NotImplemented
        if other < 0:
            # Multiplying by a negative int results in negative
            # amounts of coins, which is invalid.
            raise CookieJarException('cannot multiply with negative integers')

        return CookieJar(self.cChip * other, self.pbChip * other, self.bsChip * other)

    def __imul__(self, other):
        """Multiply the amount of chips in this object
        by a non-negative integer amount."""
        if not isinstance(other, int):
            return NotImplemented
        if other < 0:
            raise CookieJarException('cannot multiply with negative integers')

        # Not a new CookieJar class!
        # We modify the `self` object in-place:
        self.cChip *= other
        self.pbChip *= other
        self.bsChip *= other
        return self  # In-place dunder methods almost always return self.

    def _comparisonOperatorHelper(self, operatorFunc, other):
        """A helper method for our comparison dunder methods."""

        if isinstance(other, CookieJar):
            return operatorFunc(self.total, other.total)
        elif isinstance(other, (int, float)):
            return operatorFunc(self.total, other)
        elif isinstance(other, collections.abc.Sequence):
            otherValue = (other[0] * 29) + (other[1] * 22) + (other[2] * 15)
            return operatorFunc(self.total, otherValue)
        elif operatorFunc == operator.eq:
            return False
        elif operatorFunc == operator.ne:
            return True
        else:
            return NotImplemented

    def __eq__(self, other):  # eq is "EQual"
        return self._comparisonOperatorHelper(operator.eq, other)

    def __ne__(self, other):  # ne is "Not Equal"
        return self._comparisonOperatorHelper(operator.ne, other)

    def __lt__(self, other):  # lt is "Less Than"
        return self._comparisonOperatorHelper(operator.lt, other)

    def __le__(self, other):  # le is "Less than or Equal"
        return self._comparisonOperatorHelper(operator.le, other)

    def __gt__(self, other):  # gt is "Greater Than"
       return self._comparisonOperatorHelper(operator.gt, other)

    def __ge__(self, other):  # ge is "Greater than or Equal"
       return self._comparisonOperatorHelper(operator.ge, other)

    # METHODS
    
    def value(self):
        """The value (in chips) of all the chips in the cookie jar object."""
        return (self.cChip * 29) + (self.pbChip * 22) + (self.bsChip * 15)
    
    def weightInGrams(self):
        """Returns the weight of the cookies in grams."""
        return (self.cChip * 31.103) + (self.pbChip * 11.34) + (self.bsChip * 15.0)
    

class CookieJarException(Exception):
    """The CookieJar module raises this when the module is misused."""
    pass