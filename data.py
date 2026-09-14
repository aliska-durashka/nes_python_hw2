
class Data:
    def __init__(self, values):
        self.values = []

        for value in values:
            self.values.append(float(value))

    def count(self):     #this shit aint for me dawg
        return len(self.values)

    def sum(self):
        total = 0

        for value in self.values:
            total+= value

        return total

    def moment(self, k):
        total = 0

        for value in self.values:
            total += value ** k

        return total / self.count()

    def mean(self):
        return self.moment(1)

    def var(self):
        mean_value = self.mean()
        total = 0

        for value in self.values:
            total += (value - mean_value) ** 2

        return total / self.count()

    def std(self):
        return self.var() ** 0.5

    def skewness(self):
        mean_value = self.mean()
        std_value = self.std()
        total = 0

        for value in self.values:
            total += (value - mean_value) ** 3

        return (total / self.count()) / std_value ** 3

    def kurtosis(self):
        mean_value = self.mean()
        std_value = self.std()
        total = 0

        for value in self.values:
            total += (value - mean_value) ** 4

        return (total / self.count()) / std_value ** 4

    def percentile(self, p):
        sorted_values = sorted(self.values)
        index = int(p * self.count())

        if index >= self.count():
            index = self.count() - 1

        return sorted_values[index]

    def median(self):
        return self.percentile(0.5)

    def __str__(self):
        return (
            f"Count: {self.count()}\n"
            f"Mean: {self.mean():.6f}\n"
            f"Variance: {self.var():.6f}\n"
            f"Standard deviation: {self.std():.6f}\n"
            f"Skewness: {self.skewness():.6f}\n"
            f"Kurtosis: {self.kurtosis():.6f}\n"
            f"2nd moment: {self.moment(2):.6f}\n"
            f"3rd moment: {self.moment(3):.6f}\n"
            f"4th moment: {self.moment(4):.6f}\n"
            f"Median: {self.median():.6f}\n"
            f"25% quantile: {self.percentile(0.25):.6f}\n"
            f"75% quantile: {self.percentile(0.75):.6f}"
        )

