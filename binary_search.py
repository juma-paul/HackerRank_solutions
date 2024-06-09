from typing import List

class BinarySearch:
    """A class for performing binary search on a sorted array."""
    
    def __init__(self, arr: List[int], target: int) -> None:
        """
        Initialize the BinarySearch instance with an array and a target value.
        
        Args:
            arr (List[int]): The sorted array to search in.
            target (int): The target value to search for.
        """
        self.__arr = arr
        self.__target = target

    def search(self) -> int:
        """
        Perform binary search to find the target value in the array.
        
        Returns:
            int: The index of the target value if found, otherwise -1.
        """
        left, right = 0, len(self.__arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if self.__arr[mid] == self.__target:
                return mid
            elif self.__arr[mid] > self.__target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1

def main():
    """Main function to demonstrate binary search."""
    arr = [1, 3, 5, 7, 9]  # arr must be sorted
    target1 = 9
    target2 = 104

    # Creating instances of BinarySearch
    inst1 = BinarySearch(arr, target1)
    inst2 = BinarySearch(arr, target2)

    # Fetching the index of the target values
    idx1 = inst1.search()
    idx2 = inst2.search()

    print(f"The index of {target1} is {idx1}")
    print(f"The index of {target2} is {idx2}")

if __name__ == "__main__":
    main()
