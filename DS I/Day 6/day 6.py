class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for letter in ransomNote:
            if letter in magazine:
                ransomNote = ransomNote.replace(letter, "", 1)
                magazine = magazine.replace(letter, "", 1)

        return len(ransomNote) == 0
