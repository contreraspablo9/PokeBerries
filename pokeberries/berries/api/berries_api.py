"API functions module"
import concurrent.futures
from requests import get
import json
import numpy as np


class BerriesData:
    "class to manage berries data"

    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2/"
        self.berries_data = self.apicall(self.base_url + "berry/?limit=-1")
        self.complete_attributes()

    def apicall(self, url):
        "Basic HTTP GET request to json"
        response = get(url).json()
        return response

    def complete_attributes(self):
        "add main parameters to berries_data"
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # performance improvement with parallel requests
            fs = {
                executor.submit(self.apicall, berry["url"]): berry
                for berry in self.berries_data["results"]
            }
            for future in concurrent.futures.as_completed(fs):
                berry = fs[future]
                response = future.result()
                berry.update({"attributes": response})

    def names_list(self):
        "returns a list of berries names"
        return [berry["name"] for berry in self.berries_data["results"]]

    def growth_times(self):
        "Return a iterator with the growth times of all berries"
        for berry in self.berries_data["results"]:
            yield berry["attributes"]["growth_time"]

    def min_growth_time(self):
        "returns the lowest growth time"
        return min(self.growth_times())

    def median_growth_time(self):
        """
        calculates and returns the median growth time, if there are
        even growth times it will calculate the value betweeen them
        """
        growth_times_list = sorted(self.growth_times())
        size = len(growth_times_list)
        if size % 2 == 0:
            median = (
                growth_times_list[(size // 2) - 1] + growth_times_list[(size // 2)]
            ) / 2
        else:
            median = growth_times_list[(size // 2)]
        return median

    def max_growth_time(self):
        "returns the maximun growth time"
        return max(self.growth_times())

    def variance_growth_time(self):
        "returns the variance of the growth times"
        return np.var(list(self.growth_times()))

    def mean_growth_time(self):
        "returns the mean value of the growth times"
        return np.mean(list(self.growth_times()))

    def frequency_growth_time(self):
        "returns the frequency each growth times appears"
        result = {}
        for num in self.growth_times():
            if num in result:
                result[num] += 1
            else:
                result[num] = 1
        return result
