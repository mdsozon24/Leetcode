class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0] * (len(s) + 1)
        for srt, end, direc in shifts:
            if direc == 0:
                arr[srt] -= 1
                arr[end + 1] += 1
            else:
                arr[srt] += 1
                arr[end + 1] -= 1
        for i in range(1, len(s)):
            arr[i] += arr[i - 1]
        ans = ""
        for i, c in enumerate(s):
            ans += chr((ord(c) - 97 + arr[i]) % 26 + 97)
        return ans