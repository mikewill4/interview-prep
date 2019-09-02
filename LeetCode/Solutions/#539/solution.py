class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert times to minutes
        minutes = []
        for time in timePoints:
            hoursMins = time.split(":")
            minutes.append(int(hoursMins[0]) * 60 + int(hoursMins[1]))
        
        # Create bool array to mark where we have times
        boolMinutes = [False] * 1440
        for time in minutes:
            if boolMinutes[time]:
                return 0
            boolMinutes[time] = True
        
        # Iterate over bool array with two pointers finding closest times
        first = last = ptrOne = ptrTwo = -1
        minDiff = 1440
        for index,time in enumerate(boolMinutes):
            # Initializing pointers
            if time and ptrOne == -1:
                first = ptrOne = index
                continue
            if time and ptrTwo == -1:
                ptrTwo = index
                last = ptrTwo
            
            if ptrTwo != -1:
                if ptrTwo - ptrOne < minDiff:
                    minDiff = ptrTwo - ptrOne
                ptrOne = ptrTwo
                ptrTwo = -1
                
        return abs(minDiff) if abs(minDiff) < (1440 - last + first) else 1440 - last + first
