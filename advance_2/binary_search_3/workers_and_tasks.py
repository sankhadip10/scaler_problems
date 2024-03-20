class Solution:
    def no_of_task(self, arr, k):
        l = max(arr)  # The least amount of time needed is at least the longest single task.
        r = sum(arr)  # The maximum time needed if one worker does all tasks.
        ans = 0
        while (l <= r):
            mid = l + (r - l) // 2
            if self.check(arr, mid, k):  # If it's possible to do all tasks within 'mid' time
                ans = mid
                r = mid - 1  # Try to find a smaller maximum time.
            else:
                l = mid + 1  # Increase the minimum time needed.
        return ans

    def check(self, arr, time, k):
        worker = 1  # Start with one worker.
        current_work = 0
        n = len(arr)
        for i in range(n):
            if current_work + arr[i] <= time:  # Current worker can do this task.
                current_work += arr[i]
            else:  # Need a new worker for this task.
                worker += 1
                current_work = arr[i]
            if worker > k:  # If more workers needed than available, return False.
                return False
        return True  # All tasks can be done by k workers in 'time' time.


def main():
    tasks = [3, 5, 1, 7, 8, 2, 5, 3, 10, 1, 4, 7, 5, 4, 6]  # The given tasks.
    workers = 3  # Number of workers.

    solution = Solution()  # Creating an instance of the Solution class.
    min_time = solution.no_of_task(tasks, workers)  # Calculating the minimum time required.

    print(f"Minimum time to complete all tasks with {workers} workers: {min_time}")


if __name__ == "__main__":
    main()

# - **Time Complexity**: \(O(N \log(T - M))\),
# where \(N\) is the number of tasks,
# \(T\) is the sum of all task times,
# and \(M\) is the maximum task time.

# - **Space Complexity**: \(O(1)\),
# constant space, as no additional space is used that scales with the input size.