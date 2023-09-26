import math
class mathOps:
    """
    Simple math operations on a given pair of integers, u and v.

    This includes the lcm (least common multiple) and 
    gcd (greatest common divisor) functions, each of returns an integer.
    """

    def __init__(self, u, v):
        '''Set the values of u and v to be used in the math operations.'''
        self.u = u
        self.v = v
    
    def __repr__(self):
        return "mathOps({}, {})".format(self.u, self.v)
    
    def valid(self):
        '''True if both u and v are integers.'''
        return isinstance(self.u, int) and isinstance(self.v, int)
    
    def gcd(self):
      '''Compute the greatest common divisor of member variables u and v.'''
      # Find the greatest common divisor of a and b
      # Hint: Use Euclid's Algorithm
      # https://en.wikipedia.org/wiki/Euclidean_algorithm#Procedure
      tempU = abs(self.u)
      tempV = abs(self.v)
         
      try:
        if tempU == (float("inf") or float("-inf")) or tempV == (float("inf") or float("-inf")):
          raise OverflowError
        if not self.valid() and not isinstance(self.u, float) and not isinstance(self.v, float):
          raise TypeError
        if isinstance(self.u, float):
          tempU = math.ceil(tempU)
        if isinstance(self.v, float):
          tempV = math.ceil(tempV)
        # edge cases
        if tempU == 0 and tempV == 0:
          return 0
        elif tempU == 0 and tempV != 0:
          return tempV
        elif tempU != 0 and tempV == 0:
          return tempU

      except OverflowError:
        print("one or both the values of", tempU, " and ", tempV, "are equal to infinity")
        raise OverflowError
      
      except TypeError:
        print("one or both the values of", tempU, " and ", tempV, "are not a number")
        raise TypeError
      
      else:
        mod = tempU % tempV
        while mod > 0:
          tempU = tempV
          tempV = mod
          mod = tempU % tempV
        return tempV
          
    def lcm(self):
      '''Compute the least common multiple of member variables u and v.'''
      # Hint: Use the gcd of a and b
      try:
        tempU = abs(self.u)
        tempV = abs(self.v)
        if tempU == (float("inf") or float("-inf")) or tempV == (float("inf") or float("-inf")):
          raise OverflowError
        if self.valid() != True and not isinstance(self.u, float) and not isinstance(self.v, float):
          raise TypeError
        if tempU == 0 or tempV == 0:
          raise ValueError
        if isinstance(self.u, float):
          tempU = math.ceil(tempU)
        if isinstance(self.v, float):
          tempV = math.ceil(tempV)
      
      except OverflowError:
        print("one or both the values of ", tempU, " and ", tempV, " are equal to infinity")
        raise OverflowError
      
      except TypeError:
        print("one or both the values of", tempU, " and ", tempV, "are not a number")
        raise TypeError
      
      except ValueError:
        print("one or both the values of", tempU, " and ", tempV, " are equal to zero")
        raise ValueError
      
      else:
        return (tempU * tempV) / self.gcd()

