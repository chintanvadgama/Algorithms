class Solution:
    def meetingRooms(self,meetings):
        meetings = sorted(meetings,key=lambda x: x[0])
        for i in range(len(meetings)):
            if meetings[i+1] > meetings[i]:
                return False
        return True
    