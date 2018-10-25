self.maximumDifference = 0


# Add your code here
def computeDifference(self):
    for n in self.__elements:
        for k in self.__elements:
            if abs(n - k) > self.maximumDifference:
                self.maximumDifference = abs(n - k)
